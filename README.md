# Colombianos Detenidos en el Exterior

Este proyecto presenta un dashboard interactivo que analiza la información de los detenidos en el exterior, haciendo una comparativa entre Chile y Estados Unidos. El objetivo es evidenciar, a través de visualizaciones y filtros interactivos, las diferencias en la cantidad promedio de detenidos entre ambos países y brindar una herramienta que facilite el entendimiento de esta problemática.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

ColombianosDetenidosDashboard/
├── src/          # Contiene el código fuente (app.py)
├── data/         # Contiene la base de datos (colombianos detenidos exterior.csv)
├── docs/         # Documentos adicionales (informes previos, y final)
├── requirements.txt   # Lista de dependencias
├── README.md     # Este archivo de documentación
└── Enlaces.txt   # Enlaces al repositorio y a Binder


## Instrucciones para Ejecutar el Dashboard

1. **Instalar Dependencias:**  
   Abre una terminal en la carpeta raíz del proyecto y ejecuta:
pip install -r requirements.txt


2. **Ejecutar el Dashboard:**  
Desde la misma terminal, ejecuta:
python src/app.py

Esto iniciará el servidor de Dash.

3. **Abrir el Navegador:**  
Dirígete a [http://127.0.0.1:8050/](http://127.0.0.1:8050/) para ver el dashboard.

## Descripción y Funcionalidades

- **Dashboard Interactivo:** Permite filtrar la información por país (Todos, Chile, Estados Unidos) mediante un menú desplegable. Al seleccionar una opción, se actualiza un gráfico de barras que muestra la cantidad promedio de detenidos, junto con métricas adicionales en el tooltip.
- **Visualizaciones y Narrativa:** El dashboard incluye secciones de texto (Introducción, Hallazgos, Conclusiones) que explican la problemática, resaltan hallazgos clave y sugieren próximos pasos para profundizar en el análisis.
- **Estilo y Diseño:** Se utiliza un fondo azul bebé, la fuente "Times New Roman" para un aspecto elegante y una estructura organizada que facilita la interacción y lectura.

## Consideraciones y Próximos Pasos

Los análisis indican diferencias significativas en la forma en que se registran los detenidos en Chile y en Estados Unidos. Este dashboard es un punto de partida y podría complementarse con:
- Variables adicionales (tipo de delito, fecha de detención, género, etc.)
- Técnicas avanzadas de modelado predictivo y limpieza de datos.

## Enlaces Adicionales

Para facilitar la revisión del proyecto, se incluyen los siguientes enlaces (ver el archivo `Enlaces.txt` para más detalles):

- **Repositorio en GitHub:** https://github.com/Sjrios29/ColombianosDetenidosDashboard
- **Visualización en Binder:** https://mybinder.org/v2/gh/Sjrios29/ColombianosDetenidosDashboard/main?urlpath=src/app.py

