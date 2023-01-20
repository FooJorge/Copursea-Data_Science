# Import required packages
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# Add Dataframe

# Add a bar graph figure

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(
        children='US Domestic Airline Flight Performance and Delay Statistics Dashboard',
        style={
            'textAlign': 'center',
            'color': '#503D36',
            'font-size': '24' 
        }
    )

    # Create dropdown
    dcc.Dropdown(id='....', 
                   options=[
                           {'label': 'Yearly Airline Performance Reportearly Airline Performance Reportearly Airline Performance Reportearly Airline Performance Reportearly Airline Performance Report', 'value': 'OPT1'},
                           {'label': 'Yearly Airline Delay Report', 'value': 'OPT2'}
                           ],
                  placeholder='....',
                  style={....})
    # Bar graph
])

# Run Application
if __name__ == '__main__':
    app.run_server()
