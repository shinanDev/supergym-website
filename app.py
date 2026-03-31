from flask import Flask, render_template
from database import init_db, seed_db, get_db

app = Flask(__name__)

with app.app_context():
    init_db()
    seed_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kurse")
def kurse():
    conn = get_db()
    kurse_list = conn.execute('SELECT * FROM kurse ORDER BY wochentag, uhrzeit').fetchall()
    conn.close()
    return render_template("kurse.html", kurse=kurse_list)


@app.route('/impressum')
def impressum():
    return render_template('impressum.html')


@app.route("/about")
def ueber_uns():
    return render_template("about.html")


@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html")


if __name__ == "__main__":
    app.run(debug=True)
