import os
from fumedev import env
from fumedev.git_ops.github_ops.app import GithubApp


env.FILE_FOLDER = os.path.dirname(os.path.abspath(__file__))
os.makedirs(env.USER_HOME_PATH.joinpath('FumeData'), exist_ok=True) 

from dotenv import load_dotenv
from fumedev.gui.app import FumeApp

load_dotenv()
def main():
    app = FumeApp()
    app.run()

if __name__ == "__main__":
    if env.BOT_MODE and env.REPO_SERVICE == 'GITHUB':
        env.GITHUB_APP =  GithubApp()
    main()