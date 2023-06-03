from dash import html, dcc
from dash.dependencies import Input, Output
from app import app

server = app.server

app.layout = html.Div([
            dcc.Location(id='url', refresh=True),
            html.Div(id='page-content')
        ])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return 'mommy'


if __name__ == '__main__':
    app.run_server(debug=False)