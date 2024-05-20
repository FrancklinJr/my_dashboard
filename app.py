import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
from components.layout import layout
from callbacks.update_output import update_output_callback
from callbacks.update_graph import update_graph_callback

app = dash.Dash(__name__)
app.layout = layout

update_output_callback(app)
update_graph_callback(app)

if __name__ == '__main__':
    app.run_server(debug=True)