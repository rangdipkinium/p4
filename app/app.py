
import datetime
import copy
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from dog_code import human_dog_predict

# Use external stylesheets
external_stylesheets = \
    [
        {
            "href": "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap",
            "rel": "stylesheet",
        },
    ]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Format app layout
app.layout = html.Div([
    html.Div(
        children=[
            html.P(children="\U0001F436", className="header-emoji"),
            html.H1(
                children="CNN Dog Classifier", className="header-title"
            ),
            html.P(
                children="Select Your Image, then wait for magic",
                className="header-description",
            ),
        ],
        className="header"
    ),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
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
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),
])

# Parse contents of file upload
def parse_contents(contents, filename, date, pred):
    return html.Div([
                    html.H5(pred),
                    html.H6(datetime.datetime.fromtimestamp(date)),
                    # HTML images accept base64 encoded strings in the same format
                    # that is supplied by the upload
                    html.Img(src=contents, style={'height': '10%', 'width': '10%'}),
                    html.Hr()


                    ])

# Pass in image upload
@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        strimg = copy.copy(list_of_contents[0])
        children = [
            parse_contents(
                c, n, d, e) for c, n, d, e in zip(
                list_of_contents, list_of_names, list_of_dates, [
                    human_dog_predict(strimg)])]
        return children


if __name__ == '__main__':
    app.run_server(port=8000, debug=True)
