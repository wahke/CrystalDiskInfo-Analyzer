import base64
import glob
import os
from dotenv import load_dotenv
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from openai import OpenAI

# === .env laden ===
load_dotenv()

# === API-Key aus Umgebungsvariable holen ===
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === Neuesten Screenshot automatisch erkennen ===
screenshot_files = sorted(glob.glob("CrystalDiskInfo_*.png"), key=os.path.getmtime, reverse=True)
if not screenshot_files:
    raise FileNotFoundError("❌ Kein Screenshot im Format 'CrystalDiskInfo_*.png' gefunden.")
image_path = screenshot_files[0]
print(f"✅ Verwende Screenshot: {image_path}")

# === Bild in base64 umwandeln ===
with open(image_path, "rb") as f:
    image_data = f.read()
    base64_image = base64.b64encode(image_data).decode("utf-8")

# === GPT-4o Vision: Techniker-Prompt ===
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Du bist ein technischer Diagnosetool-Experte für SSDs.\n\n"
                        "Analysiere diesen Screenshot von CrystalDiskInfo so detailliert wie möglich.\n"
                        "Bitte beantworte folgende Punkte:\n"
                        "1. Zustand der SSD (z. B. Gut, Vorsicht, Schlecht)\n"
                        "2. Gesundheitswert in Prozent\n"
                        "3. Temperatur + Einschätzung\n"
                        "4. Betriebsstunden und Einschaltzyklen (falls sichtbar)\n"
                        "5. Auffällige SMART-Werte (z. B. Reallocated Sectors, CRC Errors) mit Erklärung\n"
                        "6. Gesamteinschätzung und technische Empfehlung\n\n"
                        "Sprache: Deutsch. Ton: sachlich, wie ein Technikbericht."
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{base64_image}"}
                }
            ]
        }
    ],
    max_tokens=800,
)

# === GPT-Antwort extrahieren ===
gpt_text = response.choices[0].message.content.strip()

# === Berichtstext vorbereiten ===
bericht = f"""
Analysebericht (GPT-4o Vision – CrystalDiskInfo)

{gpt_text}

Hinweis:
Die Analyse wurde automatisch durch GPT-4o auf Basis eines Screenshots erstellt.
"""

# === PDF erzeugen ===
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_font("DejaVu", "", "DejaVuSans.ttf")  # Stelle sicher, dass .ttf vorhanden ist
pdf.set_font("DejaVu", "", 12)

# Seite 1: Analyse
pdf.add_page()
pdf.multi_cell(0, 10, bericht.strip())

# Seite 2: Screenshot
pdf.add_page()
pdf.cell(200, 10, text="CrystalDiskInfo Screenshot", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.image(image_path, x=10, y=25, w=180)

# Speichern
output_file = "CrystalDisk_Bericht_GPT4o.pdf"
pdf.output(output_file)
print(f"✅ PDF wurde erfolgreich erstellt: {output_file}")
