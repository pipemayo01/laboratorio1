import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.write("""
         #mi primera pagina web
         ## hola chile""")
df = pd.read_csv("UNI_CORR_500_01.txt", skiprows = 4, sep="\t",names =["ID","frames","X","Y","Z"])


with st.sidebar:
    # titulo 
    st.write ("# Opciones")
    div = st.slider("numero de bins: ",0,130,25)
    st.write("Bins=",div)

st.write("""Muestra de datos cargados""")
#graficar tabla
st.table(df.head())
fig, ax = plt.subplots(1,2,figsize= (10,3))
ax[0].hist(df["X"], bins = div, color = "lightcoral")
ax[0].set_xlabel("posicion en metro")
ax[0].set_ylabel("frecuencia")
ax[0].set_title("histograma de posiciones")


ax[1].hist(df["Y"], bins = div, color = "indianred")
ax[1].set_xlabel("posicion en metro")
ax[1].set_ylabel("frecuencia")
ax[1].set_title("histograma de posiciones")
st.pyplot(fig)
