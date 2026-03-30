# 🏋️ SuperGym Hamburg

> "Train Hard. Stay Sharp."

Webapplikation für ein fiktives Fitnessstudio in Hamburg.  
Entwickelt als Scrum-Teamprojekt im Rahmen der Umschulung zum  
Fachinformatiker für Anwendungsentwicklung @ BBQ Hamburg 2026.

---

## 🛠️ Tech Stack

- Python 3.13 / Flask
- Jinja2 Templates
- CSS (vanilla, keine Frameworks)
- JavaScript (vanilla)
- SQLite

---

## 🎨 Corporate Identity

| Rolle | Farbe | Hex |
|---|---|---|
| Primary | Schwarz | `#0D0D0D` |
| Accent | Gelb | `#F5FF40` |
| Background | Off-White | `#F7F7F7` |
| Text | Dunkelgrau | `#1A1A1A` |
| Subtil | Hellgrau | `#E0E0E0` |

Font: **Inter** – H1: 48px/900 · H2: 32px/700 · Body: 16px/400

---

## 📁 Projektstruktur
```
supergym-website/
├── app.py              # Flask App & Routen
├── database.py         # SQLite Datenbanklogik
├── requirements.txt    # Abhängigkeiten
├── .gitignore
├── README.md
├── templates/
│   ├── base.html       # Basis-Layout (Jinja2)
│   ├── index.html      # Startseite
│   ├── kurse.html      # Kursübersicht
│   ├── kurs_detail.html
│   └── about.html
└── static/
    ├── css/style.css
    ├── js/main.js
    └── images/
```

---

## 🚀 Installation & Start
```bash
# Repo klonen
git clone git@github.com:shinanDev/supergym-website.git
cd supergym-website

# Virtuelle Umgebung
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# Datenbank initialisieren
python database.py

# App starten
flask run
```

→ App läuft auf: `http://127.0.0.1:5000`

---

## 👥 Team & Aufgabenverteilung

| Name | Feature | Branch |
|---|---|---|
| Philipp | Navigation + Body | `feature/nav-body` |
| Isabel | Karussell | `feature/karussell` |
| Vasilji | Footer | `feature/footer` |
| Bousaina | Header | `feature/header` |

---

## 🔀 Git Workflow
```bash
# Vor jedem Arbeitsbeginn
git pull origin main

# Feature entwickeln
git add .
git commit -m "feat: Beschreibung"
git push origin feature/dein-branch
```

→ Fertig? Pull Request auf GitHub öffnen · Philipp reviewed · Merge in `main`

---

## 📌 Status

- [x] Projektstruktur
- [x] Corporate Identity / CSS-Variablen
- [x] Navigation + Body
- [ ] Header
- [ ] Karussell
- [ ] Footer