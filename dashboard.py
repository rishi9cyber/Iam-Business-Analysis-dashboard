import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load sample IAM data
data = pd.read_csv('iam-data.csv')

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("IAM Business Analysis Dashboard"),
    dcc.Graph(
        id='access-requests-chart',
        figure=px.bar(data, x='User', y='AccessRequests', title="Access Requests by User")
    ),
    dcc.Graph(
        id='role-assignments-chart',
        figure=px.pie(data, names='Role', title="Role Assignments")
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
