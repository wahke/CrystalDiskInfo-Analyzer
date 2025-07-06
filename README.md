# 🧠 CrystalDiskInfo Analyzer mit GPT-4o (Vision)

Dieses Python-Projekt analysiert automatisch einen Screenshot von **CrystalDiskInfo** mithilfe von **GPT-4o Vision (OpenAI)** und erstellt einen professionellen **PDF-Bericht**, der den SSD-Zustand, Temperatur, Gesundheitswert und relevante SMART-Werte beschreibt.

---

## ✅ Funktionen

- Erkennt automatisch den neuesten Screenshot (`CrystalDiskInfo_*.png`)
- Sendet das Bild an GPT-4o (Vision-Modell von OpenAI)
- Erstellt einen PDF-Bericht mit:
  - GPT-Analyse auf Deutsch
  - Original-Screenshot (Seite 2)
- Unicode-Unterstützung (Umlaute etc.) durch DejaVu-Schrift

---

## 🧰 Voraussetzungen

- Python 3.8 oder höher
- OpenAI API-Key mit Zugriff auf GPT-4o (Vision)
- Internetverbindung
- Screenshot von CrystalDiskInfo als `.png`

---

## 🔧 Installation Schritt für Schritt

### 1. Projekt herunterladen

```bash
git clone https://github.com/dein-benutzername/crystaldiskinfo-analyzer.git
cd crystaldiskinfo-analyzer
```


### 2. Abhängigkeiten installieren
Installiere die benötigten Python-Bibliotheken direkt mit:

```bash
pip install openai python-dotenv fpdf2 Pillow
```
Oder verwende die requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. OpenAI API-Key einrichten
Erstelle eine Datei namens .env im Projektordner.

Trage dort deinen API-Key wie folgt ein:

```env

OPENAI_API_KEY=sk-...dein-api-key...
 Wichtig: Lade diese Datei niemals öffentlich hoch.
Nutze stattdessen die Datei .env.example als Vorlage.
```
### 4. Schriftart (DejaVu) hinzufügen
Für Umlaute und Sonderzeichen wird eine Unicode-fähige Schrift benötigt:

Lade DejaVuSans.ttf herunter:
 https://dejavu-fonts.github.io/Download.html

Lege sie in denselben Ordner wie das Skript crystaldisk_report.py

### 5. Screenshot vorbereiten
Speichere einen Screenshot von CrystalDiskInfo als .png

Der Dateiname sollte mit CrystalDiskInfo_ beginnen, z. B.:

text
CrystalDiskInfo_20250706_104422.png
Lege die Datei in denselben Ordner wie das Skript

### 6. Skript ausführen
```bash
python crystaldisk_report.py
```
 Danach wird automatisch eine PDF erstellt:

text
CrystalDisk_Bericht_GPT4o.pdf

 Projektstruktur
text

├── crystaldisk_report.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── DejaVuSans.ttf
├── CrystalDiskInfo_*.png  # Screenshot-Datei
 
Inhalt der requirements.txt
text

openai>=1.3.0
python-dotenv
fpdf2>=2.7.6
Pillow
