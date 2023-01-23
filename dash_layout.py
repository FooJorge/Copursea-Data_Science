# Import required packages
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output



app = dash.Dash()
app.layout = html.Div(children=[
    # TASK1: Add title to the dashboard
    html.H1(
        children='US Domestic Airline Flight Performance and Delay Statistics Dashboard',
        style={
            'textAlign': 'center',
            'color': '#503D36',
            'font-size': '24' 
        }
    ),

    # TASK2: Add a dropdown
    dcc.Dropdown(id='input-type', 
                   options=[
                           {'label': 'Yearly Airline Performance Report', 'value': 'OPT1'},
                           {'label': 'Yearly Airline Delay Report', 'value': 'OPT2'}
                           ],
                  placeholder='Select a report type',
                  style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlign':'center'})
    # Add Computed graphs
    # REVIEW3: Observe how we add an empty division and providing an id that will be updated during callback
    html.Div([ ], id='plot1'),
    
    html.Div([
            html.Div([ ], id='plot2'),
            html.Div([ ], id='plot3')
    ], style={'display': 'flex'}),
                                
    # TASK3: Add a division with two empty divisions inside. See above disvision for example.
    # Enter your code below. Make sure you have correct formatting.
    html.Div([
            html.Div([ ], id='plot4'),
            html.Div([ ], id='plot5')
    ], style={'display': 'flex'}),
    ])
])
# Run Application
if __name__ == '__main__':
    app.run_server()
