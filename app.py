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

opción = st.sidebar.selectbox("Seleccione una opción", ["Inicio","Agregar producto","Mostrar inventario","Visualizar precio"] )

if opción == "Inicio":
  st.write("Bienvenidos al Explorador")
  st.image("Python_logo.png" )

elif opción == "Agregar producto":
    st.write("Registrar nuevo producto")
    código = st.text_input("Código del producto")
    nombre = st.text_input("Nombre del producto")
    stock = st.number_input("Cantidad en stock", min_value=0)
    precio = st.number_input("Precio", min_value=0.0)

    if st.button("Guardar Producto"):

        inventario.append([
            código,
            nombre,
            stock,
            precio
        ])

        st.success("✅ Producto agregado correctamente")


elif opción == "Mostrar inventario":
  st.write("Visualización de cantidades")
  for producto in inventario:

        st.write("Código:", producto[0])
        st.write("Producto:", producto[1])
        st.write("Stock:", producto[2])
        st.write("Precio: S/", producto[3])

        # ALERTA DE STOCK
        if producto[2] <= 5:
            st.error("⚠ ALERTA: STOCK BAJO")

        st.write("----------------------------")


elif opción == "Visualizar Precio":
  st.write("Consultar Precio")
    
nombres = ["Teclado","Mouse","Monitor"]
    
    for producto in inventario:
        nombres.append(producto[1])

    seleccion = st.selectbox(
        "Seleccione un producto",
        nombres
    )

    for producto in inventario:

        if producto[1] == seleccion:
              st.success(
                f"💰 Precio de {producto[1]}: S/ {producto[3]}"
            )
            
        st.info(
                f"📦 Stock disponible: {producto[2]}"
            )
        
        if producto[2] <= 5:
                st.warning("⚠ Quedan pocas unidades")


