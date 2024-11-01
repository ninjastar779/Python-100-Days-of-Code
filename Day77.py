from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def home():
    page = ""
    f = open("templates/blog.html", "r")
    page = f.read()
    date = time.strftime("%Y-%m-%d")

    page = page.replace("{Time}", date)
    return page


app.run(host="0.0.0.0", port=81)
