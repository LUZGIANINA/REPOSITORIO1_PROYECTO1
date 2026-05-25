import streamlit as st
import numpy as np
import libreria_funciones as lf

st.title("SISTEMA DE INVENTARIOS DE PRODUCTOS CV")

st.write("Elaborado por: LUZ GARCIA CASTILLO")

st.sidebar.image("logo cv.png")

st.sidebar.title("Busqueda")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Inicio","Sesión 2","Sesión 3","Sesión 4"] )

if sesion == "Inicio":
  st.write("Bienvenidos al Explorador")
  st.image("Python_logo.png" )

elif sesion == "Sesión 2":
  st.write("Iniciamos la busqueda")

 def agregar_producto():

    codigo = input("Ingrese código del producto: ")
    nombre = input("Ingrese nombre del producto: ")
    stock = int(input("Ingrese cantidad en stock: "))
    precio = float(input("Ingrese precio del producto: "))

    inventario.append([
        codigo,
        nombre,
        stock,
        precio
    ])

    print("\nProducto agregado correctamente.\n")


elif sesion == "Sesión 3":
  st.write("Bienvenido la sesión 3")
  
  fin_rango = st.slider("Selecione un valor",min_value = 0 , max_value=20, value =8 )

  arreglo = np.arange(0 , fin_rango)

  st.write(arreglo)



else:
  st.write("Bienvenido la sesión 4")
  principal = st.number_input("ingrese el monto del prestamo", value=1000)
  tasa_anual = st.number_input("ingrese la tasa anual en decimal", value=0.1)
  anios = st.number_input("ingrese el numero de año de prestamol", value=5)
  pagos_anio = st.number_input("Ingrese la cantidad de pagos por año", value=12)
   
  cuota = round(lf.cuota_prestamo(principal,tasa_anual,anios,pagos_anio),2)
  st.write(f"El valor de la cuota es {cuota}")
