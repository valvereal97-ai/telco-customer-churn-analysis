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
# CARGA Y PREPARACIÓN DEL DATASET
# ==========================================

elif opcion == "📂 Carga de datos":

    st.title("📂 Carga y preparación del dataset")

    st.write(
        "Carga un archivo CSV para comenzar el análisis exploratorio."
    )

    archivo = st.file_uploader(
        "Selecciona tu archivo CSV",
        type=["csv"]
    )

    if archivo is not None:

        # ------------------------------------------
        # 1. LECTURA DEL ARCHIVO
        # ------------------------------------------

        df = pd.read_csv(archivo)

        st.success("✅ Archivo cargado correctamente.")

        # ------------------------------------------
        # 2. INFORMACIÓN GENERAL
        # ------------------------------------------

        st.subheader("👀 Vista previa del dataset")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        # ------------------------------------------
        # 3. DIMENSIONES
        # ------------------------------------------

        st.subheader("📐 Dimensiones del dataset")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Número de filas",
                df.shape[0]
            )

        with col2:
            st.metric(
                "Número de columnas",
                df.shape[1]
            )

        # ------------------------------------------
        # 4. TIPOS DE DATOS
        # ------------------------------------------

        st.subheader("🔎 Tipos de datos")

        tipos_datos = pd.DataFrame({
            "Columna": df.columns,
            "Tipo de dato": df.dtypes.astype(str).values
        })

        st.dataframe(
            tipos_datos,
            use_container_width=True
        )

        # ------------------------------------------
        # 5. VALORES NULOS
        # ------------------------------------------

        st.subheader("⚠️ Valores faltantes")

        nulos = pd.DataFrame({
            "Columna": df.columns,
            "Valores nulos": df.isnull().sum().values
        })

        nulos = nulos.sort_values(
            by="Valores nulos",
            ascending=False
        )

        st.dataframe(
            nulos,
            use_container_width=True
        )

        # ------------------------------------------
        # 6. CONVERSIÓN DE TOTALCHARGES
        # ------------------------------------------

        if "TotalCharges" in df.columns:

            df["TotalCharges"] = pd.to_numeric(
                df["TotalCharges"],
                errors="coerce"
            )

        # ------------------------------------------
        # 7. RESUMEN DESPUÉS DE LA PREPARACIÓN
        # ------------------------------------------

        st.subheader("🧹 Datos preparados")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Filas",
                df.shape[0]
            )

        with col2:
            st.metric(
                "Columnas",
                df.shape[1]
            )

        with col3:
            st.metric(
                "Nulos totales",
                int(df.isnull().sum().sum())
            )

        st.success(
            "✅ Los datos fueron revisados y preparados para el análisis."
        )

    else:

        st.warning(
            "⚠️ Debes cargar un archivo CSV para comenzar."
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

    st.info(
        "Primero debes cargar el archivo CSV desde la sección "
        "'📂 Carga de datos'."
    )
    # ==========================================
# CLASE PARA EL ANÁLISIS DE DATOS
# ==========================================

class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    # --------------------------------------
    # Clasificación de variables
    # --------------------------------------

    def clasificar_variables(self):

        variables_numericas = self.df.select_dtypes(
            include=np.number
        ).columns.tolist()

        variables_categoricas = self.df.select_dtypes(
            exclude=np.number
        ).columns.tolist()

        return variables_numericas, variables_categoricas

    # --------------------------------------
    # Estadísticas descriptivas
    # --------------------------------------

    def estadisticas_descriptivas(self):

        return self.df.describe()

    # --------------------------------------
    # Análisis de valores nulos
    # --------------------------------------

    def analizar_nulos(self):

        nulos = self.df.isnull().sum()

        return nulos[nulos > 0].sort_values(
            ascending=False
        )
