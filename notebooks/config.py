"""Configuración del proyecto: análisis estadístico + ciencia de datos sobre la Huella Digital (datos reales anonimizados).

La empresa se identifica solo como "una empresa de telefonía móvil" (TelcoX en el código).
El CSV original va en datos/huella_digital_anon.csv y NO se publica: solo salen agregados.
"""
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "datos"
CSV = DATOS / "huella_digital_anon.csv"
DASHBOARD = RAIZ / "dashboard"
EXPORT = DASHBOARD / "data"
SEED = 2026                      # semilla de todo lo aleatorio (reproducible)

# Población del documento (sección 5.2.1)
FECHA_INICIO, FECHA_FIN = "2026-01", "2026-10"
EDAD_MIN, EDAD_MAX = 18, 100     # rango fijado después de verificar los valores válidos (6.1)
META_POR_MES = 10_000            # meta planificada en el documento
VARIABLES = ["ANTIGUEDAD_MESES", "VAL_CFM", "BAN_BANCA", "BAN_BILLETERA", "BAN_PAGOS_ONLINE", "BAN_SUPRESION_I"]

MESES = {"2026-01": "Enero", "2026-02": "Febrero", "2026-03": "Marzo", "2026-04": "Abril", "2026-05": "Mayo",
         "2026-06": "Junio", "2026-07": "Julio", "2026-08": "Agosto", "2026-09": "Septiembre", "2026-10": "Octubre"}


def guardar(df: pd.DataFrame, nombre: str) -> pd.DataFrame:
    DATOS.mkdir(parents=True, exist_ok=True)
    df.to_parquet(DATOS / f"{nombre}.parquet", index=False)
    return df


def leer(nombre: str) -> pd.DataFrame:
    return pd.read_parquet(DATOS / f"{nombre}.parquet")


def guardar_json(obj, nombre: str):
    """Resultados intermedios para el dashboard y el informe (solo agregados)."""
    import json, math
    import numpy as np

    def limpiar(x):
        if isinstance(x, dict):
            return {str(k): limpiar(v) for k, v in x.items()}
        if isinstance(x, (list, tuple)):
            return [limpiar(v) for v in x]
        if isinstance(x, (np.integer,)):
            return int(x)
        if isinstance(x, (np.floating, float)):
            return None if (math.isnan(x) or math.isinf(x)) else float(x)
        if isinstance(x, np.bool_):
            return bool(x)
        if x is pd.NA:
            return None
        return x
    DATOS.mkdir(parents=True, exist_ok=True)
    (DATOS / f"{nombre}.json").write_text(json.dumps(limpiar(obj), ensure_ascii=False, allow_nan=False), encoding="utf-8")


def leer_json(nombre: str):
    import json
    return json.loads((DATOS / f"{nombre}.json").read_text(encoding="utf-8"))
