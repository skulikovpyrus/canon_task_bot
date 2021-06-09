from flask import Flask
from flask import request, Response
from bot import Bot


import json
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = json.loads(request.data)
    task = data["task"]
    settings = json.loads(data["bot_settings"])

    bot = Bot(settings, task)
    _response = bot.check_task()
    if _response:
        return _response
    return Response(status=200)


if __name__ == "__main__":
    app.run()
