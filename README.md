
# 📊 Telco Customer Churn Analytics

## 👤 Autor

**Luis Fernando Valverde Mendoza**

Curso: Especialización en Python for Analytics  
Año: 2026

---

## 📌 Descripción del proyecto

El presente proyecto consiste en el desarrollo de una aplicación
interactiva utilizando Python y Streamlit para realizar un Análisis
Exploratorio de Datos (EDA) sobre clientes de una empresa de
telecomunicaciones.

El objetivo principal es analizar las características de los clientes
e identificar patrones relacionados con el abandono de clientes
(Churn).

La aplicación permite cargar un archivo CSV y realizar diferentes
análisis estadísticos y visualizaciones de manera interactiva.

---

## 🎯 Objetivo

Analizar el comportamiento de los clientes y determinar qué
características pueden estar relacionadas con el abandono del servicio.

A través del análisis exploratorio se busca obtener información que
pueda servir como apoyo para la identificación de patrones y posibles
estrategias de retención de clientes.

---

## 🛠️ Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

---

## 📊 Análisis realizados

La aplicación contiene diferentes análisis exploratorios, entre ellos:

1. Información general del dataset.
2. Estadísticas descriptivas.
3. Distribución de variables numéricas.
4. Análisis de valores faltantes.
5. Distribución de Churn.
6. Churn según tipo de contrato.
7. Churn según género.
8. Churn según servicio de Internet.
9. Churn según antigüedad del cliente.
10. Cargos mensuales según Churn.
11. Relación entre antigüedad y cargos mensuales.
12. Método de pago según Churn.
13. Matriz de correlación.

Para la visualización de los resultados se utilizan gráficos de
barras, histogramas, boxplots, gráficos de dispersión y mapas de
correlación.

---

## 🧹 Preparación de los datos

El usuario puede cargar un archivo CSV directamente desde la aplicación.

Durante la preparación del dataset se realizan procesos como:

- Revisión de dimensiones.
- Identificación de tipos de datos.
- Identificación de valores faltantes.
- Conversión de la variable `TotalCharges` a formato numérico.
- Clasificación de variables numéricas y categóricas.

---

## 🧩 Programación Orientada a Objetos

El proyecto utiliza una clase denominada `DataAnalyzer`, encargada de
organizar diferentes operaciones relacionadas con el análisis de datos.

Entre sus principales métodos se encuentran:

- `clasificar_variables()`
- `estadisticas_descriptivas()`
- `analizar_nulos()`

Esto permite organizar y reutilizar la lógica de análisis sobre el
dataset.

---

## 📁 Estructura del proyecto

```text
telco-customer-churn-analysis/
│
├── APP3.py
├── requirements.txt
└── README.md
