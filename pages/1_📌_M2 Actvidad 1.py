import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
import json
from pymongo import MongoClient



st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Actividad #1 - Creación de DataFrames")
st.markdown("""
En esta actividad mostraré los 12 DataFrames desde diferentes fuentes.
""")


st.header("Solución")



libros = {
    "Título del libro": ["El Principito", "Don Quijote de la Mancha", "Cien años de soledad", "Los Juegos del Hambre"],
    "Autor": ["Antoine de Saint-Exupéry", "Miguel de Cervantes", "Gabriel García Márquez", "Suzanne Collins"],
    "Año de publicación": [1943, 1605, 1967, 2008],
    "Género": ["Fábula, Fantasía", "Novela", "Realismo mágico", "Ciencia ficción"],
}

dataframe_libros = pd.DataFrame(libros)

st.subheader("DataFrame de libros - diccionario:")
st.dataframe(dataframe_libros)







ciudades =[
    {"Nombre": "Medellín", "Población": 58964852, "País": "Colombia"},
    {"Nombre": "Madrid", "Población": 6589745, "País": "España"},
    {"Nombre": "Seul", "Población": 35621000, "País": "Corea del Sur"},
]

dataframe_ciudades = pd.DataFrame(ciudades)

st.subheader("DataFrame de ciudades - lista de diccionarios:")
st.dataframe(dataframe_ciudades)









inventario = [
    ["Pepino", 1500, 5],
    ["Tomate", 2000, 4],
    ["Uvas", 3450, 6],
    ["Cebolla", 3200, 1]
]

columnas = ["Producto", "Precio x Kilo", "Canastas disponibles del producto"]

dataframe_inventario = pd.DataFrame(inventario, columns=columnas)

st.subheader("DataFrame de inventario - lista de listas:")
st.markdown("Productos en Inventario: ")
st.dataframe(dataframe_inventario)













nombre = pd.Series(["Carla", "Marcos", "Leonor", "Esteban"])
edad = pd.Series([15, 20, 48, 3])
ciudad = pd.Series(["Ibagué", "Medellín", "Cúcuta", "Pereira" ])

datos_serie = {
    "Nombre": nombre,
    "Edad": edad,
    "Ciudad": ciudad
}
st.subheader("DataFrame de personas - Serie:")
st.markdown("Datos de Personas: ")
dataframe_personas = pd.DataFrame(datos_serie)
st.dataframe(dataframe_personas)



st.subheader("DataFrame de CSV: ")
archivo_csv = 'data.csv'
dataframe_csv = pd.read_csv(archivo_csv)
st.dataframe(dataframe_csv)


st.subheader("DataFrame de Excel: ")
archivo_excel = 'data.xlsx.xlsx'
dataframe_excel = pd.read_excel(archivo_excel)
st.dataframe(dataframe_excel)


st.subheader("DataFrame de Json:")
archivo_json = 'data.json'
dataframe_json = pd.read_json(archivo_json)
st.dataframe(dataframe_json)



st.subheader("DataFrame con URL:")
url = "https://datos.canarias.es/catalogos/estadisticas/dataset/44dc4231-b23c-464d-a0b3-709c55ff4571/resource/36c79c62-04af-4fbf-88a7-2764303ae61c/download/paises_2016_geom_10.csv"
dataframe_url = pd.read_csv(url)
st.dataframe(dataframe_url)







# st.subheader("DataFrame de SQLite:")
# base_de_datos = sqlite3.connect('estudiantes.db')
# cursor = base_de_datos.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS estudiantes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Nombre TEXT,
#     Calificacion REAL
# )
# ''')

# informacion = [
#     ('Mariana Marulanda', 5.0),
#     ('Juan Acosta', 4.5),
#     ('Ana María López', 4.8),
#     ('Pedro Pérez', 3.9),
#     ('María Gómez', 4.2),
# ]

# cursor.executemany('''
# INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)''', informacion)
# base_de_datos.commit()

# consulta = "SELECT * FROM estudiantes"
# dataframe_sqlite = pd.read_sql_query(consulta, base_de_datos)
# st.dataframe(dataframe_sqlite)
# cursor.close()
# base_de_datos.close()







st.subheader("DataFrame de NumPy: ")
numeros_enteros = np.array([1, 2, 3, 4])
letras = np.array(['M', 'A', 'R', 'I'])
numeros_decimales = np.array([1.5, 2.5, 3.5, 5.0])

nombres_columnas = ['Números enteros', 'Letras', 'Números decimales']
dataframe_numpy = pd.DataFrame({
    'Números enteros': numeros_enteros,
    'Letras': letras,
    'Números decimales': numeros_decimales
})
st.dataframe(dataframe_numpy)





# load_dotenv()
# firebase_credentials_json = os.getenv("FIREBASE_CREDENTIALS")
# firebase_credentials = json.loads(firebase_credentials_json)

# st.subheader("DataFrame de Firebase: ")
# if not firebase_admin._apps:
#     credenciales = credentials.Certificate(firebase_credentials)
#     firebase_admin.initialize_app(credenciales)

# db = firestore.client()
# coleccion = 'usuarios'
# documentos = db.collection(coleccion).stream()
# data = []
# for doc in documentos:
#     data.append(doc.to_dict())
# dataframe_firebase = pd.DataFrame(data)
# st.dataframe(dataframe_firebase)




mongo_url = "mongodb://localhost:27017/"
nombre_db = "proyecto_mongodb"
colleccion = "usuarios"

@st.cache_resource
def iniciar_coneccion_mongo():
    return MongoClient(mongo_url)

servidor_mongo = iniciar_coneccion_mongo()
db_mongo = servidor_mongo[nombre_db]
coleccion_mongo = db_mongo[colleccion]  

if coleccion_mongo.count_documents({}) == 0:
    coleccion_mongo_insertar_datos = ([
        {"Nombre": "Elena", "Ciudad": "Bogotá"},
        {"Nombre": "Martha", "Ciudad": "Medellín"},
        {"Nombre": "John", "Ciudad": "Cali"},
        {"Nombre": "María", "Ciudad": "Barranquilla"}
    ])
    


datos_mongo = list(coleccion_mongo.find())  


dataframe_mongo = pd.DataFrame(datos_mongo)


st.subheader("Datos desde MongoDB: ")
st.dataframe(dataframe_mongo)






