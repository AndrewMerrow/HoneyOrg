from dash import Dash, html, dcc, Input, Output, callback


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
    dcc.Interval(
        id='interval_component',
        interval=5 * 1000,
        n_intervals=0
    ),
    dcc.Textarea(
        id='textarea',
        value='Initial data',
        #style={'width:' '100%', 'height': 300}
    ),
    #html.Meta(httpEquiv="refresh",content="5"),
    html.Div(id='textarea-test', style={'whiteSpace': 'pre-line'})
    
])

@callback(
    Output(component_id='textarea', component_property='value'),
    Input(component_id='interval_component', component_property='n_intervals')
)
def getCommands(n_intervals):
    commands = open("/home/bsalas/cowrie.log", "r")
    displayText = ""
    for line in commands.readlines():
        if line.find("Command found") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
        elif line.find("login attempt") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
        elif line.find("Connection lost") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
        elif line.find("connection lost") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
    return displayText

if __name__ == '__main__':
    app.run(debug=True)
