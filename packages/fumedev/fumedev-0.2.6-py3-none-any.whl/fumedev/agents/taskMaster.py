import tiktoken
from openai import OpenAI
import fumedev.env as env
from fumedev.agents.agent import Agent
from fumedev.prompts import task_master_system_prompt, task_master_user_prompt
from fumedev.utils.process_snippets import process_snippets

class TaskMaster(Agent):
    def __init__(self, task, snippets, medium="cli"):
        self.messages = []
        self.task = task
        self.snippets = snippets
        self.medium = medium
        self.client = OpenAI(base_url=env.BASE_URL, api_key=env.OPENAI_API_KEY)

    def solve(self, feedback="", old_plan=""):
        context = self._generate_context()
        if not context:
            print('Too many files in. the context')
            return False
        
        self.messages = [{'role': 'system', 'content': task_master_system_prompt(context=context)},
                         {'role': 'user', 'content': task_master_user_prompt(task=self.task, feedback=feedback, old_plan=old_plan, medium=self.medium)}]
        
        response = self.client.chat.completions.create(model=env.BASE_MODEL, messages=self.messages, max_tokens=4096)
        response_message = response.choices[0].message

        return response_message.content

    def _generate_context(self, max_tokens = 70000):
        encoding = tiktoken.encoding_for_model(env.BASE_MODEL)
        increment = 100
        iteration = 1
        num_tokens = 0

        while num_tokens < max_tokens:
            context_files = process_snippets(snippets=self.snippets, lines_before=increment*iteration, lines_after=increment*iteration)
            context_str = self._format_snippets(snippets=context_files)
            new_num_tokens = len(encoding.encode(context_str))
            iteration += 1
            if new_num_tokens == num_tokens:
                break
            else:
                num_tokens = new_num_tokens

        if iteration == 1:
            return False
        else:
            context_files = process_snippets(snippets=self.snippets, lines_before=increment*(iteration-1), lines_after=increment*(iteration-1))
            context_str = self._format_snippets(snippets=context_files)
            return context_str

    def _format_snippets(self, snippets):
        res = ""

        for s in snippets:
            res += f"# File Path: {env.relative_path(s.get('file_path'))}\n{s.get('code')}\n\n"

        return res
