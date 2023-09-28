from flask import Flask

app = Flask(__name__)


@app.route('/')
def displayCommands():
    commands = open("/home/bsalas/cowrie.log", "r")
    displayText = ""
    for line in commands.readlines():
        if line.find("Command found") != -1:
            displayText = displayText + line + "\n"

    return displayText