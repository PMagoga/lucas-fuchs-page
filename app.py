import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Lucas Fuchs Team", page_icon="🏋️‍♂️", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_training = load_lottieurl("https://lottie.host/38f6401c-1f94-401f-9991-014e39b3cd4e/q0CrbqucPv.json")
img_contact_form = Image.open("images/imagem1.png")
img_lottie_animation = Image.open("images/imagem2.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Olá, eu sou o Lucas Fuchs :wave:")
    st.title("Personal Trainer de Santa Maria - RS")
    st.write(
        "No meu canal do Youtube eu falo sobre entretenimento, passo dicas e informações sobre o mundo fitness."
    )
    st.write("[Adquira meu ebook >](https://sun.eduzz.com/8WPDG65NWP)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("O que eu faço")
        st.write("##")
        st.write(
            """            
            No meu canal do YouTube, eu dou dicas e informações sobre o mundo fitness:
            - Lá você encontra dicas práticas para melhorar seu condicionamento físico.
            - Informações sobre nutrição e treinos eficazes.
            Explore nosso conteúdo divertido e educativo, onde buscamos inspirar e motivar todos a alcançarem seus objetivos de saúde. 
            Inscreva-se para não perder nossas atualizações semanais e transforme sua jornada fitness em algo empolgante e acessível!
            
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@LucasFuchs)")
    with right_column:
        st_lottie(lottie_training, height=300, key="training")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Meus projetos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("DESCUBRA O SEU BIOTIPO (MUITO FÁCIL)")
        st.write(
            """
            No vídeo de hoje eu vou explicar o que é biotipo, quais as diferenças entre eles e como você faz para achar o seu. 
            Deixe aqui nos comentários qual é o seu e qual é a maior dificuldade pra você.
            """
        )
        st.markdown("[Veja o vídeo...](https://www.youtube.com/watch?v=JRthud484jw)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("TOMAR ANTI-INFLAMATÓRIO PREJUDICA NO TREINO?")
        st.write(
            """
            Nesse vídeo eu explico se é bom o não tomar anti-inflamatório pra quem treina e o que os anti-inflamatórios fazem no nosso corpo e porque sentimos dores quando treinamos!
            """
        )
        st.markdown("[Veja o vídeo...](https://www.youtube.com/watch?v=73xciqA6cnc)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Entre em contato comigo!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Seu Nome" required>
        <input type="email" name="email" placeholder="Seu email" required>
        <textarea name="message" placeholder="Escreva sua mensagem aqui" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()