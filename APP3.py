import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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
        st.session_state["df"] = df
        # ------------------------------------------
        # CREACIÓN DEL ANALIZADOR
        # ------------------------------------------

        analyzer = DataAnalyzer(df)

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

        # ------------------------------------------
        # 8. PRUEBA DE LA CLASE
        # ------------------------------------------

        variables_numericas, variables_categoricas = (
            analyzer.clasificar_variables()
        )

        st.subheader("🔢 Variables numéricas")

        st.write(variables_numericas)

        st.subheader("🔤 Variables categóricas")

        st.write(variables_categoricas)

    else:

        st.warning(
            "⚠️ Debes cargar un archivo CSV para comenzar."
        )


# ==========================================
# ANÁLISIS EDA
# ==========================================

elif opcion == "📊 Análisis EDA":

    st.title("📊 Análisis Exploratorio de Datos")

    # ------------------------------------------
    # VERIFICAR SI EXISTE UN DATASET
    # ------------------------------------------

    if "df" not in st.session_state:

        st.warning(
            "⚠️ Primero debes cargar el archivo CSV "
            "desde la sección '📂 Carga de datos'."
        )

    else:

        df = st.session_state["df"]

        analyzer = DataAnalyzer(df)

        # ------------------------------------------
        # ANÁLISIS 1: INFORMACIÓN GENERAL
        # ------------------------------------------

        st.header("1️⃣ Información general del dataset")

        st.write(
            "En esta sección se presenta un resumen general "
            "de la información disponible en el dataset."
        )

        # ------------------------------------------
        # INDICADORES
        # ------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "👥 Total de clientes",
                df.shape[0]
            )

        with col2:

            st.metric(
                "📊 Total de variables",
                df.shape[1]
            )

        with col3:

            st.metric(
                "❌ Valores nulos",
                int(df.isnull().sum().sum())
            )

        # ------------------------------------------
        # INFORMACIÓN DE VARIABLES
        # ------------------------------------------

        st.subheader("📋 Información de las variables")

        variables_numericas, variables_categoricas = (
            analyzer.clasificar_variables()
        )

        informacion_variables = pd.DataFrame({
            "Variable": df.columns,
            "Tipo de dato": df.dtypes.astype(str).values
        })

        informacion_variables["Tipo de variable"] = (
            informacion_variables["Variable"].apply(
                lambda x:
                "Numérica"
                if x in variables_numericas
                else "Categórica"
            )
        )

        st.dataframe(
            informacion_variables,
            use_container_width=True
        )

        st.success(
            "✅ Análisis general completado correctamente."
        )
                # ==========================================
        # ANÁLISIS 2: ESTADÍSTICAS DESCRIPTIVAS
        # ==========================================

        st.header("2️⃣ Estadísticas descriptivas")

        st.write(
            "Resumen estadístico de las variables numéricas "
            "del dataset."
        )

        estadisticas = analyzer.estadisticas_descriptivas()
                # ==========================================
        # ANÁLISIS 3: DISTRIBUCIÓN DE VARIABLES
        # NUMÉRICAS
        # ==========================================

        st.header("3️⃣ Distribución de variables numéricas")

        st.write(
            "Histogramas para observar la distribución "
            "de las principales variables numéricas."
        )

        variables_graficos = [
            "tenure",
            "MonthlyCharges",
            "TotalCharges"
        ]

        for variable in variables_graficos:

            if variable in df.columns:

                st.subheader(f"Distribución de {variable}")

                fig, ax = plt.subplots()

                ax.hist(
                    df[variable].dropna(),
                    bins=20
                )

                ax.set_title(
                    f"Distribución de {variable}"
                )

                ax.set_xlabel(variable)

                ax.set_ylabel("Cantidad de clientes")

                st.pyplot(fig)

                plt.close(fig)

        st.dataframe(
            estadisticas,
            use_container_width=True
        )
                # ==========================================
        # ANÁLISIS 4: VALORES FALTANTES
        # ==========================================

        st.header("4️⃣ Análisis de valores faltantes")

        st.write(
            "Identificación de las variables que presentan "
            "valores faltantes en el dataset."
        )

        nulos_analisis = analyzer.analizar_nulos()

        if len(nulos_analisis) > 0:

            st.dataframe(
                nulos_analisis.rename(
                    "Cantidad de valores faltantes"
                ).to_frame(),
                use_container_width=True
            )

            fig, ax = plt.subplots()

            nulos_analisis.plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(
                "Valores faltantes por variable"
            )

            ax.set_xlabel("Variable")

            ax.set_ylabel("Cantidad de valores faltantes")

            plt.xticks(rotation=45)

            st.pyplot(fig)

            plt.close(fig)

        else:

            st.success(
                "✅ No se encontraron valores faltantes."
            )
                    # ==========================================
        # ANÁLISIS 5: DISTRIBUCIÓN DE CHURN
        # ==========================================

        st.header("5️⃣ Distribución de Churn")

        st.write(
            "Distribución de clientes según su estado "
            "de permanencia o abandono."
        )

        churn_counts = df["Churn"].value_counts()

        churn_percentage = (
            df["Churn"]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("👥 Cantidad de clientes")

            st.dataframe(
                churn_counts.rename(
                    "Cantidad"
                ).to_frame(),
                use_container_width=True
            )

        with col2:

            st.subheader("📊 Porcentaje de clientes")

            st.dataframe(
                churn_percentage.rename(
                    "Porcentaje (%)"
                ).to_frame(),
                use_container_width=True
            )

        # ------------------------------------------
        # GRÁFICO
        # ------------------------------------------

        fig, ax = plt.subplots()

        churn_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Distribución de clientes según Churn"
        )

        ax.set_xlabel("Churn")

        ax.set_ylabel("Cantidad de clientes")

        plt.xticks(rotation=0)

        st.pyplot(fig)

        plt.close(fig)
                # ==========================================
        # ANÁLISIS 6: CHURN SEGÚN TIPO DE CONTRATO
        # ==========================================

        st.header("6️⃣ Churn según tipo de contrato")

        st.write(
            "Análisis de la relación entre el tipo de contrato "
            "y el abandono de clientes."
        )

        contrato_churn = pd.crosstab(
            df["Contract"],
            df["Churn"]
        )

        st.dataframe(
            contrato_churn,
            use_container_width=True
        )

        fig, ax = plt.subplots()

        contrato_churn.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Churn según tipo de contrato"
        )

        ax.set_xlabel("Tipo de contrato")

        ax.set_ylabel("Cantidad de clientes")

        plt.xticks(rotation=0)

        ax.legend(
            title="Churn"
        )

        st.pyplot(fig)

        plt.close(fig)
