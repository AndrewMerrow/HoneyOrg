from flask import Flask

app = Flask(__name__)


@app.route('/')
def displayCommands():
    commands = open("/home/bsalas/cowrie.log", "r")
    commands = commands.readlines()
    return commands