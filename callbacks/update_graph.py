from dash.dependencies import Input, Output, State
import plotly.express as px
from utils.parse_contents import parse_contents

def update_graph_callback(app):
    @app.callback(
        Output('graph', 'figure'),
        Input('xaxis-dropdown', 'value'),
        Input('yaxis-dropdown', 'value'),
        Input('groupby-dropdown', 'value'),
        State('upload-data', 'contents'),
        State('upload-data', 'filename')
    )
    def update_graph(xaxis_column_name, yaxis_column_name, groupby_column_name, contents, filename):
        if contents is None or xaxis_column_name is None or yaxis_column_name is None:
            return {}
        
        df, _ = parse_contents(contents, filename)

        if groupby_column_name and groupby_column_name != 'Nenhum':
            fig = px.bar(df, x=xaxis_column_name, y=yaxis_column_name, color=groupby_column_name)
        else:
            fig = px.bar(df, x=xaxis_column_name, y=yaxis_column_name)
        return fig