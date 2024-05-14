
import streamlit as st

# Encabezado:
st.header("Pagina Web de Nami y Lilia", divider="rainbow")
st.subheader("Estas son las últimas fotos de las niñas de la casa:")

# Columnas con imagenes
col1, col2 = st.columns(2, gap="large")

fotos_nami = ["nami1.jpg", "nami2.jpg", "nami3.jpg"]
fotos_lilia = ["lilia1.jpg", "lilia2.jpg", "lilia3.jpg", "lilia4.jpg", "lilia5.jpg"]

with col1:
    st.subheader("Fotos de Nami")

    # Imagen No. 1
    imagen = fotos_nami[0]  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Nami en su primer cumpleaños!")

    # Imagen No. 2
    imagen = fotos_nami[1]  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Mi hermana se está comiendo mi torta!")

    # Imagen No. 3
    imagen = fotos_nami[2]  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡En la playa con mucho calor!")

with col2:
    st.subheader("Fotos de Lilia")

    # Imagen No. 1
    imagen = fotos_lilia[0]  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Yo divina en la playa :beach:!")

    # Imagen No. 2
    imagen = fotos_lilia[2]  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Mami, ahorita no... estoy relajadita!")

    # Imagen No. 2
    imagen = fotos_lilia[3]  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Yo también quería foto en el cumpleaños!")



