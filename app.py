from flask import Flask
from flask import request
from task_manager_bot import TaskManagerBot
from settings import LOGIN, SECRET

import json
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = json.loads(request.data)
    task = data["task"]
    settings = json.loads(data["bot_settings"])

    bot = TaskManagerBot(LOGIN, SECRET, settings, task["id"])
    if bot.authenticated:
        response = bot.check_task()
        return response
    return "Hello"


if __name__ == "__main__":
    app.run()
