import streamlit as st
import numpy as np
import libreria_funciones as lf

inventario = [
    ["P001", "Teclado", 10, 80],
    ["P002", "Mouse", 4, 35],
    ["P003", "Monitor", 2, 650]
]

st.title("SISTEMA DE INVENTARIOS DE PRODUCTOS CV")

st.write("Elaborado por: LUZ GARCIA CASTILLO")

st.sidebar.image("logo cv.png")

st.sidebar.title("Busqueda")

sesion = st.sidebar.selectbox("Seleccione una opción", ["Inicio","Agregar producto","Mpstrar inventario","Visualizar precio"] )

if sesion == "Inicio":
  st.write("Bienvenidos al Explorador")
  st.image("Python_logo.png" )

elif sesion == "Agregar producto":
  st.write("Busquemos el producto")

  precio = st.number_input("Ingrese el producto", " ")
  descuento = st.number_input("Ingrese el código del ´Producto", min_value = 0 , max_value = 100 )

  precio_final_producto = precio - (precio*(descuento/100))

  st.write("El precio final del producto es: ", precio_final_producto  )


elif sesion == "Stock":
  st.write("Visualización de cantidades")
  
  fin_rango = st.slider("Selecione un valor",min_value = 0 , max_value=20, value =8 )

  arreglo = np.arange(0 , fin_rango)

  st.write(arreglo)



else: 
  st.write("Ingresar Producto")
    codigo = st.text_input("Código")
    nombre = st.text_input("Nombre")
    stock = st.number_input("Stock", min_value=0)
    precio = st.number_input("Precio", min_value=0.0)

    if st.button("Guardar"):

        inventario.append([
            codigo,
            nombre,
            stock,
            precio
        ])

        st.success("Producto agregado correctamente")
   
  cuota = round(lf.cuota_prestamo(principal,tasa_anual,anios,pagos_anio),2)
  st.write(f"El valor de la cuota es {cuota}")
