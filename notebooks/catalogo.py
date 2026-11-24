"""Catálogo de campos del diccionario (versión anonimizada TelcoX).

Centraliza qué es cada bandera, a qué familia pertenece y qué reglas de uso aplica,
para que todos los notebooks usen la misma clasificación.
"""

# 92 banderas agrupadas en 10 familias temáticas (sección "Radiografía" del documento)
FAMILIAS = {
    "retail": ["COMPRASYMODA", "MODA", "MARKETPLACES", "GRANDES_SUPERFICIES", "SUPERMERCADOS",
               "DOMICILIOS", "COMIDAYBEBIDA", "GASTROBAR", "COSMETICOS", "CONSTRUCCION",
               "ELECTRODOMESTICOS", "CELULARES", "TURISMO", "APPS_TRANSPORTE"],
    "ecosistema": ["TELCOX_MUSICA", "TELCOX_VIDEO", "TELCOX1", "TELCOX2", "TELCOX3", "TELCOX4",
                   "TELCOX5", "TELCOXAPPCONT", "CLIENTE_HOGAR", "COD_ORION",
                   "PLANTELCOX_MUSICA", "PLANTELCOX_VIDEO", "RCS"],
    "entretenimiento": ["ENTRETENIMIENTO", "CINE", "CONCIERTOS", "MUSICA", "VIDEO", "DEPORTES",
                        "FUTBOL", "GAMERS", "HOBBIES", "NOTICIAS", "REDES_SOCIALES", "MENSAJERIA",
                        "COMUNICACIONES"],
    "control": ["SUPRESION_I", "SUPRESION_T", "BLOQUEO_CONTENIDO", "MORA_CARTERA", "COMPETENCIA",
                "REPOSICION180D", "TECNOLOGIA180D", "EDAD", "GENERO", "GEOLOCALIZACION"],
    "estilo_vida": ["CLASE_ALTA", "CLASE_MEDIA", "FAMILIA", "PADRES_BEBES", "MASCOTAS", "HOGAR",
                    "FINCA_RAIZ", "AUTOMOTOR", "MOTOCICLETAS"],
    "trabajo": ["EMPLEO", "EMPLEADORES", "EMPRENDEDORES", "EMPRENDEDORES_EMP", "NEGOCIOS",
                "EDUCACION_CONTINUADA", "EDUCACION_IDIOMAS", "EDUCACION_MEDIA", "EDUCACION_SUPERIOR"],
    "finanzas": ["BANCA", "BILLETERA", "PAGOS_ONLINE", "FINANZAS", "FINANZAS_PERS", "GIROS",
                 "SEGUROS", "CAJAS_COMPENSACION"],
    "tecnologia": ["TECNOLOGIA", "TEC_AUDIO", "TEC_CAMARAS", "TEC_CELULARES", "TEC_COMPUTADORES",
                   "TEC_ELECTRODOMESTICOS", "TEC_IOT", "TEC_TV"],
    "salud": ["SALUD", "SALUD_FITNESS", "DROGUERIA", "DEPORTISTAS"],
    "sensibles": ["APPS_CITAS", "APUESTAS", "BEBIDAS_ALCOHOLICAS", "VIDEOXXX"],
}

NOMBRE_FAMILIA = {
    "retail": "Consumo y retail", "ecosistema": "Ecosistema TelcoX",
    "entretenimiento": "Entretenimiento y medios", "control": "Control, riesgo y ciclo",
    "estilo_vida": "Estilo de vida y hogar", "trabajo": "Trabajo y educación",
    "finanzas": "Finanzas y pagos", "tecnologia": "Tecnología", "salud": "Salud y bienestar",
    "sensibles": "Sensibles",
}

BANDERAS = [b for fam in FAMILIAS.values() for b in fam]
COL = lambda b: f"BAN_{b}"  # noqa: E731  nombre de columna en la vista

# Reglas de uso (sección "Privacidad y uso responsable")
EXCLUIR = ["SALUD", "DROGUERIA", "APPS_CITAS", "VIDEOXXX"]               # nunca se usan
NO_FOCALIZAR = ["APUESTAS", "BEBIDAS_ALCOHOLICAS", "EMPLEO", "MORA_CARTERA"]  # solo filtros/agregados
OPACAS = ["TELCOX1", "TELCOX2", "TELCOX3", "TELCOX4", "TELCOX5"]           # sin definición pública
SUPRESION = ["SUPRESION_I", "SUPRESION_T"]                                  # filtro duro de activación

# Familias que entran a la segmentación por intereses
FAMILIAS_INTERES = ["retail", "entretenimiento", "estilo_vida", "trabajo", "finanzas",
                    "tecnologia", "salud"]

# Municipios del ejemplo: (municipio, departamento, región comercial, abreviatura, lat, lon, peso)
MUNICIPIOS = [
    ("Bogotá", "Bogotá D.C.", "Centro", "BOG", 4.711, -74.072, 0.24),
    ("Medellín", "Antioquia", "Noroccidente", "MED", 6.244, -75.581, 0.12),
    ("Cali", "Valle del Cauca", "Suroccidente", "CLO", 3.452, -76.532, 0.09),
    ("Barranquilla", "Atlántico", "Costa", "BAQ", 10.964, -74.796, 0.07),
    ("Cartagena", "Bolívar", "Costa", "CTG", 10.391, -75.479, 0.045),
    ("Bucaramanga", "Santander", "Oriente", "BGA", 7.119, -73.122, 0.04),
    ("Cúcuta", "Norte de Santander", "Oriente", "CUC", 7.894, -72.507, 0.035),
    ("Pereira", "Risaralda", "Noroccidente", "PEI", 4.813, -75.696, 0.03),
    ("Manizales", "Caldas", "Noroccidente", "MZL", 5.070, -75.513, 0.02),
    ("Santa Marta", "Magdalena", "Costa", "SMR", 11.240, -74.199, 0.03),
    ("Ibagué", "Tolima", "Centro", "IBE", 4.438, -75.232, 0.025),
    ("Villavicencio", "Meta", "Oriente", "VVC", 4.142, -73.626, 0.03),
    ("Pasto", "Nariño", "Suroccidente", "PSO", 1.214, -77.281, 0.025),
    ("Popayán", "Cauca", "Suroccidente", "PPN", 2.444, -76.614, 0.02),
    ("Montería", "Córdoba", "Costa", "MTR", 8.748, -75.881, 0.03),
    ("Neiva", "Huila", "Suroccidente", "NVA", 2.927, -75.282, 0.025),
    ("Valledupar", "Cesar", "Costa", "VUP", 10.463, -73.253, 0.025),
    ("Armenia", "Quindío", "Noroccidente", "AXM", 4.534, -75.681, 0.02),
]
CIUDADES_5G = ["Bogotá", "Medellín", "Cali", "Barranquilla"]  # cobertura 5G del ejemplo

ESTRATOS = ["Bajo-bajo", "Bajo", "Medio-bajo", "Medio", "Medio-alto", "Alto"]
