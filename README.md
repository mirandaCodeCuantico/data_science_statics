# Huella Digital: estadística y ciencia de datos

Proyecto de clase que analiza registros reales anonimizados de una empresa de telefonía móvil en Colombia
(enero a octubre de 2026). Tiene dos partes:

- **Estadística** sobre una sola variable, el cargo fijo mensual (VAL_CFM): datos agrupados (Sturges,
  tabla de frecuencias, media, mediana, moda, cuartiles, varianza, desviación estándar, coeficiente de
  variación), mínimos cuadrados y correlación con la antigüedad, técnicas de conteo y probabilidad
  (incluida la hipergeométrica). Cada indicador se valida a mano frente a la biblioteca (sección 6.4).
- **Ciencia de datos** alineada con esas preguntas: calidad de datos, meses en que la huella se midió,
  segmentación en dos etapas y un árbol de decisión cuyas reglas son probabilidades condicionales.

Todo corre en local con pandas, NumPy, SciPy y scikit-learn. No usa Spark ni Databricks.

## Estructura

```
huella_digital_estadistica/
├── datos/                      ← aquí va el CSV; los notebooks crean aquí base_limpia_elegibles.csv y muestra_30.csv
├── capturas/                   imágenes de respaldo del dashboard
├── notebooks/
│   ├── config.py               rutas, constantes y utilidades
│   ├── catalogo.py             familias de banderas y exclusiones
│   ├── 00_preparacion.ipynb    limpieza, enmascarado, elegibilidad, bitácora (6.1)
│   ├── 01_estadistica_descriptiva.ipynb
│   ├── 02_regresion_correlacion.ipynb
│   ├── 03_conteo_probabilidad.ipynb
│   ├── 04_ciencia_datos.ipynb      incluye prueba 70/30 con exactitud y F1
│   ├── 05_export_dashboard.ipynb   exporta agregados y construye el dashboard
│   └── 06_muestra_30.ipynb         muestra de 30 registros para el ejercicio a mano
├── dashboard/
│   ├── index.src.html          plantilla del dashboard
│   ├── build.py                incrusta los datos en la plantilla
│   ├── data/dashboard_data.json
│   └── index.html              dashboard listo para abrir
├── ejecutar_todo.py
└── requirements.txt
```

## Cómo ejecutarlo

1. Copia el CSV anonimizado en `datos/huella_digital_anon.csv`.
2. Instala las dependencias (Python 3.10 o superior):
   ```
   pip install -r requirements.txt
   ```
3. Ejecuta todos los notebooks en orden:
   ```
   python ejecutar_todo.py
   ```
   También puedes abrirlos en Jupyter y correrlos uno por uno, del 00 al 05.
4. Abre `dashboard/index.html` en el navegador. Tiene un filtro por mes en la sección de datos agrupados
   que recalcula la tabla de frecuencias, las medidas y las proporciones. Los datos van incrustados, así que funciona sin servidor.
   Necesita internet solo para cargar Plotly y las fuentes.

## Población de estudio

- 9.000 registros recibidos (1.000 por mes, 9 meses; no hay septiembre).
- 5.230 elegibles: personas naturales (sin NIT) con edad válida entre 18 y 100 años.
- La unidad de análisis es el registro de línea, no el cliente.

## Privacidad

- La marca de la empresa se enmascara («Operador») y se retiran cuatro banderas sensibles
  (salud, droguería, citas y contenido para adultos), según la Ley 1581 de 2012.
- El dashboard y el JSON contienen solo resultados agregados. No publiques el CSV ni los Parquet de `datos/`.
- Para usar los resultados fuera de la clase se necesita la autorización del dueño de los datos.

## Limitaciones principales

- Las banderas de huella digital no se calcularon en julio, agosto ni octubre; las proporciones de toda
  la muestra son un límite inferior (ver la parte de ciencia de datos).
- La muestra no es aleatoria: los resultados describen estos registros y no se generalizan a toda la base.
- Las banderas indican navegación o interés, no transacciones; ningún resultado demuestra causalidad.
