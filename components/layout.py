import dash_core_components as dcc 
import dash_html_components as html

layout = html.Div([
    html.H1(children='Dashboard Interativo'),

    html.Div(children='''Faça upload de um arquivo CSV para visualizar os dados.'''),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Arraste e solte ou ',
            html.A('selecione um arquivo')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),

    html.Div(id='output-data-upload'),

    html.Label('Eixo X:'),
    dcc.Dropdown(
        id='xaxis-dropdown',
        options=[],
        value=None
    ),

    html.Label('Eixo Y:'),
    dcc.Dropdown(
        id='yaxis-dropdown',
        options=[],
        value=None
    ),

    html.Label('Agrupamento (opcional):'),
    dcc.Dropdown(
        id='groupby-dropdown',
        options=[],
        value=None
    ),

    dcc.Graph(id='graph')
])