import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['assets/style_2.css', 'assets/style.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,  meta_tags=[{"name": "viewport", "content": "width=device-width"}])


layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Dash Data Visualization",
    #dragmode="select",
    showlegend= False
)



app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("tvd.svg"),
                            id="plotly-image",
                            style={
                                "height": "40px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Atemteurer",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "AiTrainer", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://www.trivadis.com/de/big-data-science",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    dcc.Graph(
                        id='example-graph',
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                            ],
                            'layout': layout
                        }
                    ),
                    id="right-column",
                    className="twelve columns pretty_container",
                ),
            ],
            className="row flex-display",
        )

    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"}
)

if __name__ == '__main__':
    app.run_server(debug=True)