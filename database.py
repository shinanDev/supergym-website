import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'supergym.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS kurse (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT NOT NULL,
            beschreibung  TEXT,
            niveau        TEXT,
            wochentag     TEXT,
            uhrzeit       TEXT,
            dauer         INTEGER,
            trainer       TEXT,
            kapazitaet    INTEGER,
            freie_plaetze INTEGER
        );

        CREATE TABLE IF NOT EXISTS anmeldungen (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT NOT NULL,
            email    TEXT NOT NULL,
            kurs_id  INTEGER REFERENCES kurse(id),
            datum    TEXT
        );

        CREATE TABLE IF NOT EXISTS mitglieder (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            vorname  TEXT NOT NULL,
            nachname TEXT NOT NULL,
            email    TEXT NOT NULL,
            telefon  TEXT,
            datum    TEXT
        );
    ''')
    conn.commit()
    conn.close()


def seed_db():
    conn = get_db()
    count = conn.execute('SELECT COUNT(*) FROM kurse').fetchone()[0]
    if count == 0:
        conn.executemany(
            '''INSERT INTO kurse (name, beschreibung, niveau, wochentag, uhrzeit, dauer, trainer, kapazitaet, freie_plaetze)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            [
                ('HIIT Burn',
                 'Kurze, explosive Belastungsphasen wechseln sich mit kontrollierten Erholungspausen ab – das maximiert die Fettverbrennung und steigert gleichzeitig deine Ausdauer. Kein Equipment nötig, nur dein Körpergewicht und die Bereitschaft, alles zu geben. Nach diesem Kurs brennst du noch stundenlang Kalorien – der sogenannte Nachbrenneffekt macht es möglich. Für alle, die wirklich Ergebnisse sehen wollen.',
                 'Fortgeschritten', 'Montag', '18:00', 45, 'Alex Petrov', 20, 8),
                ('Yoga Flow',
                 'Sanft fließende Yoga-Sequenzen verbinden Atemarbeit, Bewegung und Achtsamkeit zu einem kraftvollen Gesamterlebnis. Du durchläufst dynamische Abfolgen, die Flexibilität, Gleichgewicht und Körperbewusstsein gleichzeitig fördern. Ob Yoga-Einsteiger oder regelmäßige Praxis – dieser Kurs begegnet dir genau dort, wo du gerade stehst, und begleitet dich einen Schritt weiter.',
                 'Alle Level', 'Montag', '10:00', 60, 'Lena Hartmann', 15, 5),
                ('Kraftzirkel',
                 'Im Zirkel-Format wechselst du in schneller Folge zwischen verschiedenen Stationen und trainierst dabei alle großen Muskelgruppen. Freie Gewichte, Kettlebells und Körpergewichtsübungen kombinieren sich zu einem effizienten Ganzkörper-Workout. Das Format hält die Herzfrequenz dauerhaft oben und baut gleichzeitig funktionelle Kraft auf – ideal, wenn du in kurzer Zeit maximale Ergebnisse erzielen willst.',
                 'Mittel', 'Dienstag', '17:00', 50, 'Alex Petrov', 18, 12),
                ('Kickbox Cardio',
                 'Grundlagen der Boxtechnik treffen auf ein intensives Cardio-Workout. Du erlernst Schlag- und Trittkombinationen und setzt sie in rhythmischen, choreografierten Sequenzen ein – ganz ohne Kontakt zum Partner. Der Kurs verbessert Koordination, Reaktionsvermögen und konditionelle Fitness gleichzeitig. Perfekt für alle, die Kampfsport-Feeling suchen, ohne sich auf den Ring vorzubereiten. Handschuhe werden gestellt.',
                 'Alle Level', 'Dienstag', '19:00', 60, 'Marco da Silva', 16, 3),
                ('Morning Stretch',
                 'Der perfekte Start in den Tag: Sanfte Dehnübungen lösen nächtliche Verspannungen, aktivieren die Muskulatur und bereiten deinen Körper auf die täglichen Belastungen vor. Der Fokus liegt auf tiefen Dehnungen für Rücken, Hüfte und Beine sowie auf mobilisierenden Bewegungen für die Wirbelsäule. Wer regelmäßig dabei ist, bemerkt schnell eine bessere Körperhaltung und deutlich weniger Rückenschmerzen.',
                 'Anfänger', 'Mittwoch', '07:30', 30, 'Lena Hartmann', 12, 7),
                ('Power Lifting Basics',
                 'Hier lernst du die drei Königsdisziplinen des Kraftsports: Kniebeuge, Kreuzheben und Bankdrücken. Trainer Alex Petrov erklärt Schritt für Schritt die korrekte Ausführung, optimale Körperspannung und den richtigen Einsatz von Hilfsmitteln wie Hebegürtel und Kniebandagen. Mit solider Technik legst du das Fundament für langfristigen Kraftaufbau und minimierst gleichzeitig das Verletzungsrisiko.',
                 'Anfänger', 'Mittwoch', '18:00', 60, 'Alex Petrov', 10, 2),
                ('Yoga Deep',
                 'Ein Kurs für alle, die tiefer in ihre Praxis eintauchen wollen. Lange gehaltene Positionen, bewusste Atemarbeit und gezielte Faszienarbeit lösen chronische Spannungen und fördern aktiv die Regeneration. Der Fokus liegt weniger auf Dynamik als auf dem bewussten Wahrnehmen des eigenen Körpers. Besonders empfehlenswert nach intensiven Trainingseinheiten oder bei stressbedingter Verspannung.',
                 'Alle Level', 'Donnerstag', '10:00', 75, 'Lena Hartmann', 15, 10),
                ('Fight Fit',
                 'Ein Workout für erfahrene Sportler, das Elemente aus Muay Thai, Boxing und funktionellem Krafttraining kombiniert. Du steigerst explosive Kraft, Reaktionsschnelligkeit und anaerobe Ausdauer auf einem Niveau, das dich wirklich fordert. Der Kurs setzt ein solides Grundfitnesslevel voraus und ist nichts für halbherzige Trainingseinheiten – dafür verlässt du ihn jedes Mal stärker als davor.',
                 'Fortgeschritten', 'Donnerstag', '19:00', 60, 'Marco da Silva', 16, 0),
                ('HIIT Express',
                 'Wenig Zeit, maximaler Effekt. In nur 30 Minuten bringst du mit diesem kompakten HIIT-Format deinen Stoffwechsel auf Hochtouren. Kurze Arbeitsintervalle von 40 Sekunden, gefolgt von 20 Sekunden Pause – wiederholt in mehreren Runden mit wechselnden Übungen. Perfekt für die Mittagspause oder wenn du einen knappen Zeitplan hast, aber keine Abstriche beim Training machen willst.',
                 'Mittel', 'Freitag', '12:00', 30, 'Alex Petrov', 20, 14),
                ('Weekend Warrior',
                 'Das Samstags-Special vereint Elemente aus Funktionstraining, Ausdauersport und Teamübungen zu einem abwechslungsreichen 75-Minuten-Block. Jede Woche wartet eine andere Kombination – kein Training ist wie das andere. Trainer Marco da Silva bringt seine vielseitige Erfahrung ein und sorgt dafür, dass du das Wochenende mit einem echten Erfolgsgefühl und müden Muskeln startest.',
                 'Alle Level', 'Samstag', '10:00', 75, 'Marco da Silva', 20, 6),
            ]
        )
        conn.executemany(
            'INSERT INTO anmeldungen (name, email, kurs_id, datum) VALUES (?, ?, ?, ?)',
            [
                ('Lisa Müller',   'lisa.mueller@example.com',  1, '2026-03-28'),
                ('Tom Berger',    'tom.berger@example.com',    2, '2026-03-28'),
                ('Sarah Klein',   'sarah.klein@example.com',   4, '2026-03-29'),
                ('Max Hoffmann',  'max.hoffmann@example.com',  6, '2026-03-29'),
                ('Nina Weber',    'nina.weber@example.com',   10, '2026-03-30'),
            ]
        )
        conn.commit()
    conn.close()


def get_alle_kurse():
    """Alle Kurse mit freien Plätzen — für das Anmelde-Dropdown."""
    conn = get_db()
    kurse = conn.execute(
        'SELECT id, name, wochentag, uhrzeit FROM kurse WHERE freie_plaetze > 0 ORDER BY wochentag, uhrzeit'
    ).fetchall()
    conn.close()
    return kurse


def anmelden(name, email, kurs_id, datum):
    """Neue Anmeldung in die Tabelle schreiben."""
    conn = get_db()
    conn.execute(
        'INSERT INTO anmeldungen (name, email, kurs_id, datum) VALUES (?, ?, ?, ?)',
        (name, email, kurs_id, datum)
    )
    conn.commit()
    conn.close()


def mitglied_registrieren(vorname, nachname, email, telefon, datum):
    """Neues Mitglied speichern."""
    conn = get_db()
    conn.execute(
        'INSERT INTO mitglieder (vorname, nachname, email, telefon, datum) VALUES (?, ?, ?, ?, ?)',
        (vorname, nachname, email, telefon, datum)
    )
    conn.commit()
    conn.close()


def freie_plaetze_reduzieren(kurs_id):
    """Freie Plätze um 1 senken — Guard: nie unter 0."""
    conn = get_db()
    conn.execute(
        'UPDATE kurse SET freie_plaetze = freie_plaetze - 1 WHERE id = ? AND freie_plaetze > 0',
        (kurs_id,)
    )
    conn.commit()
    conn.close()
