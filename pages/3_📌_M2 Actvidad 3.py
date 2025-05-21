import streamlit as st
import numpy as np
from faker import Faker
import random
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")




st.header("Actividad # 1: Practica de filtrado en Pandas (Google Colab)")
st.subheader("Solución: ")

st.markdown('[Abrir cuaderno de Google Colab](https://colab.research.google.com/drive/1EV14Eqbf4VS3c2hjkgIk7iejqwIiQGVA?usp=sharing)')


st.header("Actividad # 2: Desarrollar una aplicación de filtros dinámicos en Streamlit.")
st.subheader("Solución: ")


#DATAFRAME
# Configurar Faker para Colombia
fake = Faker('es_CO')

# Establecer semilla para reproducibilidad
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# Crear datos
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

# Crear DataFrame
df_nuevo = pd.DataFrame(data)

# Introducir algunos valores nulos
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan

# Convertir fecha_nacimiento a datetime
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])



st.subheader("Filtros dinámicos en Streamlit con el Dataframe.")
st.subheader("")

#Filtro #1 between
st.subheader("Filtro #1: Filtrar por edad")
filtro_edad = st.checkbox("Filtrar por determinado rango de edad: ")
if filtro_edad:
    min_value, max_value = st.slider(
        "Rango de edad específico: ",
        min_value = 15,
        max_value = 75,
        value = (15, 75),
    )
    df_nuevo = df_nuevo[df_nuevo['edad'].between(min_value, max_value)] 

st.subheader("Dataframe filtrado por edad: ")
st.dataframe(df_nuevo)


#Filtro #2 isin
st.subheader("Filtro #2: Filtrar por municipio")
filtro_municipio = st.checkbox("Filtrar por municipio: ")
if filtro_municipio:
    municipios = [
        'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja',
        'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal',
        'Leticia', 'Puerto Inírida'
    ]
    municipios_elegidos = st.multiselect(
        "Municipios disponibles: ", municipios
    )
    if municipios_elegidos:
        df_nuevo = df_nuevo[df_nuevo['municipio'].isin(municipios_elegidos)]



#Filtro #3 operador >
st.subheader("Filtro #3: Filtrar con operador >")
filtro_ingreso_mensual_minimo = st.checkbox("Filtrar por ingreso mensual mínimo: ")
if filtro_ingreso_mensual_minimo:
    ingreso_mensual_rango = st.slider(  
        "Ingreso mínimo mensual específico:",
        min_value=800000,
        max_value=12000000,
        value=(800000, 12000000), 
        step=100000
    )
    ingreso_minimo_seleccionado = ingreso_mensual_rango[0]  
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'] > ingreso_minimo_seleccionado]