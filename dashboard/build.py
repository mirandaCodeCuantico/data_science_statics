"""Incrusta data/dashboard_data.json dentro de index.html (página autocontenida)."""
import json, os, re
aqui = os.path.dirname(os.path.abspath(__file__))
datos = json.load(open(os.path.join(aqui, "data", "dashboard_data.json"), encoding="utf-8"))
texto = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = open(os.path.join(aqui, "index.src.html"), encoding="utf-8").read()
bloque = f'<script id="datos" type="application/json">{texto}</script>\n'
html = html.replace('<script src="https://cdn.plot.ly', bloque + '<script src="https://cdn.plot.ly', 1)
open(os.path.join(aqui, "index.html"), "w", encoding="utf-8").write(html)
print(f"index.html: {os.path.getsize(os.path.join(aqui, 'index.html')) / 1024:.0f} KB")
