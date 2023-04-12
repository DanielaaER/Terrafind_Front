
#Este mapa muestra todosss los municipios JSKAS
import pandas as pd

# Cargar datos del CSV
municipios_csv = "municipios.csv"
municipios = pd.read_csv(municipios_csv)

# Crear mapa centrado en México
mexico_map = folium.Map(location=[23.626672, -102.537292], zoom_start=5)

# Agregar marcadores de cada municipio al mapa
for index, row in municipios.iterrows():
    lat = row['LAT_DEC']
    lon = row['LON_DEC']
    nombre = row['NOM_MUN']
    estado = row['NOM_ENT']
    tooltip = f"{nombre}, {estado}"
    marker = folium.Marker(location=[lat, lon], tooltip=tooltip)
    marker.add_to(mexico_map)

# Mostrar mapa
mexico_map

import ipywidgets as widgets

# Crear una lista desplegable para seleccionar el municipio de origen
origen_dropdown = widgets.Dropdown(
    options=municipios['NOM_MUN'].tolist(),
    description='Origen:',
)

# Crear una lista desplegable para seleccionar el municipio de destino
destino_dropdown = widgets.Dropdown(
    options=municipios['NOM_MUN'].tolist(),
    description='Destino:',
)

# Mostrar las listas desplegables
widgets.VBox([origen_dropdown, destino_dropdown])

mexico_map.save('map.html')