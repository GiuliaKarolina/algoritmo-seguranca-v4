import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.let_it_rain import rain
import streamlit.components.v1 as components
import os

# 1. CONFIGURAÇÃO DE DESIGN (UI/UX PREMIUM)
# Disfarce técnico para a aba do navegador
st.set_page_config(page_title="Relatório Técnico - Sistema de Segurança", page_icon="📊", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Montserrat:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fe9a9e 100%);
    }

    #MainMenu, footer, header {visibility: hidden;}
    
    .glass-card {
        background: rgba(255, 255, 255, 0.35);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        padding: 30px;
        margin: 10px auto;
        max-width: 750px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }

    h1 {
        font-family: 'Dancing Script', cursive;
        color: #ffffff;
        font-size: 3.8rem !important;
        text-align: center;
        text-shadow: 2px 2px 8px rgba(214, 51, 132, 0.4);
    }

    p, span, label, div, .stRadio, .stTextInput {
        font-family: 'Montserrat', sans-serif !important;
        color: #3d3d3d !important;
        font-size: 1rem !important;
    }

    [data-testid="stImage"] img {
        border-radius: 25px;
        border: 4px solid white;
    }

    .rodape {
        text-align: center;
        color: white;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.9rem !important;
        margin-top: 50px;
        opacity: 0.9;
    }
    
    div[data-testid="stAudio"] audio {
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 25px;
        padding: 5px;
        border: 1px solid white;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SUPERIOR
selected = option_menu(
    menu_title=None,
    options=["Início", "Nossas Fotos", "Quiz", "Desafio"],
    icons=["house-heart-fill", "images", "patch-question-fill", "gift-fill"],
    orientation="horizontal",
    styles={
        "container": {"padding": "5!important", "background-color": "rgba(255,255,255,0.5)"},
        "nav-link-selected": {"background-color": "#d63384"},
    }
)

# 3. CONTEÚDO
if selected == "Início":
    rain(emoji="🌸", font_size=30, falling_speed=3, animation_length="infinite")
    st.markdown("<h1>Para o Homem da minha vida 💖</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #d63384; font-family: Dancing Script; font-size: 2.5rem; margin-top:0;'>Oi, meu amor! 💌</h2>", unsafe_allow_html=True)
        st.write("Dei um monte de chicotada na IA pra poder demonstrar uma fração da nossa história. Te amo muito meu amor, olha aí meu projetinho.")
        
        # GIF Centralizado
        st.image("https://media.tenor.com/y2be8_vO78IAAAAi/cute-ice-bear-love-puffy.gif", use_container_width=True)
        
        # Player de Música (Melhorado para carregar do GitHub)
        if os.path.exists("musica.mp3"):
            with open("musica.mp3", "rb") as f:
                st.audio(f.read(), format="audio/mp3", loop=True)
        else:
            st.warning("🎵 Arquivo 'musica.mp3' não encontrado. Verifique se ele está no GitHub!")
            
        st.markdown("</div>", unsafe_allow_html=True)

elif selected == "Nossas Fotos":
    rain(emoji="🐱🐒", font_size=30, falling_speed=4, animation_length=2)
    st.markdown("<h1 style='color:white;'>Nossos Momentos</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    fotos = ["foto1.jpeg", "foto2.jpeg", "foto3.jpeg", "foto4.jpeg", "foto5.jpeg", "foto6.jpeg"]
    
    for i, foto in enumerate(fotos):
        with [col1, col2, col3][i % 3]:
            if os.path.exists(foto):
                st.image(foto, use_container_width=True)
            else:
                st.info(f"Falta a imagem {foto}")

elif selected == "Quiz":
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#d63384; font-family: Dancing Script; font-size: 2.5rem; margin-top:0;'>📝 Quiz</h2>", unsafe_allow_html=True)
        p1 = st.radio("O que eu mais amo em você?", [
            "Seu sorrisinho fofo 😊", "Seu olhar 👀", "Sua voz 🎵", "Seu corpo perfeito 💪",
            "Seu cabelo lindo 💇", "Sua inteligência 🧠", "Sua paixão por carros 🏎️",
            "Como você me ama 💕", "Você saber jogar de tudo e ser super habilidoso 🎮",
            "Sua nerdice 🤓", "✅ Todas as alternativas estão corretas!"
        ], key="q1")
        p2 = st.text_input("Qual foi o dia que começamos a nos falar? (Dica: d/m/aaaa)", key="q2")
        if st.button("Conferir Resultado"):
            if p1 == "✅ Todas as alternativas estão corretas!" and (p2 == "09/04/2025" or p2 == "9/4/2025"):
                st.balloons(); st.success("Acertou tudo, meu amor! ❤️")
            else: st.error("Tente de novo!")
        st.markdown("</div>", unsafe_allow_html=True)

elif selected == "Desafio":
    rain(emoji="❤️", font_size=30, falling_speed=4, animation_length="infinite")
    st.markdown("<h1 style='color:white;'>Um desafio final...</h1>", unsafe_allow_html=True)
    components.html(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');
            .card { background: rgba(255, 255, 255, 0.45); backdrop-filter: blur(10px); border-radius: 30px; padding: 30px; text-align: center; font-family: 'Montserrat', sans-serif; height: 300px; border: 1px solid rgba(255, 255, 255, 0.5); box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin: 0 auto; max-width: 550px; }
            #area-botoes { position: relative; height: 150px; margin-top: 30px; width: 100%; }
            button { padding: 12px 40px; font-size: 16px; border-radius: 20px; border: none; font-weight: bold; cursor: pointer; }
            .btn-sim { background: #d63384; color: white; position: absolute; left: 15%; top: 50%; transform: translateY(-50%); }
            .btn-nao { background: white; color: #666; position: absolute; right: 15%; top: 50%; transform: translateY(-50%); transition: 0.1s; }
        </style>
        <div class="card">
            <p style="font-size: 18px; color: #3d3d3d;">Você aceita continuar me fazendo a mulher mais feliz do mundo?</p>
            <div id="area-botoes"><button class="btn-sim" onclick="alert('EU SABIA! Te amo infinitamente! ❤️🎉')">SIM!</button><button id="nao" class="btn-nao">Não</button></div>
        </div>
        <script>
            const btn = document.getElementById('nao'); const area = document.getElementById('area-botoes');
            btn.addEventListener('mouseover', () => {
                const maxX = area.clientWidth - btn.clientWidth; const maxY = area.clientHeight - btn.clientHeight;
                btn.style.left = Math.random() * maxX + 'px'; btn.style.top = Math.random() * maxY + 'px';
                btn.style.right = 'auto'; btn.style.transform = 'none';
            });
        </script>
        """, height=350
    )

st.markdown("<div class='rodape'>Feito com ❤️ por Sua tintinha</div>", unsafe_allow_html=True)
