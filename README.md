# SuperGym Hamburg

> "Train Hard. Stay Sharp."

Webapplikation für ein fiktives Fitnessstudio in Hamburg.  
Entwickelt als Scrum-Teamprojekt im Rahmen der Umschulung zum  
Fachinformatiker für Anwendungsentwicklung @ BBQ Hamburg 2026.

---

## Tech Stack

- Python 3.13 / Flask
- Jinja2 Templates
- CSS (vanilla, keine Frameworks)
- JavaScript (vanilla)
- SQLite

---

## Corporate Identity

| Rolle | Farbe | Hex |
|---|---|---|
| Primary | Schwarz | `#0D0D0D` |
| Accent | Gelb | `#F5FF40` |
| Background | Dark | `#0D0D0D` |
| Text | Hellgrau | `#E0E0E0` |
| Subtil | Hellgrau | `#E0E0E0` |

Font: **Inter** – H1: 48px/900 · H2: 32px/700 · Body: 16px/400  
Design-Prinzipien: Weissraum · Klare eckige Kanten · Akzentfarbe nur für CTAs/Headlines/Logo

---

## 📁 Projektstruktur
```
supergym-website/
├── app.py                  # Flask App & Routen
├── database.py             # SQLite Datenbanklogik
├── requirements.txt        # Abhängigkeiten
├── .gitignore
├── README.md
├── templates/
│   ├── base.html           # Basis-Layout (Jinja2)
│   ├── index.html          # Startseite
│   ├── kurse.html          # Kursübersicht mit Filter
│   ├── kurs_detail.html    # Kursdetailseite
│   ├── about.html          # Über uns
│   ├── contact.html        # Kontaktformular
│   ├── impressum.html      # Impressum (§5 TMG)
│   ├── datenschutz.html    # Datenschutzerklärung (DSGVO)
│   └── agb.html            # Allgemeine Geschäftsbedingungen
└── static/
    ├── css/style.css
    ├── js/main.js
    └── images/
```

---

## Datenbankstruktur

### Tabelle `kurse`
| Feld | Typ | Beschreibung |
|---|---|---|
| id | INTEGER | Primary Key |
| name | TEXT | Kursname |
| beschreibung | TEXT | Kursbeschreibung |
| niveau | TEXT | Anfänger / Mittel / Fortgeschritten / Alle Level |
| wochentag | TEXT | Montag – Samstag |
| uhrzeit | TEXT | Uhrzeit des Kurses |
| dauer | INTEGER | Dauer in Minuten |
| trainer | TEXT | Trainername |
| kapazitaet | INTEGER | Max. Teilnehmerzahl |
| freie_plaetze | INTEGER | Aktuell verfügbare Plätze |

### Tabelle `anmeldungen`
| Feld | Typ | Beschreibung |
|---|---|---|
| id | INTEGER | Primary Key |
| name | TEXT | Name des Teilnehmers |
| email | TEXT | E-Mail des Teilnehmers |
| kurs_id | INTEGER | Foreign Key → kurse.id |
| datum | TEXT | Anmeldedatum |

### Tabelle `mitglieder`
| Feld | Typ | Beschreibung |
|---|---|---|
| id | INTEGER | Primary Key |
| vorname | TEXT | Vorname |
| nachname | TEXT | Nachname |
| email | TEXT | E-Mail |
| telefon | TEXT | Telefon (optional) |
| datum | TEXT | Registrierungsdatum |

---

## Installation & Start
```bash
# Repo klonen
git clone git@github.com:shinanDev/supergym-website.git
cd supergym-website

# Virtuelle Umgebung
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# App starten (DB wird automatisch initialisiert & befüllt)
flask run
```

→ App läuft auf: `http://127.0.0.1:5000`

---

## 📄 Seiten & Routen

| Route | Seite | Beschreibung |
|---|---|---|
| `/` | index.html | Startseite mit Hero, Karussell, Body |
| `/kurse` | kurse.html | Kursübersicht mit Wochentag-Filter |
| `/kurse/<id>` | kurs_detail.html | Kursdetails mit Anmelde-Modal |
| `/kurse/<id>/anmelden` | POST | Kursanmeldung in DB speichern |
| `/about` | about.html | Über uns, Trainer, Öffnungszeiten, Standort |
| `/contact` | contact.html | Kontaktformular |
| `/mitglied-werden` | POST | Mitgliedschaftsanmeldung |
| `/impressum` | impressum.html | Impressum |
| `/datenschutz` | datenschutz.html | Datenschutzerklärung |
| `/agb` | agb.html | Allgemeine Geschäftsbedingungen |

---

## 👥 Team & Aufgabenverteilung

| Name | Rolle | Features |
|---|---|---|
| Philipp | Dev / Git-Lead | Navigation, Body, Datenbanklogik, Kursübersicht, Standort & Karte, Datenschutz, AGB |
| Isabel | Developer | Karussell, Trainer-Vorstellung, Kursdetails |
| Vasilji | Developer | Footer, Gym-Geschichte, Logo, Anmeldeformular |
| Bousaina | Developer | Header, Öffnungszeiten, Impressum |

---

## Git Workflow
```bash
# Vor jedem Arbeitsbeginn
git checkout main
git pull origin main
git checkout -b feature/mein-feature

# Feature entwickeln & committen
git add .
git commit -m "feat: Beschreibung"
git push -u origin feature/mein-feature

# Pull Request auf GitHub → Review → Merge in main
```

**Branch-Konvention:**
- `feature/` – neue Features
- `fix/` – Bugfixes
- `docs/` – Dokumentation

---

## Scrum-Prozess

Entwickelt in **3 Sprints** nach Scrum-Methodik:

**Sprint 1** – Homepage & About-Seite
- Navigation, Header, Karussell, Body, Footer
- About-Seite: Gym-Geschichte, Öffnungszeiten, Trainer, Standort

**Sprint 2** – Legal & Fertigstellung Homepage
- Impressum, Datenschutz, AGB
- Grafisches Logo, Hantel-Icon, Kontaktformular

**Sprint 3** – Kursportal
- Kursübersicht mit DB-Anbindung
- Kursdetails, Anmeldeformular, Mitglieder-Modal
- Wochentag-Filter, Auslastungsanzeige

**Tools:** Jira · GitHub · Microsoft Teams · Claude Code

---

## 📌 Status

- [x] Projektstruktur & CI
- [x] Navigation & Layout
- [x] Homepage (Hero, Karussell, Body)
- [x] About-Seite
- [x] Legal-Seiten (Impressum, Datenschutz, AGB)
- [x] Datenbankanbindung (SQLite)
- [x] Kursportal mit Filter
- [x] Kursdetails
- [x] Anmeldeformular mit DB-Anbindung
- [x] Mitglieder-Anmeldung (Modal)
- [x] Responsives Design