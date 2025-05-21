import streamlit as st
import pandas as pd
import io 
import csv
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Actividad #2 ")

st.markdown("""
""")

#Aquí es donde se carga al data y se muestra
st.subheader("Dataset.")
dataframe_estudiantes_colombia = pd.read_csv('static/datasets/estudiantes_colombia.csv')
st.dataframe(dataframe_estudiantes_colombia)


#Acá solo se pide que muestre las primeras 5 filas.
st.subheader("Ver las primeras 5 filas.")
st.write(dataframe_estudiantes_colombia.head())


#Acá solo se pide que muestre las últimas 5 filas.
st.subheader("Ver las últimas 5 filas.")
st.write(dataframe_estudiantes_colombia.tail())


#Esto muestra características especificas de las columnas numéricas.
st.header("Resumen.")
st.subheader("Resumen con 'Describe'.")
descripcion = dataframe_estudiantes_colombia.describe()
st.write(descripcion)


#Este nos muestra la información del dataframe, cuantas columnas tiene, su tipo, la cantidad de datos que hay en cada una y así.
st.subheader("Resumen con 'Info'.")
info = dataframe_estudiantes_colombia.info()
buffer = io.StringIO()
dataframe_estudiantes_colombia.info(buf=buffer)
info_string = buffer.getvalue()
st.code(info_string)


#Acá solo se pide mostrar 3 columnas puntuales de las que hay en el dataframe.
st.subheader("Selección de columnas: Nombre, Edad y Promedio.")
st.write(dataframe_estudiantes_colombia[['Nombre', 'Edad', 'Promedio']])


#Este nos filtra por medio de una barra, donde se puede buscar el promedio a filtrar y nos muestra los estudiantes que corresponden al promedio selecciondo.
st.subheader("Filtrar estudiantes por promedio.")
promedio = st.slider("Selecciona el promedio:", 0.0, 5.0, 3.0)

filtrado_de_promedio = dataframe_estudiantes_colombia[dataframe_estudiantes_colombia['Promedio'] >= promedio]

st.write("Estudiantes con promedio mayor o igual a:", promedio)
st.dataframe(filtrado_de_promedio)




