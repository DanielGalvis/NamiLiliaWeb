
import os

import streamlit as st
from PIL import Image

# Obtener el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Función para rotar imágenes
def rotate_image(image_path, angle):
    image = Image.open(image_path)
    return image.rotate(angle, expand=True)

# Encabezado:
st.header("Pagina Web de Nami y Lilia", divider="rainbow")
st.subheader("Estas son las últimas fotos de las niñas de la casa:")

# Columnas con imagenes
col1, col2 = st.columns(2, gap="large")

# Definir las rutas completas a las imágenes
fotos_nami = [os.path.join(current_dir, "nami1.JPG"),
              os.path.join(current_dir, "nami2.JPG"),
              os.path.join(current_dir, "nami3.JPG")]

fotos_lilia = [os.path.join(current_dir, "lilia1.JPG"),
               os.path.join(current_dir, "lilia2.JPG"),
               os.path.join(current_dir, "lilia3.JPG"),
               os.path.join(current_dir, "lilia4.JPG"),
               os.path.join(current_dir, "lilia5.JPG")]

with col1:
    st.subheader("Fotos de Nami")

    # Imagen No. 1
    imagen = rotate_image(fotos_nami[0], 90)  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Nami en su primer cumpleaños!")

    # Imagen No. 2
    imagen = rotate_image(fotos_nami[1], 90)  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Mi hermana se está comiendo mi torta!")

    # Imagen No. 3
    imagen = Image.open(fotos_nami[2])
    st.image(imagen, caption="¡En la playa con mucho calor!")

with col2:
    st.subheader("Fotos de Lilia")

    # Imagen No. 1
    imagen = rotate_image(fotos_lilia[0], 90)  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Yo divina en la playa :beach:!")

    # Imagen No. 2
    imagen = rotate_image(fotos_lilia[2], 90)  # Ajusta el ángulo según sea necesario
    st.image(imagen, caption="¡Mami, ahorita no... estoy relajadita!")

    # Imagen No. 2
    imagen = Image.open(fotos_lilia[3])
    st.image(imagen, caption="¡Yo también quería foto en el cumpleaños!")
