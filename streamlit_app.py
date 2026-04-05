import streamlit as st

# 1. Configuración de la interfaz
st.set_page_config(page_title="Referencia Inteligente - Hospital", layout="centered")

# 2. Título y Bienvenida
st.title("🩺 Asistente de Derivación Digital")
st.markdown("""
Esta herramienta ayuda a los médicos de APS a consultar los **Manuales de Derivación** del Hospital mediante Inteligencia Artificial.
""")

# 3. Selector de Especialidad
especialidad = st.selectbox(
    "Seleccione la especialidad a consultar:",
    ["Cardiología", "Neurología", "Traumatología", "Urología"]
)

# 4. Área de Consulta
st.subheader(f"Consulta sobre {especialidad}")
pregunta = st.text_input("Escribe tu duda (ej: ¿Qué exámenes pide neurología para migraña?)")

if pregunta:
    st.info(f"Buscando en el manual de {especialidad}...")
    # Aquí es donde NotebookLM hará la magia más adelante
    st.write("Respuesta: [Aquí aparecerá la información del manual una vez conectado]")

# 5. Pie de página institucional
st.divider()
st.caption("Unidad de Gestión de Red - Hospital Barros Luco Trudeau")
