import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------
# CONFIGURAÇÃO DE PAGINA
# -----------------
st.set_page_config(
    page_title="Passos Mágicos | Datathon",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------
# IDENTIDADE VISUAL E ESTILO (Dark Theme + Roxo Rocketseat)
# -----------------
ROXO_PM = "#8257E5"
st.markdown(f"""
    <style>
    /* Ocultar menu padrão do Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Global Background and Text */
    .stApp {{
        background-color: #0d1117;
        color: #c9d1d9;
    }}
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {{
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }}
    
    /* Highlight Roxo */
    .highlight {{
        color: {ROXO_PM};
        font-weight: bold;
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: #161b22;
    }}
    
    /* Cards para info e tooltips */
    div.stInfo {{
        background-color: rgba(130, 87, 229, 0.1) !important;
        color: #e6edf3 !important;
        border-left-color: {ROXO_PM} !important;
    }}
    
    /* Cards KPI */
    .kpi-card {{
        background-color: #161b22;
        border-radius: 10px;
        padding: 20px;
        border-top: 4px solid {ROXO_PM};
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }}
    .kpi-value {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {ROXO_PM};
        margin: 10px 0;
    }}
    .kpi-label {{
        font-size: 1rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    /* Botões Padrão Streamlit */
    .stButton>button {{
        background-color: {ROXO_PM};
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s;
    }}
    .stButton>button:hover {{
        background-color: #996bf5;
        box-shadow: 0 0 10px rgba(130,87,229,0.5);
    }}
    </style>
""", unsafe_allow_html=True)

# -----------------
# CARGA DE DADOS
# -----------------
@st.cache_data
def carregar_dados():
    df = pd.read_csv('dados_limpos_pm.csv')
    return df

@st.cache_resource
def carregar_modelo():
    try:
        with open('modelo_risco.pkl', 'rb') as f:
            modelo_dict = pickle.load(f)
        return modelo_dict
    except FileNotFoundError:
        return None

df = carregar_dados()
modelo_dict = carregar_modelo()

# -----------------
# FUNÇÕES DE PLOTAGEM MATPLOTLIB/SEABORN DARK
# -----------------
def aplicar_tema_grafico():
    plt.style.use('dark_background')
    sns.set_theme(style="dark", rc={"axes.facecolor":"#0d1117", "figure.facecolor":"#0d1117"})
    # Paleta dark roxa
    paleta_dark = sns.dark_palette(ROXO_PM, reverse=True, n_colors=5)
    sns.set_palette(paleta_dark)
    return paleta_dark

# -----------------
# SIDEBAR NAVEGAÇÃO
# -----------------
with st.sidebar:
    svg_logo = """
    <svg width="100%" height="120" viewBox="0 0 400 150" xmlns="http://www.w3.org/2000/svg">
      <g fill="#8257E5">
        <path d="M 50,40 C 55,40 60,35 60,30 C 60,25 55,20 50,20 C 45,20 40,25 40,30 C 40,35 45,40 50,40 Z"/>
        <path d="M 55,45 C 65,45 70,55 70,70 L 65,130 L 55,130 L 55,90 L 45,90 L 45,130 L 35,130 L 30,70 C 30,55 35,45 45,45 Z"/>
        <path d="M 20,70 C 23,70 25,67 25,64 C 25,61 23,58 20,58 C 17,58 15,61 15,64 C 15,67 17,70 20,70 Z"/>
        <path d="M 23,73 C 30,73 32,80 32,90 L 30,130 L 24,130 L 24,105 L 16,105 L 16,130 L 10,130 L 8,90 C 8,80 10,73 17,73 Z"/>
        <path d="M 32,85 L 35,85 L 35,80 L 32,80 Z"/>
      </g>
      <text x="80" y="65" font-family="'Segoe UI', Arial, sans-serif" font-weight="900" font-style="italic" font-size="52" fill="#c9d1d9">PASSOS</text>
      <text x="85" y="115" font-family="'Segoe UI', Arial, sans-serif" font-weight="900" font-style="italic" font-size="52" fill="#c9d1d9">MÁGICOS</text>
      <path d="M 160,80 L 163,86 L 170,86 L 165,90 L 167,97 L 160,93 L 153,97 L 155,90 L 150,86 L 157,86 Z" fill="#8257E5"/>
    </svg>
    """
    st.markdown(svg_logo, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🧭 Menu de Navegação")
    menu = st.radio("", ["🏠 Conheça o Projeto", "📊 Análises (Storytelling)", "🔍 Predição de Risco"])
    
    st.markdown("---")
    
    # Disclaimer no formato Footer
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
    st.markdown(
        "<div style='color: #8b949e; font-size: 13px; text-align: center; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1);'>"
        "Transformação Educacional<br><b>Passos Mágicos - Fase 5 FIAP</b></div>", 
        unsafe_allow_html=True
    )

# ==========================================
# PÁGINA: CONHEÇA O PROJETO
# ==========================================
if menu == "🏠 Conheça o Projeto":
    st.title("Conheça o Projeto")
    
    st.markdown("### A Associação Passos Mágicos")
    st.markdown('''
A Associação Passos Mágicos tem uma trajetória de 33 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.

A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.

Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.
    ''')
    
    st.markdown("---")
    
    st.markdown("### Sobre este Projeto (Datathon - Fase 5)")
    st.markdown('''
**Quais dados são usados?**  
Utilizamos o dataset de pesquisa extensiva do desenvolvimento educacional no período de 2022, 2023 e 2024. Esses dados contêm métricas de desempenho acadêmico (IDA), engajamento (IEG), fatores psicossociais (IPS) e avaliações psicopedagógicas (IPP) dos alunos atendidos.

**O que tentamos responder?**  
O objetivo principal é responder a perguntas de dores de negócio através de Analytics, identificando perfis de defasagem, descobrindo o impacto de indicadores como engajamento e bolsas de estudo, e demonstrando a efetividade real do programa ao longo dos anos.

**O uso de Machine Learning e o que ela prevê?**  
Com base no histórico dos alunos, construímos um modelo de A.I. preditivo (XGBoost Otimizado) capaz de identificar padrões que antecedem uma queda no rendimento e aumento da defasagem escolar. O modelo **prevê a probabilidade probabilidade do aluno entrar em risco grave**, permitindo ação focada e precoce dos educadores e psicólogos da ONG.
    ''')

# ==========================================
# PÁGINA: DATA STORYTELLING
# ==========================================
elif menu == "📊 Análises (Storytelling)":
    st.title("Storytelling com Dados")
    st.markdown("Acompanhe as principais descobertas extraídas dos indicadores de desempenho acadêmico (IDA), engajamento (IEG) e bem-estar (IPS).")
    
    paleta_dark = aplicar_tema_grafico()
    
    # --- GRÁFICO 1: EVOLUÇÃO GERAL ---
    st.markdown("### 1. Evolução da Trajetória (2022-2024)")
    st.markdown("Como o impacto global do programa se comporta ano a ano?")
    
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    indicadores_evolucao = ['ida', 'ieg', 'ips', 'inde']
    df_timeline = df.groupby('ano')[indicadores_evolucao].mean().reset_index()
    
    cores_linha = ['#e1d5fa', '#a188e5', ROXO_PM, '#ffb86c'] # Tons com laranja como destaque
    for i, col in enumerate(indicadores_evolucao):
        ax1.plot(df_timeline['ano'], df_timeline[col], marker='o', lw=3, color=cores_linha[i], label=col.upper())
    
    ax1.set_xticks([2022, 2023, 2024])
    ax1.set_ylim(0, 10)
    ax1.legend(frameon=False, ncol=4, loc='lower center', bbox_to_anchor=(0.5, -0.3))
    ax1.grid(axis='y', alpha=0.2)
    sns.despine(left=True, bottom=True)
    
    st.pyplot(fig1)
    
    # Tooltip Executivo G1
    with st.expander("💡 **Resumo Executivo (Insight)**", expanded=True):
        st.markdown(f"> **Crescimento Consistente**: Todos os indicadores principais crescem ao longo dos 3 anos. O projeto escalou sua abrangência recuperando passivos educacionais dos anos anteriores, comprovando que a metodologia se sustenta perfeitamente a longo prazo.")

    st.markdown("---")
    
    # --- GRÁFICO 2: ENGAJAMENTO ---
    st.markdown("### 2. O Poder do Engajamento (IEG)")
    
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        df['ieg_nivel'] = pd.cut(df['ieg'], bins=[-1, 5.9, 7.9, 10], labels=['Baixo', 'Médio', 'Alto'])
        df_ieg_medias = df.groupby('ieg_nivel')[['ida', 'ipv']].mean().reset_index()
        df_ieg_melt = df_ieg_medias.melt(id_vars='ieg_nivel', var_name='Indicador', value_name='Nota')
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.barplot(data=df_ieg_melt, x='ieg_nivel', y='Nota', hue='Indicador', palette=[ROXO_PM, '#ffb86c'], ax=ax2)
        ax2.set_xlabel('Nível de Entrega e Frequência')
        ax2.set_ylabel('Nota (Média)')
        ax2.legend(frameon=False)
        sns.despine(left=True)
        st.pyplot(fig2)
        
    with col_b:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.info(f"**💡 Insight Estratégico**\n\nAlunos com 'Alto' engajamento despontam! O foco da ONG gamificar e monitorar tarefas diárias garante automaticamente notas (IDA) elevadas e impulsiona o Ponto de Virada. Focar no comportamento é resolver a nota.")

    st.markdown("---")
    
    # --- GRÁFICO 3: BOLSISTAS ---
    st.markdown("### 3. A Alavanca da Bolsa de Estudos")
    
    col_c, col_d = st.columns([1, 1])
    with col_c:
        df_bolsa = df.groupby('bolsa')[['ida', 'inde']].mean().reset_index()
        df_bolsa['bolsa'] = df_bolsa['bolsa'].replace({'Sim': 'Bolsista Privado', 'Não': 'Escola Pública'})
        df_melt_bolsa = df_bolsa.melt(id_vars='bolsa', var_name='Indicador', value_name='Nota')
        
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        sns.barplot(data=df_melt_bolsa, x='Indicador', y='Nota', hue='bolsa', palette=['#50fa7b', ROXO_PM], ax=ax3)
        ax3.set_xlabel('')
        ax3.set_ylabel('Nota (Média)')
        ax3.legend(frameon=False)
        sns.despine(left=True)
        st.pyplot(fig3)
        
    with col_d:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.info(f"**💡 Insight Estratégico**\n\nEstudar em colégios privados sob a tutela da Passos Mágicos cria um 'Duplo Motor'. Os bolsistas performam acima da média geral em proficiência. Ampliar alianças com a rede privada é o maior acelerador que a Passos Mágicos detém.")

# ==========================================
# PÁGINA: MACHINE LEARNING (PREDIÇÃO)
# ==========================================
elif menu == "🤖 Predição de Risco":
    st.title("Sistema de Alerta Precoce")
    st.markdown("Utilize o modelo de **Inteligência Artificial (XGBoost Otimizado)** para prever a probabilidade matemática de um aluno entrar em risco grave de defasagem acadêmica no próximo período.")
    
    if modelo_dict is None:
        st.error("O modelo Preditivo ('modelo_risco.pkl') não foi encontrado. Por favor, execute o notebook de Machine Learning.")
    else:
        xgb_model = modelo_dict['modelo']
        le_genero = modelo_dict['le_genero']
        le_bolsa = modelo_dict['le_bolsa']
        
        with st.form("form_predicao"):
            st.markdown("### 👤 Dados do Aluno")
            c1, c2, c3 = st.columns(3)
            with c1:
                idade = st.number_input("Idade de Ingresso", min_value=5, max_value=25, value=12)
                genero = st.selectbox("Gênero", ["Menino", "Menina"])
                gen_val = "Masculino" if genero == "Menino" else "Feminino"
            with c2:
                bolsa = st.selectbox("Aluno possui Bolsa em Instituição Privada?", ["Não", "Sim"])
            with c3:
                st.markdown('<div style="height: 25px;"></div>', unsafe_allow_html=True)
                submit = st.form_submit_button("Analisar Risco com A.I. ⚡", use_container_width=True)
            
            st.markdown("### 📝 Notas do Período Atual")
            n1, n2, n3 = st.columns(3)
            with n1:
                ida = st.slider("Desempenho Acadêmico (IDA)", 0.0, 10.0, 6.0, 0.1)
                delta_ida = st.number_input("Variação (IDA) em relação ao último ano", min_value=-10.0, max_value=10.0, value=0.0, help="Negativo indica que o desempenho caiu")
            with n2:
                ieg = st.slider("Engajamento p/ Tarefas (IEG)", 0.0, 10.0, 7.5, 0.1)
                delta_ieg = st.number_input("Variação (IEG)", min_value=-10.0, max_value=10.0, value=0.0)
            with n3:
                ips = st.slider("Bem Estar Psicossocial (IPS)", 0.0, 10.0, 8.0, 0.1)
                delta_ips = st.number_input("Variação Emocional (IPS)", min_value=-10.0, max_value=10.0, value=0.0, help="Negativo indica que o psicólogo notou piora do bem-estar.")
            
            st.markdown("### 🧠 Avaliações Subjetivas (Professores e Conselhos)")
            o1, o2, o3 = st.columns(3)
            with o1:
                ipp = st.slider("Avaliação Psicopedagógica (IPP)", 0.0, 10.0, 7.0, 0.1)
            with o2:
                iaa = st.slider("Auto-avaliação do Aluno (IAA)", 0.0, 10.0, 8.0, 0.1)
            with o3:
                ipv = st.slider("Ponto de Virada (IPV)", 0.0, 10.0, 6.5, 0.1)
        
        if submit:
            # Transformação categórica
            try:
                # O Encoder espera exatamente a mesma classe que foi treinada (já configuramos antes)
                # Garantindo o tratamento de "Masculino" e "Feminino" (o fit transform do modelo original usou essas strings)
                gen_enc = le_genero.transform([gen_val])[0]
                bolsa_enc = le_bolsa.transform([bolsa])[0]
                
                input_data = pd.DataFrame([{
                    'idade_unificada': idade,
                    'genero': gen_enc,
                    'bolsa': bolsa_enc,
                    'ida': ida,
                    'ieg': ieg,
                    'iaa': iaa,
                    'ips': ips,
                    'ipp': ipp,
                    'ipv': ipv,
                    'delta_ida': delta_ida,
                    'delta_ieg': delta_ieg,
                    'delta_ips': delta_ips
                }])
                
                probabilidade = xgb_model.predict_proba(input_data)[0][1] * 100
                classe = xgb_model.predict(input_data)[0]
                
                st.markdown("---")
                st.markdown("## 🎯 Diagnóstico da A.I.")
                
                if classe == 1 or probabilidade > 50:
                    st.error(f"⚠️ **RISCO ALTO DE DEFASAGEM** ({probabilidade:.1f}%)")
                    st.markdown(f"O modelo de Machine Learning identificou padrões severos de risco. O impacto cascata nas avaliações recentes ou no estado emocional sugere que esse aluno deve ser encaminhado para **Tutoria e Acompanhamento Psicológico Imediato**.")
                else:
                    st.success(f"✅ **BOM PROGNÓSTICO** ({probabilidade:.1f}% de risco apenas)")
                    st.markdown("O aluno apresenta base emocional e engajamento suficientes para manter a adequação educacional sem defasagem profunda no método atual.")
            except Exception as e:
                st.error(f"Erro ao processar predição: {e}")
