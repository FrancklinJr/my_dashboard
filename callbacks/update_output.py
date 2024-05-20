from dash.dependencies import Input, Output, State
from utils.parse_contents import parse_contents
import dash_html_components as html

def update_output_callback(app):
    @app.callback(
        Output('output-data-upload', 'children'),
        Output('xaxis-dropdown', 'options'),
        Output('yaxis-dropdown', 'options'),
        Output('groupby-dropdown', 'options'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename')
    )
    def update_output(contents, filename):
        if contents is not None:
            df, error = parse_contents(contents, filename)
            if error:
                return error, [], [], []
            if hasattr(df, 'columns'):
                options = [{'label': col, 'value': col} for col in df.columns]
                return '', options, options, [{'label': 'Nenhum', 'value': 'Nenhum'}] + options
            else:
                return html.Div(['Erro ao carregar o arquivo']), [], [], []
        else:
            return '', [], [], []