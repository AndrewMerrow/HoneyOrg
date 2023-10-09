from flask import Flask

app = Flask(__name__)


@app.route('/')
def displayCommands():
    displayText = getCommands()
    #commands = open("/home/bsalas/cowrie.log", "r")
    #displayText = []
    #for line in commands.readlines():
    #    if line.find("Command found") != -1:
    #        displayText.append(line.rstrip("\n"))
    #    elif line.find("login attempt") != -1:
    #        displayText.append(line.rstrip("\n"))
    #    elif line.find("Connection lost") != -1:
    #        displayText.append(line.rstrip("\n"))
    #    elif line.find("connection lost") != -1:
    #        displayText.append(line.rstrip("\n"))



    return displayText

def getCommands():
    commands = open("/home/bsalas/cowrie.log", "r")
    displayText = []
    for line in commands.readlines():
        if line.find("Command found") != -1:
            displayText.append(line.rstrip("\n"))
        elif line.find("login attempt") != -1:
            displayText.append(line.rstrip("\n"))
        elif line.find("Connection lost") != -1:
            displayText.append(line.rstrip("\n"))
        elif line.find("connection lost") != -1:
            displayText.append(line.rstrip("\n"))
    return displayText