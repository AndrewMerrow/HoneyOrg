from dash import Dash, html, dcc, Input, Output, callback, dash_table
import pandas as pd
from collections import OrderedDict


app = Dash(__name__)

commands = open("/home/bsalas/cowrie.log", "r")
displayDict = OrderedDict()
displayDict['type'] = []
displayDict['value'] = []
displayDict['ID'] = []
for line in commands.readlines():
    if line.find("Command found") != -1:
        displayDict["type"].append("command")
        displayDict["value"].append(line.rstrip("\n"))
        sessionID = line.split(',')[1]
        displayDict['ID'].append(sessionID)
        print(sessionID)
    elif line.find("login attempt") != -1:
        displayDict["type"].append("login")
        displayDict["value"].append(line.rstrip("\n"))
        sessionID = line.split(',')[1]
        displayDict['ID'].append(sessionID)
    elif line.find("Connection lost") != -1:
        displayDict["type"].append("logout")
        displayDict["value"].append(line.rstrip("\n"))
        displayDict['ID'].append(sessionID)
        sessionID = line.split(',')[1]
    #elif line.find("connection lost") != -1:
    #    displayDict["type"].append("logout")
    #    displayDict["value"].append(line.rstrip("\n"))
    #    sessionID = line.split(',')[1]
    #    displayDict['ID'].append(sessionID)

df = pd.DataFrame(displayDict)

app.layout = html.Div([
    dcc.Tabs(id='tabs-test-1', value='tab-test-1', children=[
        dcc.Tab(label='Tab One', value='tab-test-1'),
        dcc.Tab(label='Tab Two', value='tab-test-2'),
    ]),
    html.Div(id='tabs-content-test'),
    html.Div([
    dcc.Interval('table-update', interval=5 * 1000, n_intervals = 0),
    dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        #enble filtering 
        filter_action='native',
        sort_action='native',
        columns=[
            {'name': 'Type', 'id':'type', 'type':'text'},
            {'name': 'ID', 'id': 'ID', 'type':'text'},
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
])

@callback(Output('table', 'data'),
          Input('tabs-test-1', 'value'),
          Input('table-update', 'n_intervals'))
def render_content(tab, n_intervals):
    if tab == 'tab-test-1':
        '''Update function that reads the log file and updates the table every 5 seconds'''
        commands = open("/home/bsalas/cowrie.log", "r")
        displayDict = OrderedDict()
        displayDict['type'] = []
        displayDict['value'] = []
        displayDict['ID'] = []
        for line in commands.readlines():
            #Search the log file lines for specific phrases
            if line.find("Command found") != -1:
                displayDict["type"].append("command")
                displayDict["value"].append(line.rstrip("\n"))
                sessionID = line.split(',')[1]
                displayDict['ID'].append(sessionID)
            elif line.find("login attempt") != -1:
                displayDict["type"].append("login")
                displayDict["value"].append(line.rstrip("\n"))
                sessionID = line.split(',')[1]
                displayDict['ID'].append(sessionID)
            elif line.find("Connection lost") != -1:
                displayDict["type"].append("logout")
                displayDict["value"].append(line.rstrip("\n"))
                sessionID = line.split(',')[1]
                displayDict['ID'].append(sessionID)
            #elif line.find("connection lost") != -1:
            #    displayDict["type"].append("logout")
            #    displayDict["value"].append(line.rstrip("\n"))

        df = pd.DataFrame(displayDict)
        
        return df.to_dict('records')

    elif tab == 'tab-test-2':
        commands = open("/home/bsalas/alert", "r")
        displayDict = OrderedDict()
        displayDict['type'] = []
        displayDict['value'] = []
        displayDict['ID'] = []
        for line in commands.readlines():
            #print(line.rstrip('\n').split("[**]"))
            displayDict['type'] = 'test'
            final_value = ""
            #for value in line.rstrip('\n').split("[**]")[0:2]:
            #    final_value += value
            displayDict['value'] = "blah"
            print(final_value)
            displayDict['ID'] = '0'
            break
        df = pd.DataFrame(displayDict)
        return df.to_dict('records')


if __name__ == '__main__':
    app.run(debug=True)
