from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from app import app, database, twitter

# Layout do Dashboard
app.layout = html.Div([
    dcc.Input(id='filter-input', type='text', placeholder='Digite uma palavra-chave'),
    html.Br(),
    html.Div(id='trends-output')
])

# Callback para atualizar os trends com base no filtro
@app.callback(Output('trends-output', 'children'),
              [Input('filter-input', 'value')])
def update_trends(filter_keyword):
    trends = database.get_filtered_trends(filter_keyword)
    trends_list = []
    for trend in trends:
        trends_list.append(html.Div(f"Nome: {trend['name']}, Volume: {trend['tweet_volume']}"))
    return trends_list
