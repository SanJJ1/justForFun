import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go


base_url = "https://raw.githubusercontent.com/plotly/datasets/master/ply/"
mesh_names = ['sandal', 'scissors', 'shark', 'walkman']
dataframes = {
    name: pd.read_csv(base_url + name + '-ply.csv') 
    for name in mesh_names
}

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Choose an object:"),
    dcc.Dropdown(
        id='dropdown',
        options=[{'value': x, 'label': x} 
                 for x in mesh_names],
        value=mesh_names[0],
        clearable=False
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")]
)
def display_mesh(name):
    df = dataframes[name]
    fig = go.Figure(go.Mesh3d(
        x=df.x, y=df.y, z=df.z, 
        i=df.i, j=df.j, k=df.k, 
        facecolor=df.facecolor
    ))

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
