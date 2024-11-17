from flask import Flask

app =Flask(__name__)

@app.get("/")
def index():
    return "index page"


@app.route("/make/<slug>")
def make_url(slug:str) :
    print(slug)
    return slug
