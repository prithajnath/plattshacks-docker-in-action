import requests as r
from flask import Flask, render_template
from random import choice
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    query = os.getenv("GIF")
    gifs = json.loads(r.get(f"https://api.giphy.com/v1/gifs/search?q={query}&api_key=uSDUmb3nwESGUPh9pz8cZs13fEbUg57d").content)
    image = choice(gifs["data"])["images"]["downsized_medium"]["url"]
    return render_template("index.html", img=image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)
