from dash import Dash, html

app = Dash(__name__)


commands = open("/home/bsalas/cowrie.log", "r")
displayText = []
for line in commands.readlines():
    if line.find("Command found") != -1:
        #displayText.append(line.rstrip("\n"))
        displayText.append(line)
    elif line.find("login attempt") != -1:
        #displayText.append(line.rstrip("\n"))
        displayText.append(line)
    elif line.find("Connection lost") != -1:
        #displayText.append(line.rstrip("\n"))
        displayText.append(line)
    elif line.find("connection lost") != -1:
        #displayText.append(line.rstrip("\n"))
        displayText.append(line)
#display_text = "test"

app.layout = html.Div([
    html.Meta(httpEquiv="refresh",content="5"),
    html.Div(displayText, style={'whiteSpace': 'pre-line'})
])

if __name__ == '__main__':
    app.run(debug=True)
