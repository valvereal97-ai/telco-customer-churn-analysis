import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ==========================================

st.set_page_config(
    page_title="Telco Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📊 Telco Churn Analytics")

opcion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "🏠 Home",
        "📂 Carga de datos",
        "📊 Análisis EDA"
    ]
)


# ==========================================
# HOME
# ==========================================

if opcion == "🏠 Home":

    st.title("📊 Telco Customer Churn Analytics")

    st.subheader("Análisis Exploratorio de Datos")

    st.write(
        """
        Esta aplicación permite realizar un análisis exploratorio
        del comportamiento de los clientes de una empresa de
        telecomunicaciones, con el objetivo de identificar patrones
        asociados a la fuga de clientes (Churn).
        """
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 👤 Autor")
        st.write("**LUIS FERNANDO VALVERDE MENDOZA**")
        st.write("Especialización en Python for Analytics")
        st.write("Año: 2026")

    with col2:
        st.write("### 🛠️ Tecnologías utilizadas")
        st.write("- Python")
        st.write("- Pandas")
        st.write("- NumPy")
        st.write("- Matplotlib")
        st.write("- Seaborn")
        st.write("- Streamlit")

    st.markdown("---")

    st.info(
        "El proyecto utiliza técnicas de Análisis Exploratorio "
        "de Datos (EDA) para comprender las características de "
        "los clientes y su relación con el Churn."
    )


# ==========================================
# CARGA DEL DATASET
# ==========================================

elif opcion == "📂 Carga de datos":

    st.title("📂 Carga del dataset")

    st.write(
        "Selecciona el archivo TelcoCustomerChurn.csv para comenzar el análisis."
    )

    archivo = st.file_uploader(
        "Carga tu archivo CSV",
        type=["csv"]
    )

    if archivo is not None:

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")

        st.subheader("👀 Vista previa del dataset")

        st.dataframe(df.head())

        st.subheader("📐 Dimensiones del dataset")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Número de filas", df.shape[0])

        with col2:
            st.metric("Número de columnas", df.shape[1])

    else:

        st.warning(
            "⚠️ Debes cargar el archivo CSV para comenzar."
        )


# ==========================================
# ANÁLISIS EDA
# ==========================================

elif opcion == "📊 Análisis EDA":

    st.title("📊 Análisis Exploratorio de Datos")

    st.info(
        "Primero debes cargar el archivo CSV desde la sección "
        "'📂 Carga de datos'."
    )
