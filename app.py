import streamlit as st
from PIL import Image 

st.set_page_config(page_title="D´G Glam Studio by Dennis", page_icon=":nail_care:", layout="wide")
email_contact = "glamstudiobydennis@gmail.com"

def load_css():
    with open("style/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

#intro

with st.container():
    st.title("Bienvenido a D´G Glam Studio by Dennis : nail_care:")
    st.title ("tu mejor opcion para realzar tu belleza y estilo")
    st.write("En D´G Glam Studio by Dennis, nos dedicamos a ofrecerte los mejores servicios")
    st.write("de manicura, pedicura, diseño de uñas y mucho más")

    st.write("[Conocenos](#Conocenos)")

    #Conocenos 

with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros")
        st.write (
           """brindamos servicios integrales de belleza especializados de uñas, cejas y pestañas
           ofreciendo atención personalizada, productos de calidad y tecnicas innovadoras que resalten
           la imagen y confianza de cada cliente, garantizado una experiencia comoda, profesional y satisfactorias"""
        )

st.write("[conoce mas sobre nuestros servicios](link de instagram y facebook)")
with animation_column:
    st.empty()

#Servicios 
with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("---")
    st.write("## Servicios que ofrecemos")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/imagenpg1.jpeg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Uñas Tradicionales")
        st.write("Limpieza, corte, limado y esmatado básico")
        st.write("[ver servicios](https://nailstudio.com/servicios)")

#Contacto
with st.container():
    st.write("---")
    st.header("Contáctanos")
    st.write("¿Tienes alguna pregunta o deseas reservar una cita? No dudes en contactarnos.")
    contact_form = """
    <form action="https://formsubmit.co/{email_contact}" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Tu nombre" required>
     <input type="email" name="email" placeholder="Tu email" required>
     <textarea name="message" placeholder="Tu mensaje aqui"></textarea>
     <button type="submit">Enviar</button>
    </form>
    """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
