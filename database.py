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
                ('HIIT Burn',          'Hochintensives Intervalltraining für maximale Fettverbrennung.', 'Fortgeschritten', 'Montag',    '18:00', 45, 'Alex Petrov',    20, 8),
                ('Yoga Flow',          'Fließende Yoga-Sequenzen für Flexibilität und innere Ruhe.',    'Alle Level',      'Montag',    '10:00', 60, 'Lena Hartmann',  15, 5),
                ('Kraftzirkel',        'Ganzkörper-Krafttraining im Zirkel-Format.',                    'Mittel',          'Dienstag',  '17:00', 50, 'Alex Petrov',    18, 12),
                ('Kickbox Cardio',     'Boxtechnik trifft Ausdauer.',                                  'Alle Level',      'Dienstag',  '19:00', 60, 'Marco da Silva', 16, 3),
                ('Morning Stretch',    'Sanftes Dehnen zum Start in den Tag.',                          'Anfänger',        'Mittwoch',  '07:30', 30, 'Lena Hartmann',  12, 7),
                ('Power Lifting Basics','Kniebeugen, Kreuzheben, Bankdrücken.',                        'Anfänger',        'Mittwoch',  '18:00', 60, 'Alex Petrov',    10, 2),
                ('Yoga Deep',          'Tiefe Dehnungen und Regeneration.',                             'Alle Level',      'Donnerstag','10:00', 75, 'Lena Hartmann',  15, 10),
                ('Fight Fit',          'Intensives Kampfsport-Workout.',                                'Fortgeschritten', 'Donnerstag','19:00', 60, 'Marco da Silva', 16, 0),
                ('HIIT Express',       'Kompaktes HIIT in 30 Minuten.',                                'Mittel',          'Freitag',   '12:00', 30, 'Alex Petrov',    20, 14),
                ('Weekend Warrior',    'Samstags-Special: Mixed Workout.',                              'Alle Level',      'Samstag',   '10:00', 75, 'Marco da Silva', 20, 6),
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
