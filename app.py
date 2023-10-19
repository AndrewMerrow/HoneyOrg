from dash import Dash, html, dcc, Input, Output, callback, dash_table
import pandas as pd
from collections import OrderedDict


app = Dash(__name__)


commands = open("/home/bsalas/cowrie.log", "r")
displayText = []
displayDict = OrderedDict()
for line in commands.readlines():
    if line.find("Command found") != -1:
        #displayText.append(line.rstrip("\n"))
        displayText.append(line)
        displayDict["type"] = "command"
        displayDict["value"] = line
    elif line.find("login attempt") != -1:
        #displayText.append(line.rstrip("\n"))
        displayText.append(line)
        displayDict["type"] = "login"
        displayDict["value"] = line
    elif line.find("Connection lost") != -1:
        #displayText.append(line.rstrip("\n"))
        displayDict["type"] = "logout"
        displayDict["value"] = line
        displayText.append(line)
    elif line.find("connection lost") != -1:
        #displayText.append(line.rstrip("\n"))
        displayText.append(line)
        displayDict["type"] = "logout"
        displayDict["value"] = line
for k, v in displayDict.items():
    print(k, v)
df = pd.DataFrame([displayDict])
#df['id'] = df.index
#display_text = "test"


#app.layout = html.Div([
#    dcc.Interval(
#        id='interval_component',
#        interval=5 * 1000,
#        n_intervals=0
#    ),
#    dcc.Textarea(
#        id='textarea',
#        value='Initial data',
#        #style={'width:' '100%', 'height': 300}
#    ),
#    #html.Meta(httpEquiv="refresh",content="5"),
#    html.Div(id='textarea-test', style={'whiteSpace': 'pre-line'})
#    
#])

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[
        {'name': 'Type', 'id':'Type', 'type':'text'},
        {'name': 'Value', 'id':'Value', 'type':'text'},
    ],
    editable=True
)

#@callback(
#    Output(component_id='textarea', component_property='value'),
#    Input(component_id='interval_component', component_property='n_intervals')
#)
def getCommands(n_intervals):
    commands = open("/home/bsalas/cowrie.log", "r")
    displayDict = OrderedDict()
    displayText = ""
    for line in commands.readlines():
        if line.find("Command found") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
            displayDict["command"] = line
        elif line.find("login attempt") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
            displayDict["login"] = line
        elif line.find("Connection lost") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
        elif line.find("connection lost") != -1:
            #displayText.append(line.rstrip("\n"))
            #displayText.append(line)
            displayText = displayText + line
            displayDict["logout"] = line

    df = pd.DataFrame(displayDict)
    
    return displayText

if __name__ == '__main__':
    app.run(debug=True)
