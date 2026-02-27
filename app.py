import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go

# -----------------
# CONFIGURAÇÃO DE PAGINA
# -----------------
st.set_page_config(page_title="Passos Mágicos | Datathon", page_icon="✨", layout="wide", initial_sidebar_state="expanded")

ROXO_PM = "#8257E5"
NEON_GREEN = "#50fa7b"
NEON_BLUE = "#8be9fd"
NEON_PINK = "#ff79c6"
NEON_ORANGE = "#ffb86c"
BG_COLOR = "#0d1117"
TEXT_COLOR = "#ffffff"

st.markdown(f"""
    <style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stApp {{ background-color: {BG_COLOR}; color: {TEXT_COLOR}; }}
    h1, h2, h3, h4, h5, h6, p, span, div {{ color: {TEXT_COLOR}; font-family: 'Inter', sans-serif; }}
    [data-testid="stSidebar"] {{ background-color: #161b22; }}
    div.stInfo {{ background-color: rgba(130, 87, 229, 0.1) !important; color: {TEXT_COLOR} !important; border-left-color: {ROXO_PM} !important; }}
    .stButton>button {{ background-color: {ROXO_PM}; color: {TEXT_COLOR}; border-radius: 8px; border: none; padding: 10px 24px; font-weight: bold; transition: all 0.3s; }}
    .stButton>button:hover {{ background-color: #996bf5; box-shadow: 0 0 10px rgba(130,87,229,0.5); }}
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def carregar_dados():
    df = pd.read_csv('dados_limpos_pm.csv')
    return df

@st.cache_resource
def carregar_modelo():
    try:
        with open('modelo_risco.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

df = carregar_dados()
modelo_dict = carregar_modelo()

def apply_plotly_layout(fig):
    fig.update_layout(
        plot_bgcolor=BG_COLOR,
        paper_bgcolor=BG_COLOR,
        font=dict(color=TEXT_COLOR),
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5, font=dict(color=TEXT_COLOR))
    )
    fig.update_xaxes(showgrid=False, color=TEXT_COLOR, tickfont=dict(color=TEXT_COLOR))
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)', color=TEXT_COLOR, tickfont=dict(color=TEXT_COLOR))
    return fig

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
      <text x="80" y="65" font-family="'Segoe UI', Arial, sans-serif" font-weight="900" font-style="italic" font-size="52" fill="#ffffff">PASSOS</text>
      <text x="85" y="115" font-family="'Segoe UI', Arial, sans-serif" font-weight="900" font-style="italic" font-size="52" fill="#ffffff">MÁGICOS</text>
      <path d="M 160,80 L 163,86 L 170,86 L 165,90 L 167,97 L 160,93 L 153,97 L 155,90 L 150,86 L 157,86 Z" fill="#8257E5"/>
    </svg>
    """
    st.markdown(svg_logo, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🧭 Menu de Navegação")
    menu = st.radio("", ["🏠 Conheça o Projeto", "📊 Análise de Dados", "🔍 Predição de Risco"])
    
    st.markdown("---")
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
    st.markdown(
        "<div style='color: #ffffff; font-size: 13px; text-align: center; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1);'>"
        "Transformação Educacional<br><b>Passos Mágicos - Fase 5 FIAP</b></div>", 
        unsafe_allow_html=True
    )

if menu == "🏠 Conheça o Projeto":
    st.title("Conheça o Projeto")
    st.markdown("### A Associação Passos Mágicos")
    st.markdown('''
A Associação Passos Mágicos tem uma trajetória de 33 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.

A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.

Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.
    ''')
    st.markdown("---")
    st.markdown("### 🤝 A Parceria Educacional")
    st.markdown('''
**Nosso Projeto**  
Como uma consultoria de dados especializada, fomos convidados a atuar junto à Passos Mágicos durante o desafio final (Datathon - Fase 5) da FIAP. Nosso objetivo principal é aplicar técnicas avançadas de Analytics não apenas para visualizar o passado, mas para iluminar o futuro através de modelos inteligentes, ajudando a escalar a nobre missão da Associação.

**O que tentamos responder?**  
O grande desafio de negócio que abraçamos foi mapear a fundo a jornada dos alunos: descobrir perfis de defasagem, comprovar matematicamente o impacto de ferramentas como bolsas de estudo e apoio psicológico, além de consolidar a efetividade do modelo educacional.

**Quais dados utilizamos?**  
Nossas análises mergulham no rico *dataset* histórico da ONG (anos de 2022 a 2024). Essa base nos forneceu as peças do quebra-cabeça: Indicadores de Desempenho Acadêmico (IDA), Engajamento (IEG), fatores Psicossociais (IPS) e avaliações Psicopedagógicas (IPP) de cada estudante assistido.

**Por Que Machine Learning?**  
Olhar para o passado é fundamental, mas prever o amanhã é transformador. Construímos e otimizamos uma Inteligência Artificial Preditiva (baseada em *XGBoost*) que aprende com esse vasto histórico para atuar como um **Sistema de Alerta Precoce**. O nosso modelo prediz a probabilidade matemática de um aluno entrar em risco grave, entregando aos educadores e psicólogos o poder de agir proativamente antes que o rendimento do aluno caia vertiginosamente.
    ''')

elif menu == "📊 Análise de Dados":
    st.title("Análise de Dados")
    st.markdown("Acompanhe as principais descobertas extraídas dos indicadores educacionais e psicológicos (2022-2024).")
    
    # helper UI
    def insight_card(titulo, texto):
        st.markdown(f"""
        <div style='background-color: rgba(130, 87, 229, 0.1); border-left: 4px solid {NEON_BLUE}; padding: 15px; border-radius: 5px; margin-top: 15px; margin-bottom: 30px;'>
            <h4 style='color: {NEON_BLUE}; margin-top: 0;'>{titulo}</h4>
            <p style='color: #ffffff; margin-bottom: 0;'>{texto}</p>
        </div>
        """, unsafe_allow_html=True)

    # 1. IAN
    st.markdown("### 1. Evolução da Defasagem (IAN)")
    df['defasagem_cat'] = pd.cut(df['ian'], bins=[-1, 5, 6.9, 10], labels=["Severo", "Moderado", "Adequado"])
    df_ian = df.groupby(['ano', 'defasagem_cat']).size().reset_index(name='count')
    df_ian['percent'] = df_ian.groupby('ano')['count'].transform(lambda x: x / x.sum() * 100)
    
    fig1 = px.bar(df_ian, x='ano', y='percent', color='defasagem_cat', text=df_ian['percent'].apply(lambda x: f'{x:.1f}%'),
                  color_discrete_map={"Adequado": NEON_GREEN, "Moderado": NEON_ORANGE, "Severo": NEON_PINK}, barmode='group')
    fig1.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1)
    st.plotly_chart(apply_plotly_layout(fig1), use_container_width=True)
    insight_card("1. Adequação do nível (IAN): Qual é o perfil geral de defasagem dos alunos e como ele evolui ao longo do ano?", 
                 "O programa tem sucesso em combater o risco educacional severo. Ao longo da série histórica, nota-se uma tendência positiva onde, a cada ano, os alunos consolidam sua jornada rumo à adequação de nível, comprovando a efetividade das práticas pedagógicas ao nivelar a aprendizagem.")

    # 2. IDA
    st.markdown("### 2. Desempenho Acadêmico (IDA)")
    df_ida = df.groupby('ano')['ida'].mean().reset_index()
    fig2 = px.line(df_ida, x='ano', y='ida', text=df_ida['ida'].apply(lambda x: f'{x:.2f}'), markers=True)
    fig2.update_traces(textposition='top center', line=dict(color=ROXO_PM, width=4), marker=dict(size=10, color=NEON_BLUE))
    fig2.update_layout(yaxis_range=[0, 10])
    st.plotly_chart(apply_plotly_layout(fig2), use_container_width=True)
    insight_card("2. Desempenho acadêmico (IDA): O desempenho acadêmico médio está melhorando, estagnado ou caindo?",
                 "O indicador acadêmico demonstra uma curva que acompanha a recuperação e nivelamento dos alunos subindo consistentemente. O programa não apenas tira o aluno do risco na base, mas garante a manutenção do desempenho quando o nível de cobrança e complexidade escolar aumenta.")

    # 3. IEG
    st.markdown("### 3. Engajamento nas Atividades (IEG)")
    df['ieg_nivel'] = pd.cut(df['ieg'], bins=[-1, 5.9, 7.9, 10], labels=['Baixo', 'Médio', 'Alto'])
    df_ieg_medias = df.groupby('ieg_nivel')[['ida', 'ipv']].mean().reset_index()
    fig3 = px.bar(df_ieg_medias, x='ieg_nivel', y=['ida', 'ipv'], text_auto='.2f', barmode='group',
                  color_discrete_sequence=[ROXO_PM, NEON_ORANGE])
    fig3.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1)
    st.plotly_chart(apply_plotly_layout(fig3), use_container_width=True)
    insight_card("3. Engajamento (IEG): O grau de engajamento tem relação direta com o desempenho (IDA) e o ponto de virada (IPV)?",
                 "O engajamento é a bússola e a alavanca principal do sucesso dentro do projeto! Promover campanhas, metodologias ativas e gamificação para garantir que o aluno mantenha alta presença e entrega de tarefas garante automaticamente notas (IDA) elevadas e impulsiona o Ponto de Virada.")

    # 4. IAA
    st.markdown("### 4. Autoavaliação vs Vida Real (IAA x IDA)")
    fig4 = px.scatter(df, x='ida', y='iaa', color='ieg_nivel', opacity=0.7, 
                      color_discrete_map={"Alto": NEON_GREEN, "Médio": ROXO_PM, "Baixo": NEON_PINK})
    fig4.add_shape(type="line", x0=0, y0=0, x1=10, y1=10, line=dict(color="gray", dash="dash"))
    st.plotly_chart(apply_plotly_layout(fig4), use_container_width=True)
    insight_card("4. Autoavaliação (IAA): As percepções dos alunos sobre si mesmos são coerentes com seu desempenho real (IDA)?",
                 "Existe um 'Gap de Otimismo' nos alunos. Ao comparar os dados, nota-se que a Autoavaliação (IAA) tende a ser superior ao desempenho acadêmico real. As estratégias de tutoria devem focar em feedbacks mais frequentes para alinhar a percepção do aluno à realidade acadêmica.")

    # 5. IPS
    st.markdown("### 5. Aspectos Psicossociais (IPS)")
    df['ips_trend'] = np.where(df['delta_ips'] < 0, 'Queda de IPS', 'Estável/Alta de IPS')
    df_ips = df.groupby('ips_trend')[['delta_ida', 'delta_ieg']].mean().reset_index()
    fig5 = px.bar(df_ips, x='ips_trend', y=['delta_ida', 'delta_ieg'], barmode='group', text_auto='.2f',
                  color_discrete_sequence=[NEON_BLUE, NEON_PINK])
    fig5.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1)
    st.plotly_chart(apply_plotly_layout(fig5), use_container_width=True)
    insight_card("5. Aspectos psicossociais (IPS): Há padrões psicossociais que antecedem quedas de desempenho acadêmico?",
                 "Sim! Oscilações no bem-estar psicossocial (IPS) estão conectadas ao aprendizado de forma antecipada. Alunos com o IPS em Queda apresentam variações negativas no desempenho. O monitoramento do IPS alerta para uma atuação preventiva crucial.")

    # 6. IPP
    st.markdown("### 6. Psicopedagógico vs Defasagem (IPP x IAN)")
    df_ipp = df.groupby('defasagem_cat')['ipp'].mean().reset_index()
    fig6 = px.bar(df_ipp, x='defasagem_cat', y='ipp', text_auto='.2f', color='defasagem_cat',
                  color_discrete_map={"Adequado": NEON_GREEN, "Moderado": NEON_ORANGE, "Severo": NEON_PINK})
    fig6.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1)
    st.plotly_chart(apply_plotly_layout(fig6), use_container_width=True)
    insight_card("6. Aspectos psicopedagógicos (IPP): As avaliações dos professores (IPP) confirmam a defasagem matemática do IAN?",
                 "Há convergência clara e direta! Alunos que o sistema classifica com defasagem Severa pela idade também recebem as menores notas na avaliação técnica (IPP). Isso prova que a defasagem identificada pela idade reflete dificuldades pedagógicas reais.")

    # 7. IPV
    st.markdown("### 7. Comportamentos do Ponto de Virada (IPV)")
    df['ipv_cat'] = np.where(df['ipv'] >= 7, 'Virou a Chave', 'Em Desenvolvimento')
    df_ipv = df.groupby('ipv_cat')[['ieg', 'ipp', 'ips']].mean().reset_index().melt(id_vars='ipv_cat')
    fig7 = px.bar(df_ipv, x='variable', y='value', color='ipv_cat', barmode='group', text_auto='.2f',
                  color_discrete_sequence=[ROXO_PM, NEON_GREEN])
    fig7.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1)
    st.plotly_chart(apply_plotly_layout(fig7), use_container_width=True)
    insight_card("7. Ponto de virada (IPV): Quais comportamentos mais influenciam o IPV ao longo do tempo?",
                 "A chave é multidisciplinar! A correlação reforça que indicadores atitudinais e emocionais (Engajamento e Psicopedagógico) lideram a influência. Alunos que viram a chave possuem médias extraordinárias e homogêneas em disciplina e estabilidade emocional.")

    # 8. GÊNERO
    st.markdown("### 8. Análise de Gênero")
    df_gen = df.groupby('genero')[['inde', 'ida', 'ieg', 'ips']].mean().reset_index().melt(id_vars='genero')
    fig8 = px.line(df_gen, x='variable', y='value', color='genero', markers=True, text='value')
    fig8.update_traces(texttemplate='%{text:.2f}', textposition='top center', line=dict(width=3))
    st.plotly_chart(apply_plotly_layout(fig8), use_container_width=True)
    insight_card("8. Há distinções significativas de performance e impacto entre Meninos e Meninas?",
                 "A equidade tem sido uma marca presente. O modelo da Passos Mágicos prova ser inclusivo para todos os gêneros, com patamares muito aproximados. Pequenas diferenças observadas no IPS balizam apenas atividades para fortalecer a autoestima sem comprometer resultados.")

    # 9. IDADE
    st.markdown("### 9. Impacto da Idade de Ingresso")
    df['idade_faixa'] = pd.cut(df['idade_unificada'], bins=[0, 10, 14, 25], labels=['Até 10 anos', '11 a 14 anos', '15+ anos'])
    df_idade = df.groupby('idade_faixa')['inde'].mean().reset_index()
    fig9 = px.bar(df_idade, x='idade_faixa', y='inde', text_auto='.2f', color='idade_faixa',
                  color_discrete_sequence=[NEON_GREEN, NEON_BLUE, NEON_PINK])
    fig9.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1)
    fig9.update_layout(yaxis_range=[0, 10])
    st.plotly_chart(apply_plotly_layout(fig9), use_container_width=True)
    insight_card("9. Ingressar cedo na Passos Mágicos altera a rota educacional do jovem a longo prazo?",
                 "Geralmente, alunos mais novos ('Até 10 anos') têm uma curva de adaptação mais fácil e demonstram médias de INDE mais robustas. A recomendação estratégica é priorizar o ingresso nas faixas iniciais do ensino fundamental, minimizando defasagens passadas.")

    # 10. BOLSA
    st.markdown("### 10. Efeito 'Bolsa de Estudos'")
    df_bolsa = df.groupby('bolsa')[['ida', 'inde']].mean().reset_index().melt(id_vars='bolsa')
    fig10 = px.bar(df_bolsa, x='variable', y='value', color='bolsa', barmode='group', text_auto='.2f',
                   color_discrete_sequence=[ROXO_PM, NEON_GREEN])
    fig10.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1)
    st.plotly_chart(apply_plotly_layout(fig10), use_container_width=True)
    insight_card("10. Qual a alavanca de impacto ao garantir Bolsas de Estudo em escolas parceiras?",
                 "As bolsas de estudo funcionam como catalisador supremo. O ambiente de uma escola privada aliada ao apoio da ONG gera um duplo motor de desenvolvimento, resultando nos maiores índices atingidos. Ampliar essa aliança é o grande diferencial de alavancagem.")

    # 11. GERAL
    st.markdown("### 11. Efetividade Geral do Programa (2022-2024)")
    df_all = df.groupby('ano')[['ida', 'ieg', 'ips', 'ipp', 'inde']].mean().reset_index().melt(id_vars='ano')
    fig11 = px.line(df_all, x='ano', y='value', color='variable', markers=True, text='value')
    fig11.update_traces(texttemplate='%{text:.1f}', textposition='top center', line=dict(width=4))
    fig11.update_xaxes(tickvals=[2022, 2023, 2024])
    st.plotly_chart(apply_plotly_layout(fig11), use_container_width=True)
    insight_card("11. Efetividade do programa: Os indicadores mostram melhora consistente ao longo do ciclo (2022 a 2024)?",
                 "Sim! Acompanhando a linha do tempo encontramos o amadurecimento incontestável do projeto. A Passos Mágicos foi desafiada nos anos analisados a absorver dezenas de alunos novos com déficits, e mesmo assim manteve a curva do programa ascendente.")


elif menu == "🔍 Predição de Risco":
    st.title("Sistema de Alerta Precoce")
    st.markdown("Utilize o modelo de **Inteligência Artificial (XGBoost Otimizado)** para prever a probabilidade matemática de um aluno entrar em risco grave de defasagem acadêmica no próximo período.")
    
    if modelo_dict is None:
        st.error("O modelo Preditivo ('modelo_risco.pkl') não foi encontrado.")
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
                delta_ida = st.number_input("Variação (IDA) em relação ao último ano", min_value=-10.0, max_value=10.0, value=0.0)
            with n2:
                ieg = st.slider("Engajamento p/ Tarefas (IEG)", 0.0, 10.0, 7.5, 0.1)
                delta_ieg = st.number_input("Variação (IEG)", min_value=-10.0, max_value=10.0, value=0.0)
            with n3:
                ips = st.slider("Bem Estar Psicossocial (IPS)", 0.0, 10.0, 8.0, 0.1)
                delta_ips = st.number_input("Variação Emocional (IPS)", min_value=-10.0, max_value=10.0, value=0.0)
            
            st.markdown("### 🧠 Avaliações Subjetivas (Professores e Conselhos)")
            o1, o2, o3 = st.columns(3)
            with o1:
                ipp = st.slider("Avaliação Psicopedagógica (IPP)", 0.0, 10.0, 7.0, 0.1)
            with o2:
                iaa = st.slider("Auto-avaliação do Aluno (IAA)", 0.0, 10.0, 8.0, 0.1)
            with o3:
                ipv = st.slider("Ponto de Virada (IPV)", 0.0, 10.0, 6.5, 0.1)
        
        if submit:
            try:
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
                    st.markdown(f"O modelo de Machine Learning identificou padrões severos de risco. O impacto cascata nas avaliações recentes sugere focar em Acompanhamento Imediato.")
                else:
                    st.success(f"✅ **BOM PROGNÓSTICO** ({probabilidade:.1f}% de risco apenas)")
                    st.markdown("O aluno apresenta base emocional e engajamento suficientes para manter a adequação educacional sem defasagem profunda.")
            except Exception as e:
                st.error(f"Erro ao processar predição: {e}")
