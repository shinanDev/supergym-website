import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import (
    init_db, seed_db, get_db,
    get_alle_kurse,
    anmelden as db_anmelden,
    freie_plaetze_reduzieren,
)

app = Flask(__name__)
app.secret_key = 'supergym-secret-key'

with app.app_context():
    init_db()
    seed_db()


@app.context_processor
def inject_anmelde_kurse():
    """Verfügbare Kurse in jedes Template injizieren — wird im Anmelde-Modal gebraucht."""
    return {'anmelde_kurse': get_alle_kurse()}


# ── Hauptrouten ──────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/kurse")
def kurse():
    conn = get_db()
    kurse_list = conn.execute('SELECT * FROM kurse ORDER BY wochentag, uhrzeit').fetchall()
    conn.close()
    return render_template("kurse.html", kurse=kurse_list)


@app.route("/kurse/<int:id>")
def kurs_details(id):
    conn = get_db()
    kurs = conn.execute('SELECT * FROM kurse WHERE id = ?', (id,)).fetchone()
    conn.close()
    if kurs is None:
        return "Kurs nicht gefunden", 404
    return render_template("kurse_details.html", kurs=kurs)


@app.route('/impressum')
def impressum():
    return render_template('impressum.html')


@app.route("/about")
def ueber_uns():
    return render_template("about.html")


@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html")


@app.route("/agb")
def agb():
    return render_template("agb.html")


# ── Anmeldung ────────────────────────────────────────────────

@app.route('/anmelden', methods=['GET', 'POST'])
def anmelden():
    if request.method == 'GET':
        # Direktaufruf der URL → einfach zurück zur Startseite
        return redirect(url_for('index'))

    # POST — kommt als fetch()-Aufruf vom Modal
    name    = request.form.get('name',    '').strip()
    email   = request.form.get('email',   '').strip()
    kurs_id = request.form.get('kurs_id', '').strip()

    if not name or not email or not kurs_id:
        return jsonify({'success': False, 'error': 'Alle Felder sind Pflichtfelder.'})

    try:
        kurs_id = int(kurs_id)
    except ValueError:
        return jsonify({'success': False, 'error': 'Ungültiger Kurs.'})

    # Race-condition-Schutz: nochmal prüfen ob Platz frei
    conn = get_db()
    kurs = conn.execute(
        'SELECT * FROM kurse WHERE id = ? AND freie_plaetze > 0', (kurs_id,)
    ).fetchone()
    conn.close()

    if kurs is None:
        return jsonify({'success': False, 'error': 'Dieser Kurs ist leider ausgebucht.'})

    db_anmelden(name, email, kurs_id, str(datetime.date.today()))
    freie_plaetze_reduzieren(kurs_id)

    return jsonify({'success': True, 'kursname': kurs['name']})


if __name__ == "__main__":
    app.run(debug=True)
