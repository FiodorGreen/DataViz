import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table,dcc, callback, Input, Output

df = pd.read_csv("C://Users/User/Downloads/ThreatenedSpecies.csv")
df_plants = df.loc[((df['Series'] == 'Threatened Species: Plants (number)'))]
df_verts = df.loc[((df['Series'] == 'Threatened Species: Vertebrates (number)'))]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1(children='Threatened Species around the World', style={'textAlign':'center'}),
    dcc.Dropdown(df_plants['Threatened species'].unique(), 'Russian Federation', id='dropdown-altogether'),
    #dcc.Dropdown(df_verts['Threatened species'].unique(), 'Russian Federation', id='dropdown-verts'),
    dcc.Graph(id='graph-content'),
    html.Div(children="\uf180 Based on the UN dataset, 2022", style = {"text-align": "center"})
    #dcc.Graph(id='graph-content-vert')
    #dcc.Graph(id = 'graph-content-unvert')
    #dcc.Graph(od = 'graph-content-total')
])
@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-altogether', 'value')
)
def update_graph(value):
    dff = df[df['Threatened species']==value]
    #dfv = df_verts[df_verts['Threatened species'] == value]
    return px.line(dff, x='Year', y='Value', color='Series')# px.line(dfv, x = 'Year', y = 'Value')

if __name__ == '__main__':
    app.run_server(debug=True)
