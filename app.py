import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
from dotenv import load_dotenv
from helpers.create_joke import create_joke

load_dotenv()
app = Flask(__name__)

NEW_FEATURES = os.environ["NEW_FEATURES"]

@app.route('/')
def index():
    if NEW_FEATURES == "on":
        return render_template("index_joke_feature.html")
    return render_template("index.html")


@app.route("/images/clippy.png")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "images/clippy.png",
        mimetype="image/vnd.microsoft.icon",
    )

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get("name")
    if NEW_FEATURES == "on":
        title = request.form.get("title")
        joke = create_joke(name, title)
        if name:
            return render_template("hello_joke_feature.html", joke=joke)
        print("Request for hello page received with no name or blank name -- redirecting")
        return redirect(url_for("index"))
    if (name):
        return render_template("hello.html", name=name)
    print("Request for hello page received with no name or blank name -- redirecting")
    return redirect(url_for("index"))


if __name__ == '__main__':
   app.run()