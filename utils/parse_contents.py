import pandas as pd
import base64
import io
import dash_html_components as html

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        else:
            return html.Div([
                'O arquivo não é um CSV.'
            ]), None
    except Exception as e:
        return html.Div([
            f'Houve um erro ao processar o arquivo: {e}'
        ]), None

    # Correção: Verificar se df é um DataFrame Pandas válido
    if isinstance(df, pd.DataFrame):
        return df, None
    else:
        return html.Div([
            'Falha ao processar o arquivo. Por favor, verifique se é um arquivo CSV válido.'
        ]), None