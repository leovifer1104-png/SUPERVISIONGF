import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Supervisión GF", layout="wide")

st.title("📊 Dashboard de Supervisión GF")
st.markdown("Carga tus archivos PDF GF y valida el estado de los contratistas.")

uploaded_files = st.file_uploader("📂 Cargar archivos GF (PDF)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    data = []
    for file in uploaded_files:
        filename = file.name
        try:
            # Nombre esperado: GF_cedula_siif_mes_año.pdf
            _, cedula, siif, mes, anio = filename.replace(".pdf", "").split("_")
            data.append({
                "Cédula": cedula,
                "SIIF": siif,
                "Mes": mes,
                "Año": anio,
                "Archivo": filename,
                "Estado": "✔️ Completo"
            })
        except Exception:
            data.append({
                "Cédula": "Error",
                "SIIF": "Error",
                "Mes": "Error",
                "Año": "Error",
                "Archivo": filename,
                "Estado": "❌ Nombre inválido"
            })
    df = pd.DataFrame(data)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Descargar CSV", csv, "supervision_gf.csv", "text/csv")

