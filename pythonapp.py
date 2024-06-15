import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load your data
# Assuming your data is in a CSV file named 'sales_data.csv'
df = pd.read_csv('sales_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Sales Data Visualizer'),
    dcc.Graph(id='sales-line-chart')
])

# Create a callback to update the graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('sales-line-chart', 'id')  # Dummy input to trigger the callback
)
def update_graph(_):
    fig = px.line(df, x='date', y='sales', title='Sales of Pink Morsels Over Time')
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
