from dash import Dash, html, dcc, Input, Output, callback, dash_table
import pandas as pd
from collections import OrderedDict


app = Dash(__name__)


commands = open("/home/bsalas/cowrie.log", "r")
displayDict = OrderedDict()
displayDict['type'] = []
displayDict['value'] = []
for line in commands.readlines():
    if line.find("Command found") != -1:
        displayDict["type"].append("command")
        displayDict["value"].append(line.rstrip("\n"))
    elif line.find("login attempt") != -1:
        displayDict["type"].append("login")
        displayDict["value"].append(line.rstrip("\n"))
    elif line.find("Connection lost") != -1:
        displayDict["type"].append("logout")
        displayDict["value"].append(line.rstrip("\n"))
    elif line.find("connection lost") != -1:
        displayDict["type"].append("logout")
        displayDict["value"].append(line.rstrip("\n"))

df = pd.DataFrame(displayDict)


app.layout = html.Div([
    dcc.Interval('table-update', interval=5 * 1000, n_intervals = 0),
    dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        sort_action='native',
        columns=[
            {'name': 'Type', 'id':'type', 'type':'text'},
            {'name': 'Value', 'id':'value', 'type':'text'},
        ],
        style_data_conditional=[
            {
                'if': {
                    'column_type': 'text'
                },
                'textAlign': 'left'
            },
            #set color for command logs
            {
                'if': {
                    'filter_query': '{type} = command',
                },
                'backgroundColor': 'tomato',
                'color': 'white'
            },
            #set color for login/logout logs
            {
                'if': {
                    'filter_query': '{type} = login || {type} = logout',
                },
                'backgroundColor': '#0000ff',
                'color': 'white'
            }
        ]
    )
])

@callback(
    Output(component_id='table', component_property='data'),
    Input(component_id='table-update', component_property='n_intervals')
)
def getCommands(n_intervals):
    '''Update function that reads the log file and updates the table every 5 seconds'''
    commands = open("/home/bsalas/cowrie.log", "r")
    displayDict = OrderedDict()
    displayDict['type'] = []
    displayDict['value'] = []
    for line in commands.readlines():
        #Search the log file lines for specific phrases
        if line.find("Command found") != -1:
            displayDict["type"].append("command")
            displayDict["value"].append(line.rstrip("\n"))
        elif line.find("login attempt") != -1:
            displayDict["type"].append("login")
            displayDict["value"].append(line.rstrip("\n"))
        elif line.find("Connection lost") != -1:
            displayDict["type"].append("logout")
            displayDict["value"].append(line.rstrip("\n"))
        elif line.find("connection lost") != -1:
            displayDict["type"].append("logout")
            displayDict["value"].append(line.rstrip("\n"))

    df = pd.DataFrame(displayDict)
    
    return df.to_dict('records')

if __name__ == '__main__':
    app.run(debug=True)
