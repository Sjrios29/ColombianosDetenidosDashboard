import os
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# --- DIAGNÓSTICO DE RUTA Y ARCHIVOS ---
# Este bloque imprime el directorio de trabajo y los archivos que encuentra en ../data/
print("Directorio de trabajo actual:", os.getcwd())
try:
    archivos_data = os.listdir('../data')
    print("Archivos en ../data/:", archivos_data)
except Exception as e:
    print("Error al listar ../data/:", e)

# --- LECTURA DEL CSV ---
ruta = r'../data/colombianos detenidos exterior.csv'
df = pd.read_csv(ruta, sep=';', encoding='utf-8', on_bad_lines='skip', low_memory=False)

# Estandariza la columna para evitar problemas de espacios y mayúsculas
df["PAIS PRISIÓN"] = df["PAIS PRISIÓN"].str.strip().str.upper()
paises_interes = ["CHILE", "ESTADOS UNIDOS"]

# --- CONFIGURACIÓN DE LA APP ---
app = dash.Dash(__name__)

app.layout = html.Div([
    # Título y subtítulo centrados
    html.H1("Colombianos detenidos en el exterior", style={
        'textAlign': 'center', 
        'color': '#2C3E50',
        'fontFamily': '"Times New Roman", Times, serif'
    }),
    html.H3("Análisis Comparativo: Chile vs. Estados Unidos", style={
        'textAlign': 'center', 
        'color': '#34495E',
        'fontFamily': '"Times New Roman", Times, serif'
    }),

    # Sección de Introducción / Contexto
    html.Div([
        html.H4("Introducción", style={'color': '#2C3E50', 'fontFamily': '"Times New Roman", Times, serif'}),
        html.P(
            "Este tablero presenta un análisis de los detenidos en el exterior, "
            "centrándose en la comparación entre Chile y Estados Unidos. "
            "El objetivo es mostrar la cantidad promedio de detenidos en cada país, "
            "así como brindar una herramienta interactiva para filtrar y explorar los datos.",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        )
    ], style={'margin': '20px', 'padding': '10px', 'backgroundColor': '#ECF0F1', 'borderRadius': '8px'}),

    # Dropdown y gráfico interactivo
    html.Div([
        html.Label("Selecciona el país a visualizar:", style={
            'fontWeight': 'bold', 
            'fontFamily': '"Times New Roman", Times, serif'
        }),
        dcc.Dropdown(
            id='dropdown-pais',
            options=[
                {'label': 'Todos', 'value': 'TODOS'},
                {'label': 'Chile', 'value': 'CHILE'},
                {'label': 'Estados Unidos', 'value': 'ESTADOS UNIDOS'}
            ],
            value='TODOS',
            clearable=False,
            style={'width': '100%'}
        ),
        dcc.Graph(id='grafico-comparativa')
    ], style={
        'width': '70%', 
        'margin': 'auto', 
        'padding': '20px', 
        'backgroundColor': '#FFFFFF', 
        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 
        'borderRadius': '8px'
    }),

    # Sección de Hallazgos Clave
    html.Div([
        html.H4("Hallazgos Clave", style={'color': '#2C3E50', 'fontFamily': '"Times New Roman", Times, serif'}),
        html.P(
            "• Se observa que la cantidad promedio de detenidos difiere entre Chile y Estados Unidos. "
            "Esto podría reflejar diferencias en políticas, controles migratorios o tipos de delitos reportados.",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        ),
        html.P(
            "• El filtro interactivo permite ver cada país por separado o compararlos en conjunto, "
            "ofreciendo una visión más detallada de la situación.",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        )
    ], style={
        'margin': '20px', 
        'padding': '15px', 
        'backgroundColor': '#FDFEFE', 
        'borderLeft': '5px solid #2980B9', 
        'borderRadius': '8px'
    }),

    # Sección de Conclusiones y Hallazgos
    html.Div([
        html.H4("Conclusiones y Hallazgos", style={'color': '#2C3E50', 'fontFamily': '"Times New Roman", Times, serif'}),
        html.P(
            "A partir del análisis realizado en el dashboard, se pudo evidenciar que existen diferencias notables en la cantidad promedio de detenidos entre Chile y Estados Unidos. En concreto, al filtrar los datos y calcular el promedio, se observó que:",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        ),
        html.P(
            "• En Estados Unidos se registra un mayor promedio de detenidos en comparación con Chile. Este hallazgo podría estar relacionado con diferencias en las políticas de detención, protocolos de registro o en la naturaleza de los delitos reportados.",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        ),
        html.P(
            "• La herramienta interactiva del dashboard me permitió visualizar dinámicamente estos resultados, facilitando la identificación de tendencias y diferencias entre ambos países de forma intuitiva.",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        ),
        html.P(
            "• La agregación de métricas adicionales (como el total de detenidos y el número de casos) ofrece un panorama más completo del contexto, sugiriendo que no solo es relevante la media, sino también la dispersión y el volumen total de los registros.",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        ),
        html.P(
            "En conclusión, este análisis me ha permitido comprender que existen diferencias significativas en la forma en que se registran los detenidos en Chile y en Estados Unidos, lo que abre la puerta a investigaciones futuras que profundicen en los factores determinantes y optimicen los modelos predictivos para una toma de decisiones más informada.",
            style={'fontSize': '16px', 'lineHeight': '1.5', 'fontFamily': '"Times New Roman", Times, serif'}
        )
    ], style={'margin': '20px', 'padding': '15px', 'backgroundColor': '#ECF0F1', 'borderRadius': '8px'})
    
], style={
    'maxWidth': '1200px', 
    'margin': 'auto', 
    'fontFamily': '"Times New Roman", Times, serif', 
    'backgroundColor': '#BFEFFF', 
    'padding': '20px'
})

# --- CALLBACK PARA ACTUALIZAR EL GRÁFICO ---
@app.callback(
    Output('grafico-comparativa', 'figure'),
    Input('dropdown-pais', 'value')
)
def actualizar_grafico(pais_seleccionado):
    if pais_seleccionado == 'TODOS':
        df_filtrado = df[df["PAIS PRISIÓN"].isin(paises_interes)]
    else:
        df_filtrado = df[df["PAIS PRISIÓN"] == pais_seleccionado]

    df_grouped = df_filtrado.groupby("PAIS PRISIÓN").agg(
        CANTIDAD_PROMEDIO=('CANTIDAD', 'mean'),
        CANTIDAD_TOTAL=('CANTIDAD', 'sum'),
        CASOS=('CANTIDAD', 'count')
    ).reset_index()

    fig_bar = px.bar(
        df_grouped,
        x="PAIS PRISIÓN",
        y="CANTIDAD_PROMEDIO",
        title="Cantidad promedio de detenidos",
        hover_data={
            "CANTIDAD_PROMEDIO": ':.2f',
            "CANTIDAD_TOTAL": True,
            "CASOS": True
        }
    )
    return fig_bar

# --- EJECUCIÓN DE LA APP ---
if __name__ == '__main__':
    app.run(debug=True)
