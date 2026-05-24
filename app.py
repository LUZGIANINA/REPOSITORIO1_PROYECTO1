import streamlit as st
import numpy as np
import libreria_funciones as lf

st.title("SISTEMA DE INVENTARIOS DE PRODUCTOS CV")

st.write("Elaborado por: LUZ GARCIA CASTILLO")

st.sidebar.image("logo cv.png")

st.sidebar.title("Busqueda")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )

if sesion == "Inicio":
  st.write("Bienvenidos al Explorador")
  st.image("Python_logo.png" )

elif sesion == "Sesión 2":
  st.write("Bienvenido la sesión 2")

  precio = st.number_input("Ingrese el precio del producto", min_value = 0 , max_value = 5000 , value = 1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100% ", min_value = 0 , max_value = 100 )

  precio_final_producto = precio - (precio*(descuento/100))

  st.write("El precio final del producto es: ", precio_final_producto  )


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
