from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kurse")
def kurse():
    return render_template("kurse.html")


@app.route("/ueber-uns")
@app.route("/about")
def ueber_uns():
    return render_template("about.html")


@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html")


if __name__ == "__main__":
    app.run(debug=True)
