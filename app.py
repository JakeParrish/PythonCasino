import dash


app = dash.Dash(
    __name__,
    # use_pages=True, KEEP DISABLED
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

app.title = "Just one silly python casino"