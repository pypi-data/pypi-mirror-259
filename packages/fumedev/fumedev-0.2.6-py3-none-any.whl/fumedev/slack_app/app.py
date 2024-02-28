import copy
import os
from dotenv import load_dotenv
from fumedev.agents.coderMinion import CoderMinion

from fumedev.agents.philosopher import Philosopher
from fumedev.lllm_utils.if_changes_needed import if_changes_needed
from fumedev.lllm_utils.split_complex_task import split_complex_task
from fumedev.utils.create_diff import create_diff
from fumedev.utils.process_snippets import process_snippets
load_dotenv()
from slack_bolt import App
from slack_sdk import WebClient

# Load environment variables (make sure SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET are set)
import fumedev.env as env 
from fumedev.lllm_utils.generate_search_phrases import generate_search_phrases
from fumedev.utils.search_snippet import search_snippet
from fumedev.agents.taskMaster import TaskMaster
from fumedev.utils.remove_at_words import remove_at_words

env.CLOUD_HOSTED = True
env.OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

app = App(
    token=env.SLACK_BOT_TOKEN,
    signing_secret=env.SLACK_SIGNING_SECRET,
)

# Function to process a single message (for text and images) 
def process_message(message):
    text = message.get('text', '')
    print(f"Message Text: {text}") 

    if 'files' in message:
        for file in message['files']:
            if file.get('filetype') == 'image':  
                image_url = file['url_private']  # Or appropriate URL variant
                print(f"Image Found: {image_url}")
                # Do something with the image URL

@app.event("app_mention")
def handle_mention(event, say, client):
    channel_id = event['channel'] 
    thread_ts = event.get('thread_ts', event['ts'])

    # React to the mention with eyes emoji
    client.reactions_add(
        channel=event['channel'],
        timestamp=event['ts'],
        name="eyes"
    )

    if not globals().get('FILE_PATHS'):
        globals()["FILE_PATHS"] = []

    formatted_messages = []  # Initialize an empty list to store message information

    # try:
    if True:
        result = client.conversations_replies(
            channel=channel_id,
            ts=thread_ts
        )
        messages = result['messages']
        for message in messages:
            # Handle text content of the message
            if message.get('text', ''):
                formatted_messages.append({"type": "text", "text": message['text']})

            # Handle files (including images) attached to the message
            if 'files' in message:
                for file in message['files']:
                    if file['mimetype'].startswith('image/'):
                        image_url = file['url_private']
                        formatted_messages.append({"type": "image_url", "image_url": {"url": image_url}})

            # Handle images embedded in blocks (optional)
            if 'blocks' in message:
                for block in message['blocks']:
                    if block['type'] == 'image':
                        image_url = block['image_url']
                        formatted_messages.append({"type": "image_url", "image_url": {"url": image_url}})

        env.BASE_MODEL = "gpt-4-vision-preview"

        task = []

        for message in formatted_messages:
            if message.get('type') == "text":
                message["text"] = remove_at_words(text=message.get("text"))
                task.append(message)
            else:
                task.append(message)

        env.TASK = formatted_messages
        phrases = generate_search_phrases(task=formatted_messages, medium="slack")

        file_paths = []

        for phrase in phrases:

            query = phrase.get('phrase')
            extension = phrase.get('file_extension')

            snip_lst, files = search_snippet(query=query, extension=extension)

            file_paths += files
            file_paths = list(set(file_paths))

            env.SNIPPETS += snip_lst 

        options = []
        globals()["FILE_PATHS"] = file_paths

        for idx, p in enumerate(file_paths):
            option = {
                        "text": {
                            "type": "mrkdwn",
                            "text": env.relative_path(path= p)
                        },
                        "value": p
                    }
            options.append(option)

        blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Here are the files I selected for this task. Please un select the ones you think are irrelevant or add more using /add command"
                    },
                    "accessory": {
                        "type": "checkboxes",
                        "options": options[:10],
                        "initial_options": options[:10],
                        "action_id": "checkboxes_action"
                    }
                },
                {
                "type": "actions",
                "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Done"
                            },
                            "action_id": "done_button"
                        }
                    ]
                }
        ]

        # Now formatted_messages contains all messages in the specified format
        say(
            blocks=blocks,
            text=f"Hi, I selected relevant files for the task!"
        )
        # You can use the formatted_messages list as needed

    # except Exception as e:
    #     print(f"Error fetching thread messages: {e}")

# Helper function: Assumes threads are simple sequences before the mention
def find_original_message(messages, mention_ts):
    for message in messages:  # Iterate in reverse for efficiency 
        if message['ts'] > mention_ts:  # If the message is older than the mention
            continue
        else:
            return

@app.action("done_button")
def handle_done_button(ack, body, client, say):
    # Acknowledge the button click
    ack()
    
    # Extract the selected options from the state
    selected_options = body['state']['values']
    # Process the selected options to get a list of their values
    # This part depends on how your checkboxes are structured and may need adjustment
    selected_values = [option['value'] for block_id, action_id in selected_options.items() for option in action_id['checkboxes_action']['selected_options']]
    removed_files = [file for file in globals()["FILE_PATHS"] if file not in selected_values]

    new_snippets = [snip for snip in env.SNIPPETS if snip.get('file_path') not in removed_files]
    new_files = [file for file in globals()['FILE_PATHS'] if file not in removed_files]

    env.SNIPPETS = new_snippets
    globals()["FILE_PATHS"] = new_files
    
    # Respond with the list of selected options
    say(f":hourglass_flowing_sand: Planning what to do...")

    task_master = TaskMaster(task=env.TASK, snippets=env.SNIPPETS, medium="slack")
    plan = task_master.solve()
    globals()['PLAN'] = plan

    plan_paragraphs = plan.split('\n\n')

    blocks = []
    for paragraph in plan_paragraphs:
        while len(paragraph) > 3000:
            part = paragraph[:3000]
            end_index = part.rfind("\n")
            if end_index == -1:
                end_index = 3000

            blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": paragraph[:end_index]}})
            paragraph = paragraph[end_index:]

        if paragraph:
            blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": paragraph}})
    start_block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Here is the plan I came up with:\n\nDoes this plan look good to you?"
        },
    }

    confirmation_blocks = [
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Yes"
                    },
                    "action_id": "plan_yes_button"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "No"
                    },
                    "action_id": "plan_no_button"
                }
            ]
        }
    ]

    blocks = [start_block] + blocks + confirmation_blocks

    say(blocks=blocks, text="I'm done with the plan! Can you please review it?")

@app.action("plan_no_button")
def handle_plan_rejection(ack, body, say):
    ack()
        # Respond with the list of selected options
    globals()['FEEDBACK_MODE'] = 'task_master'
    say(f"How should I change it? Please use /edit tool to give feedback.")

@app.action("plan_yes_button")
def handle_plan_approval(ack, body, say):
    ack()

    env.BASE_MODEL = 'gpt-4-0125-preview'

    say(f":technologist: Writing the code...")

    diffs = []
    isDone = False

    while not isDone:
        snippets_copy = copy.deepcopy(env.SNIPPETS)
        processed_snippets = process_snippets(snippets=snippets_copy)

        phil = Philosopher(task=globals()["PLAN"], snippets=processed_snippets, short_snippets=env.SNIPPETS, diffs=diffs)

        res = phil.generate_step()

        if res:
            action, file_paths, current_snippets, new_file = res

            if len(file_paths) > 1:
                print_files = ', '.join([env.relative_path(f) for f in file_paths])
                say(f"Working on {print_files}")
            else:
                print_files = env.relative_path(file_paths[0])
                say(f"Working on {print_files}")

            action_word = "modified"

            new_snippets = [snippet for snippet in env.SNIPPETS if not snippet.get('file_path') in file_paths]
            env.SNIPPETS = new_snippets

            if new_file:
                diffs.append(f"* You created {print_files}. Here is what you did:\n{action}")

                CoderMinion(task=action, file_paths=file_paths).create_file()

                continue

            changes = if_changes_needed(speech=action)

            decision = changes.get('decision')
            is_multiple = changes.get('is_multiple')

            if decision:
                diffs.append(f"* You {action_word} {print_files}. Here is what you did:\n{action}")
                if is_multiple:
                    old_files = []
                    for path in file_paths:
                        with open(path, 'r') as file:
                            old_files.append(file.read())

                    sub_tasks_dict = split_complex_task(action)

                    sub_tasks = sub_tasks_dict.get('plan')
                    for t in sub_tasks:

                        task = '# ' + t.get('task') + '\n' + '* ' + '\n'.join(t.get('steps'))

                        coder = CoderMinion(task=task, file_paths=file_paths)
                        coder.code()

                else:
                    new_snippets = [snippet for snippet in env.SNIPPETS if not snippet.get('file_path') in file_paths]
                    env.SNIPPETS = new_snippets

                    old_files = []
                    for path in file_paths:
                        with open(path, 'r') as file:
                            old_files.append(file.read())

                    # Assuming 'action' is defined elsewhere and appropriate for 'task'
                    coder = CoderMinion(task=action, file_paths=file_paths)
                    coder.code()
            else:
                for path in file_paths:
                    diffs.append(f"* You decied no changes are necessary for {env.relative_path(path=path)}. There is no need to select them again. Here is your reasoning:\n {action}")

        else:
            isDone = True

@app.action("checkboxes_action")
def handle_some_action(ack, body, logger):
    ack()
    logger.info(body)

@app.command("/add")
def handle_add(ack, body, say):
    # Acknowledge the button click
    ack()

    if not globals().get('FILE_PATHS'):
        globals()["FILE_PATHS"] = []

    text = body['text']

    say(f':mag: Searching "{text}"')

    phrases = text.split(',')

    file_paths = []

    for phrase in phrases:

            query = phrase.strip()

            snip_lst, files = search_snippet(query=query)

            snip_lst = [snip for snip in snip_lst if snip.get('file_path') not in globals()["FILE_PATHS"]]
            files = [f for f in files if f not in globals()["FILE_PATHS"]]

            file_paths += files
            file_paths = list(set(file_paths))

            env.SNIPPETS += snip_lst 

    options = []
    globals()["FILE_PATHS"] += file_paths

    for idx, p in enumerate(file_paths):
        option = {
                    "text": {
                        "type": "mrkdwn",
                        "text": env.relative_path(path= p)
                    },
                    "value": p
                }
        options.append(option)


    if file_paths:
        blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Here a are the files I added to the context"
                    },
                    "accessory": {
                        "type": "checkboxes",
                        "options": options[:10],
                        "initial_options": options[:10],
                        "action_id": "checkboxes_action"
                    }
                },
                {
                "type": "actions",
                "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Done"
                            },
                            "action_id": "done_button"
                        }
                    ]
                }
            ]
    else:
        blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Couldn't find any files that are not already in the context :confused:"
                    },
                },
                {
                "type": "actions",
                "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Done"
                            },
                            "action_id": "done_button"
                        }
                    ]
                }
            ]

    # Now formatted_messages contains all messages in the specified format
    say(
        blocks=blocks,
        text=f"Hi, I selected relevant files for your query!"
    )

@app.command("/edit")
def handle_feedback(ack, body, say):
    # Acknowledge the button click
    ack()

    feedback = body['text']

    say(f":writing_hand: Revising my plan with you feedback.")

    mode =  globals()['FEEDBACK_MODE']

    if mode == 'task_master':
        task_master = TaskMaster(task=env.TASK, snippets=env.SNIPPETS, medium="slack")
        plan = task_master.solve(feedback=feedback, old_plan=globals()['PLAN'])
        globals()['PLAN'] = plan
    else:
        say("There is nothing to give feedback for? I think you made a mistake:confused:")
        return

    plan_paragraphs = plan.split('\n\n')

    blocks = []
    for paragraph in plan_paragraphs:
        while len(paragraph) > 3000:
            part = paragraph[:3000]
            end_index = part.rfind("\n")
            if end_index == -1:
                end_index = 3000

            blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": paragraph[:end_index]}})
            paragraph = paragraph[end_index:]

        if paragraph:
            blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": paragraph}})
    start_block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Here is the new plan I came up with:\n\nDoes this look good now?"
        },
    }

    confirmation_blocks = [
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Yes"
                    },
                    "action_id": "plan_yes_button"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "No"
                    },
                    "action_id": "plan_no_button"
                }
            ]
        }
    ]

    blocks = [start_block] + blocks + confirmation_blocks

    say(blocks=blocks, text="I edited the plan! Can you please review it?")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))