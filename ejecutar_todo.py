"""Ejecuta los notebooks 00 a 05 en orden y guarda sus salidas.

Uso:  python ejecutar_todo.py
Requiere el CSV anonimizado en datos/huella_digital_anon.csv.
"""
import sys
from pathlib import Path
import nbformat
from nbclient import NotebookClient

RAIZ = Path(__file__).resolve().parent
NB = RAIZ / "notebooks"
CSV = RAIZ / "datos" / "huella_digital_anon.csv"

if not CSV.exists():
    sys.exit(f"Falta el archivo de datos: {CSV}\nCópialo ahí y vuelve a ejecutar.")

for ruta in sorted(NB.glob("0*.ipynb")):
    print(f"→ {ruta.name} ...", flush=True)
    nb = nbformat.read(ruta, as_version=4)
    NotebookClient(nb, timeout=900, kernel_name="python3", resources={"metadata": {"path": str(NB)}}).execute()
    nbformat.write(nb, ruta)
print(f"\nListo. Abre {RAIZ / 'dashboard' / 'index.html'} en el navegador.")
