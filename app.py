import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
import time

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
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation="v", yanchor="top", y=1.0, xanchor="left", x=1.02, font=dict(color=TEXT_COLOR))
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
    st.markdown("### Perfil geral de defasagem (IAN)")
    
    insight_card("Qual é o perfil geral de defasagem dos alunos (IAN) e como ele evolui?", 
                 "Aqui vemos se o aluno está no nível certo para a idade. As barras mostram que o grupo Adequado cresceu de 2022 para 2024, enquanto os casos Severos diminuíram drasticamente. Isso prova que o nivelamento da Passos Mágicos está funcionando: estamos resgatando quem estava atrasado e acelerando o aprendizado desses jovens.")

    df['defasagem_cat'] = pd.cut(df['ian'], bins=[-1, 4.9, 6.9, 10], labels=["Severa (0 a 4.9)", "Moderada (5 a 6.9)", "Adequada (7 a 10)"])
    color_map_ian = {"Severa (0 a 4.9)": "#d0bfff", "Moderada (5 a 6.9)": "#a188e5", "Adequada (7 a 10)": "#8257E5"}
    
    col1, col2 = st.columns(2)
    
    with col1:
        df_ian_geral = df.groupby('defasagem_cat', observed=True).size().reset_index(name='count')
        fig1a = px.bar(df_ian_geral, x='defasagem_cat', y='count', text=df_ian_geral['count'].apply(lambda x: f'{x} alunos'),
                       color='defasagem_cat', color_discrete_map=color_map_ian)
        fig1a = apply_plotly_layout(fig1a)
        fig1a.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1, textfont=dict(color='#ffffff'))
        fig1a.update_layout(title="Perfil Geral de Defasagem (IAN)", showlegend=False, 
                            yaxis=dict(showgrid=False, showticklabels=False, title=""), 
                            xaxis=dict(title=""),
                            height=400)
        st.plotly_chart(fig1a, use_container_width=True)
        
    with col2:
        df_ian_ano = df.groupby(['ano', 'defasagem_cat'], observed=True).size().reset_index(name='count')
        df_ian_ano['percent'] = df_ian_ano.groupby('ano')['count'].transform(lambda x: x / x.sum() * 100)
        fig1b = px.bar(df_ian_ano, x='ano', y='percent', color='defasagem_cat', text=df_ian_ano['percent'].apply(lambda x: f'{x:.1f}%'),
                       color_discrete_map=color_map_ian, barmode='stack')
        fig1b = apply_plotly_layout(fig1b)
        fig1b.update_traces(textposition='inside', insidetextanchor='middle', marker_line_color='#ffffff', marker_line_width=1, textfont=dict(color='#ffffff'))
        fig1b.update_layout(title="Evolução do Perfil de Defasagem por Ano (%)", legend_title="", 
                            yaxis=dict(showgrid=False, showticklabels=False, title=""), 
                            xaxis=dict(title="", type='category'),
                            height=400)
        st.plotly_chart(fig1b, use_container_width=True)

    # 2. IDA
    st.markdown("### Desempenho acadêmico (IDA)")
    
    insight_card("O desempenho acadêmico médio (IDA) está melhorando, estagnado ou caindo ao longo dos anos e fases?",
                 "O IDA médio cresceu de 6,09 em 2022 para 6,67 em 2023, com leve ajuste para 6,35 em 2024 — ainda acima do ponto inicial. Por fase, a maioria avançou entre 2022 e 2023, com pequenas oscilações em 2024. O cenário geral é de evolução no desempenho, com estabilidade e consolidação dos resultados ao longo do tempo.")

    col3, col4 = st.columns(2)
    
    with col3:
        df_ida_ano = df.groupby('ano')['ida'].mean().reset_index()
        fig2a = px.bar(df_ida_ano, x='ano', y='ida', text=df_ida_ano['ida'].apply(lambda x: f'Nota {x:.2f}'),
                       color_discrete_sequence=[ROXO_PM])
        fig2a = apply_plotly_layout(fig2a)
        fig2a.update_traces(textposition='outside', marker_line_color='#ffffff', marker_line_width=1, textfont=dict(color='#ffffff', size=14, family="Arial Black"))
        fig2a.update_layout(title="Evolução do Desempenho Acadêmico (IDA Médio)",
                            yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, 10]), 
                            xaxis=dict(title="", type='category'),
                            height=400)
        st.plotly_chart(fig2a, use_container_width=True)
        
    with col4:
        df_tmp = df.copy()
        df_tmp['fase_nome'] = df_tmp['fase'].astype(str).apply(lambda x: 'Fase 0 (Alfa)' if x == '0' else f'Fase {x}')
        
        # Conta as top 6 fases gerais do projeto
        fases_populosas = df_tmp['fase'].value_counts().nlargest(6).index
        df_ida_fase = df_tmp[df_tmp['fase'].isin(fases_populosas)].groupby(['fase', 'fase_nome', 'ano'])['ida'].mean().reset_index()
        
        # Pivot garantindo a ordem crescente da fase
        df_ida_fase = df_ida_fase.sort_values(by=['fase', 'ano'])
        df_ida_pivot = df_ida_fase.pivot(index='fase_nome', columns='ano', values='ida')
        
        def safe_fase_int(x):
            if x == 'Fase 0 (Alfa)': return 0
            try:
                numeric_part = ''.join(filter(str.isdigit, str(x)))
                return int(numeric_part) if numeric_part else 999
            except:
                return 999
                
        sorted_fases = sorted(df_ida_pivot.index, key=safe_fase_int)
        df_ida_pivot = df_ida_pivot.reindex(sorted_fases)
        
        # Heatmap com Plotly Express
        fig2b = px.imshow(df_ida_pivot, text_auto=".2f", aspect="auto",
                          color_continuous_scale=["#3a286b", "#8257E5", "#a188e5"],
                          labels=dict(x="", y="", color="IDA"))
        fig2b = apply_plotly_layout(fig2b)
        fig2b.update_traces(xgap=2, ygap=2, textfont=dict(color='#ffffff'))
        fig2b.update_xaxes(side="bottom", type='category')
        fig2b.update_yaxes(autorange="reversed")
        fig2b.update_layout(title="Desempenho (IDA) nas Fases Mais Populosas",
                            coloraxis_showscale=False,
                            xaxis=dict(title=""),
                            yaxis=dict(title=""),
                            height=400)
        st.plotly_chart(fig2b, use_container_width=True)

    # 3. IEG
    st.markdown("### Impacto no engajamento")
    
    insight_card("Qual o impacto real do engajamento estudantil nos resultados?",
                 "A correlação entre Engajamento e Desempenho é positiva (0,54), assim como com o Ponto de Virada (0,56). Isso indica uma relação moderada: quanto maior o engajamento, melhores tendem a ser os resultados. Na prática, alunos com engajamento alto apresentam médias significativamente superiores em IDA e IPV. O dado confirma que engajar é um dos principais motores de evolução acadêmica no Passos Mágicos.")

    col5, col6 = st.columns(2)
    
    with col5:
        cols_corr = ['ieg', 'ida', 'ipv']
        corr_matrix = df[cols_corr].corr().round(2)
        corr_matrix.columns = ['Engajamento (IEG)', 'Desempenho (IDA)', 'Ponto de Virada (IPV)']
        corr_matrix.index = ['Engajamento (IEG)', 'Desempenho (IDA)', 'Ponto de Virada (IPV)']
        
        fig3a = px.imshow(corr_matrix, text_auto=".2f", aspect="auto",
                          color_continuous_scale=["#161b22", "#8257E5"],
                          labels=dict(x="", y="", color="Correlação"))
        fig3a = apply_plotly_layout(fig3a)
        fig3a.update_traces(xgap=2, ygap=2, textfont=dict(color='#ffffff'))
        fig3a.update_xaxes(side="bottom")
        fig3a.update_yaxes(autorange="reversed")
        fig3a.update_layout(title="Força da Relação (Correlação)", coloraxis_showscale=False, height=400)
        st.plotly_chart(fig3a, use_container_width=True)

    with col6:
        df['ieg_nivel_img'] = pd.cut(df['ieg'], bins=[-1, 5.9, 7.9, 10], labels=["Baixo (0 a 5.9)", "Médio (6 a 7.9)", "Alto (8 a 10)"])
        df_ieg_img = df.groupby('ieg_nivel_img', observed=True)[['ida', 'ipv']].mean().reset_index().melt(id_vars='ieg_nivel_img')
        df_ieg_img['variable'] = df_ieg_img['variable'].replace({'ida': 'Desempenho (IDA)', 'ipv': 'Ponto de Virada (IPV)'})
        
        fig3b = px.bar(df_ieg_img, x='ieg_nivel_img', y='value', color='variable', barmode='group', text='value',
                       color_discrete_sequence=['#a188e5', '#d0bfff'])
        fig3b = apply_plotly_layout(fig3b)
        fig3b.update_traces(texttemplate='%{text:.2f}', textposition='outside', marker_line_color='#ffffff', marker_line_width=1, textfont=dict(color='#ffffff'))
        fig3b.update_layout(title="Impacto do Engajamento (Média das Notas)", legend_title="",
                            yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, 10]), 
                            xaxis=dict(title=""), height=400)
        st.plotly_chart(fig3b, use_container_width=True)
    # 4. IAA
    st.markdown("### Autoavaliação e Gap de Percepção")
    
    insight_card("As percepções dos alunos sobre si mesmos são coerentes com seu desempenho real?",
                 "Em todos os anos, a autoavaliação (IAA) fica acima do desempenho real (IDA), indicando tendência de superestimação. A distribuição do gap confirma que a maioria dos alunos se avalia um pouco acima da própria nota. Ao mesmo tempo, o IAA se mantém mais próximo do nível de engajamento (IEG), que é consistentemente mais alto. Isso mostra que os alunos se percebem melhor do que performam, mas essa confiança está alinhada a um bom nível de engajamento — um ponto positivo para evolução futura.")

    col7, col8 = st.columns(2)
    
    with col7:
        df_gap_ano = df.groupby('ano')[['iaa', 'ida', 'ieg']].mean().reset_index().melt(id_vars='ano')
        df_gap_ano['variable'] = df_gap_ano['variable'].replace({
            'iaa': 'Autoavaliação (IAA)', 
            'ida': 'Desempenho (IDA)', 
            'ieg': 'Engajamento (IEG)'
        })
        fig4a = px.bar(df_gap_ano, x='ano', y='value', color='variable', barmode='group', text='value',
                       color_discrete_sequence=['#8257E5', '#a188e5', '#e0d6ff'])
        fig4a = apply_plotly_layout(fig4a)
        fig4a.update_traces(texttemplate='%{text:.2f}', textposition='outside', marker_line_color='#ffffff', marker_line_width=1, textfont=dict(color='#ffffff'))
        fig4a.update_layout(title="Autoavaliação vs. Desempenho e Engajamento", legend_title="",
                            yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, 11]), 
                            xaxis=dict(title="", type='category'), height=400)
        st.plotly_chart(fig4a, use_container_width=True)
        
    with col8:
        import scipy.stats as stats
        
        df_tmp = df.copy()
        df_tmp['gap'] = df_tmp['iaa'] - df_tmp['ida']
        
        fig4b = px.histogram(df_tmp, x='gap', nbins=30, color_discrete_sequence=['#b794f6'], opacity=0.9, histnorm='probability density')
        
        gap_drop = df_tmp['gap'].dropna()
        if len(gap_drop) > 1:
            kde = stats.gaussian_kde(gap_drop)
            x_kde = np.linspace(gap_drop.min(), gap_drop.max(), 100)
            fig4b.add_scatter(x=x_kde, y=kde(x_kde), mode='lines', line=dict(color='#8257E5', width=2), showlegend=False)

        fig4b = apply_plotly_layout(fig4b)
        fig4b.update_traces(marker_line_color=BG_COLOR, marker_line_width=1, selector=dict(type='histogram'))
        fig4b.update_layout(title="Distribuição do Gap de Percepção (IAA - IDA)", showlegend=False,
                            yaxis=dict(showgrid=False, showticklabels=False, title=""), 
                            xaxis=dict(title="Diferença (Notas)", showgrid=False),
                            height=400)
        
        fig4b.add_vline(x=0, line_dash="dash", line_color="white", line_width=2)
        fig4b.add_annotation(x=-0.5, y=0.85, yref="paper", text="← Subestima-se", showarrow=False, font=dict(color="#ffffff", size=14), xanchor="right")
        fig4b.add_annotation(x=0.5, y=0.85, yref="paper", text="Superestima-se →", showarrow=False, font=dict(color="#ffffff", size=14), xanchor="left")
        
        st.plotly_chart(fig4b, use_container_width=True)

    # 5. IPS
    st.markdown("### Aspectos Psicossociais (IPS)")
    
    insight_card("Qual o impacto das variações psicossociais no rendimento e engajamento?",
                 "As correlações entre variação psicossocial (ΔIPS) e variação de desempenho (ΔIDA) e engajamento (ΔIEG) são fracas e levemente negativas (-0,10 e -0,20). Isso indica que não há uma relação forte e direta. No entanto, alunos com IPS em queda apresentam reduções maiores em desempenho e engajamento. Ou seja, o IPS não explica tudo, mas sua queda funciona como sinal de alerta para possíveis perdas acadêmicas.")

    col9, col10 = st.columns(2)
    
    with col9:
        cols_corr_delta = ['delta_ips', 'delta_ida', 'delta_ieg']
        corr_delta = df[cols_corr_delta].corr().round(2)
        
        labels_delta = ['Variação Psicossocial<br>(Δ IPS)', 'Variação Desempenho<br>(Δ IDA)', 'Variação Engajamento<br>(Δ IEG)']
        corr_delta.columns = labels_delta
        corr_delta.index = labels_delta
        
        fig5a = px.imshow(corr_delta, text_auto=".2f", aspect="auto",
                          color_continuous_scale=["#f3f0ff", "#a188e5", "#8257E5"],
                          labels=dict(x="", y="", color="Correlação"))
        fig5a = apply_plotly_layout(fig5a)
        fig5a.update_traces(xgap=2, ygap=2, textfont=dict(color='#000000', size=14, family="Arial Black"))
        fig5a.update_xaxes(side="bottom")
        fig5a.update_yaxes(autorange="reversed")
        fig5a.update_layout(title="P5. Força da Relação entre Variações (Deltas)", coloraxis_showscale=False, height=400)
        st.plotly_chart(fig5a, use_container_width=True)

    with col10:
        df['ips_trend'] = np.where(df['delta_ips'] < 0, 'IPS em Queda', 'IPS Estável/Subindo')
        df_ips = df.groupby('ips_trend')[['delta_ida', 'delta_ieg']].mean().reset_index().melt(id_vars='ips_trend')
        df_ips['variable'] = df_ips['variable'].replace({'delta_ida': 'Variação IDA', 'delta_ieg': 'Variação IEG'})
        
        fig5b = px.bar(df_ips, x='variable', y='value', color='ips_trend', barmode='group', text='value',
                       color_discrete_sequence=['#8257E5', '#d0bfff'])
        fig5b = apply_plotly_layout(fig5b)
        fig5b.update_traces(texttemplate='%{text:.2f}', textposition='outside', marker_line_color=BG_COLOR, marker_line_width=1, textfont=dict(color='#8257E5', size=13, family="Arial Black"))
        
        y_min = df_ips['value'].min() * 1.2
        fig5b.update_layout(title="Impacto do Comportamento do IPS no Desempenho", 
                            legend_title="",
                            legend=dict(orientation="v", yanchor="bottom", y=0.0, xanchor="left", x=0.0, font=dict(color=TEXT_COLOR)),
                            yaxis=dict(showgrid=False, showticklabels=False, title="", range=[y_min, 0]), 
                            xaxis=dict(title=""), height=400)
        st.plotly_chart(fig5b, use_container_width=True)

    # 6. IPP
    st.markdown("### Avaliação Psicopedagógica (IPP) por Nível de Defasagem (IAN)")
    
    insight_card("As avaliações dos professores (IPP) confirmam a defasagem matemática do IAN?",
                 "Aqui mostramos que os indicadores estão em total sintonia. As barras revelam que, conforme o nível de defasagem (IAN) melhora, a média da avaliação psicopedagógica (IPP) também sobe — saindo de 6,95 no nível Severo para 7,68 no Adequado. Isso confirma que o IAN é um termômetro preciso: o aluno que está na idade certa para a série também demonstra um desempenho de aprendizagem superior. Essa validação entre os dados nos dá segurança de que estamos diagnosticando e tratando as dificuldades dos jovens com exatidão.")

    df_ipp = df.groupby('defasagem_cat')['ipp'].mean().reset_index()
    df_ipp['defasagem_cat'] = df_ipp['defasagem_cat'].replace({
        'Severo': 'Severa (0 a 4.9)',
        'Moderado': 'Moderada (5 a 6.9)',
        'Adequado': 'Adequada (7 a 10)'
    })
    
    # Sort strictly Severa -> Moderada -> Adequada
    cat_order = ['Severa (0 a 4.9)', 'Moderada (5 a 6.9)', 'Adequada (7 a 10)']
    df_ipp['defasagem_cat'] = pd.Categorical(df_ipp['defasagem_cat'], categories=cat_order, ordered=True)
    df_ipp = df_ipp.sort_values('defasagem_cat')

    fig6 = px.bar(df_ipp, x='defasagem_cat', y='ipp', text='ipp', color_discrete_sequence=['#8257E5'])
    fig6 = apply_plotly_layout(fig6)
    
    fig6.update_traces(texttemplate='Média IPP: %{text:.2f}', textposition='outside', 
                       marker_line_color=BG_COLOR, marker_line_width=1, 
                       textfont=dict(color='#FFFFFF', size=14, family="Arial Black"))
    
    fig6.update_layout(title="Avaliação Psicopedagógica (IPP) por nível de defasagem (IAN)", showlegend=False,
                       yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, 10]), 
                       xaxis=dict(title=""), height=400)
    
    st.plotly_chart(fig6, use_container_width=True)

    # 7. IPV
    st.markdown("### Ponto de Virada")
    
    insight_card("Quais comportamentos mais impulsionam o Ponto de Virada ao longo do tempo?",
                 "O 'ponto de virada' é o momento em que o aluno assume o protagonismo de sua jornada. Os dados revelam que os grandes motores dessa transformação são o Desempenho Acadêmico (IPP) e o Engajamento (IEG). Com uma forte correlação de 0,61 e 0,56, respectivamente, vemos que o aluno que 'vira a chave' é aquele que está presente, participa e colhe resultados no aprendizado. Note a diferença clara nas médias: quem atingiu o ponto de virada saltou para 8,66 em engajamento e 7,81 em pedagogia. Por outro lado, o fator psicossocial (IPS) se mantém estável em ambos os grupos, o que nos mostra que a virada de chave acontece, primordialmente, através da dedicação aos estudos e da constância nas atividades. Isso valida nossa estratégia de incentivar a presença e o esforço contínuo como o caminho mais curto para a transformação de vida.")

    col11, col12 = st.columns(2)
    
    with col11:
        corr_ipv = df[['ipp', 'ieg', 'ips', 'ipv']].corr()[['ipv']].drop('ipv').round(2)
        corr_ipv.index = ['Psicopedag.', 'Engajamento', 'Psicossocial']
        
        fig7a = px.imshow(corr_ipv, text_auto=".2f", aspect="auto",
                          color_continuous_scale=["#f3f0ff", "#a188e5", "#8257E5"],
                          labels=dict(x="", y="", color="Correlação"))
        fig7a = apply_plotly_layout(fig7a)
        fig7a.update_traces(xgap=2, ygap=2, textfont=dict(color='#000000', size=14, family="Arial Black"))
        fig7a.update_xaxes(showticklabels=False, title="Ponto de<br>Virada")
        fig7a.update_layout(title="Fatores que Impulsionam o Ponto de Virada - Correlação (Pearson)", coloraxis_showscale=False, height=400)
        st.plotly_chart(fig7a, use_container_width=True)
        
    with col12:
        df_tmp = df.copy()
        df_tmp['ipv_cat'] = np.where(df_tmp['ipv'] >= 7, 'Virou a Chave', 'Em Evolução')
        
        # Calculate exactly IPP, IEG, IPS means.
        df_ipv = df_tmp.groupby('ipv_cat')[['ieg', 'ips', 'ipp']].mean().reset_index().melt(id_vars='ipv_cat')
        
        # Sort categorical logic for 'Em Evolução' first, then 'Virou a Chave'
        cat_order_ipv = ['Em Evolução', 'Virou a Chave']
        df_ipv['ipv_cat'] = pd.Categorical(df_ipv['ipv_cat'], categories=cat_order_ipv, ordered=True)
        df_ipv = df_ipv.sort_values('ipv_cat')

        fig7b = px.bar(df_ipv, x='variable', y='value', color='ipv_cat', barmode='group', text='value',
                       color_discrete_sequence=['#8257E5', '#d0bfff'])
        fig7b = apply_plotly_layout(fig7b)
        fig7b.update_traces(texttemplate='%{text:.2f}', textposition='outside', marker_line_color=BG_COLOR, marker_line_width=1, textfont=dict(color='#FFFFFF', size=13, family="Arial Black"))
        
        y_max = df_ipv['value'].max() * 1.2
        fig7b.update_layout(title="Média dos Indicadores por Status de Virada", 
                            legend_title="",
                            legend=dict(orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5, font=dict(color=TEXT_COLOR)),
                            yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, y_max]), 
                            xaxis=dict(title=""), height=400)
        st.plotly_chart(fig7b, use_container_width=True)

    # 8. GÊNERO
    st.markdown("### Indicadores de Gênero")
    
    insight_card("Há distinções significativas de performance e impacto entre Meninos e Meninas?",
                 "Os dados revelam um cenário de equilíbrio e equidade: não há disparidade entre meninos e meninas. As médias de Engajamento (IEG) e Desempenho (IDA) são quase idênticas. Meninas têm engajamento de 8,32 (contra 8,13 dos meninos), e no desempenho a diferença é mínima (6,40 vs 6,35). Essa consistência prova que a metodologia da Passos Mágicos é universal. O gênero não determina o sucesso; com as mesmas oportunidades, ambos os grupos atingem altos níveis de dedicação e aprendizado de forma equivalente.")

    df_gen = df.groupby('genero')[['ida', 'ieg', 'ips']].mean().reset_index().melt(id_vars='genero')
    df_gen['genero'] = df_gen['genero'].replace({'F': 'Feminino', 'M': 'Masculino'})
    
    # Sort categories inside gender as Feminino -> Masculino
    cat_order_gen = ['Feminino', 'Masculino']
    df_gen['genero'] = pd.Categorical(df_gen['genero'], categories=cat_order_gen, ordered=True)
    df_gen = df_gen.sort_values('genero')

    fig8 = px.bar(df_gen, x='variable', y='value', color='genero', barmode='group', text='value',
                  color_discrete_sequence=['#8257E5', '#d0bfff'])
    fig8 = apply_plotly_layout(fig8)
    fig8.update_traces(texttemplate='%{text:.2f}', textposition='outside', marker_line_color=BG_COLOR, marker_line_width=1, textfont=dict(color='#FFFFFF', size=14, family="Arial Black"))
    
    y_max_gen = df_gen['value'].max() * 1.2
    fig8.update_layout(title="Comparativo de Indicadores por Gênero", 
                       legend_title="",
                       legend=dict(orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5, font=dict(color=TEXT_COLOR)),
                       yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, y_max_gen]), 
                       xaxis=dict(title=""), height=400)
    st.plotly_chart(fig8, use_container_width=True)

    # 9. IDADE
    st.markdown("### Impacto da Idade no Desempenho Geral")
    
    insight_card("Ingressar cedo na Passos Mágicos altera a rota educacional do jovem a longo prazo?",
                 "A intervenção precoce é um diferencial claro. Alunos que entram com até 10 anos têm o melhor desempenho (7,55), enquanto quem ingressa aos 16+ anos atinge a média mais baixa (6,69). Essa queda gradual prova que quanto antes o jovem começa, mais sólida é sua evolução. Iniciar cedo garante tempo para consolidar o aprendizado e atingir resultados superiores ao longo da jornada na Passos Mágicos.")

    df_tmp2 = df.copy()
    df_tmp2['idade_faixa'] = pd.cut(df_tmp2['idade_unificada'], bins=[0, 10, 13, 15, 50], 
                                   labels=['Até 10 anos', '11 a 13 anos', '14 a 15 anos', '16+ anos'])
    
    # Calculate means and append a tiny 'error' column to draw the T-ticks manually via Plotly
    df_idade = df_tmp2.groupby('idade_faixa')['inde'].mean().reset_index()
    df_idade['e_plus'] = 0.15
    df_idade['e_minus'] = 0.0
    
    color_map_idade = {
        'Até 10 anos': '#a38ada', 
        '11 a 13 anos': '#b4a0e3', 
        '14 a 15 anos': '#c5b6ec', 
        '16+ anos': '#d5ccf5'
    }

    fig9 = px.bar(df_idade, x='idade_faixa', y='inde', text='inde', color='idade_faixa', 
                  color_discrete_map=color_map_idade,
                  error_y='e_plus', error_y_minus='e_minus')
    
    fig9 = apply_plotly_layout(fig9)
    fig9.update_traces(texttemplate='%{text:.2f}', textposition='outside', 
                       error_y=dict(color='#333333', thickness=2, width=4),
                       marker_line_color=BG_COLOR, marker_line_width=1, 
                       textfont=dict(color='#FFFFFF', size=14, family="Arial Black"))
    
    y_max_idade = df_idade['inde'].max() * 1.2
    
    fig9.update_layout(title="P9. Impacto da Idade de Ingresso no Desempenho Geral (INDE Médio)", 
                       showlegend=False,
                       yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, y_max_idade]), 
                       xaxis=dict(title=dict(text="Faixa Etária de Ingresso", font=dict(color=TEXT_COLOR, size=14, family="Arial Black"))), 
                       height=400)
    st.plotly_chart(fig9, use_container_width=True)

    # 10. BOLSA
    st.markdown("### Efeito 'Bolsa de Estudos'")

    insight_card("Qual a alavanca de impacto ao garantir Bolsas de Estudo em escolas parceiras?",
                 "A bolsa atua como um potente catalisador de resultados. Os dados mostram que bolsistas superam os não bolsistas em todos os indicadores, registrando médias superiores tanto no IDA (6,93 vs 6,32) quanto no INDE (7,73 vs 7,22). Isso demonstra que o suporte e o reconhecimento direto fortalecem o compromisso do aluno. O incentivo transforma o potencial em desempenho real, elevando o patamar de aproveitamento educacional dos jovens dentro do projeto.")

    df_bolsa_temp = df.copy()
    # Handle 'Sim' vs everything else ('Não' with potential encoding issues)
    df_bolsa_temp['bolsa_str'] = df_bolsa_temp['bolsa'].apply(lambda x: 'Bolsista' if str(x).strip().lower() == 'sim' else 'Não Bolsista')
    
    # Calculate means for 'ida', 'inde', 'ieg' grouped by 'bolsa_str'
    df_bolsa = df_bolsa_temp.groupby('bolsa_str')[['ida', 'inde', 'ieg']].mean().reset_index().melt(id_vars='bolsa_str')
    
    # Ensure correct category ordering inside grouped chart
    cat_order_bolsa = ['Bolsista', 'Não Bolsista']
    df_bolsa['bolsa_str'] = pd.Categorical(df_bolsa['bolsa_str'], categories=cat_order_bolsa, ordered=True)
    df_bolsa = df_bolsa.sort_values('bolsa_str')

    fig10 = px.bar(df_bolsa, x='variable', y='value', color='bolsa_str', barmode='group', text='value',
                   color_discrete_sequence=['#8257E5', '#d0bfff'])
    
    fig10 = apply_plotly_layout(fig10)
    fig10.update_traces(texttemplate='%{text:.2f}', textposition='outside', 
                        marker_line_color=BG_COLOR, marker_line_width=1, 
                        textfont=dict(color='#FFFFFF', size=14, family="Arial Black"))
    
    y_max_bolsa = df_bolsa['value'].max() * 1.2
    fig10.update_layout(title="P10. Comparativo de Performance: Bolsistas vs. Não Bolsistas", 
                        legend_title="",
                        legend=dict(orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5, font=dict(color=TEXT_COLOR)),
                        yaxis=dict(showgrid=False, showticklabels=False, title="", range=[0, y_max_bolsa]), 
                        xaxis=dict(title=""), height=400)
    
    st.plotly_chart(fig10, use_container_width=True)

    # 11. GERAL
    st.markdown("### Efetividade Geral do Programa")
    
    insight_card("Efetividade do programa: Os indicadores mostram melhora consistente ao longo do ciclo?",
                 "Os indicadores demonstram maturidade e crescimento constante ao longo dos anos. O Engajamento (IEG) mantém-se como o índice mais alto, atingindo 8,09, enquanto o Índice Geral (INDE) e o Pedagógico (IPP) apresentam evolução sólida, chegando a 7,40 e 7,55, respectivamente. A recuperação do indicador Psicossocial (IPS) em 2024, após uma queda no ano anterior, reforça a capacidade do projeto de ajustar rotas e apoiar o aluno. Essa evolução equilibrada prova que a Passos Mágicos gera um impacto real e multidimensional na vida dos jovens.")
                 
    df_all = df.groupby('ano')[['ida', 'ieg', 'ips', 'ipp', 'inde']].mean().reset_index().melt(id_vars='ano')
    fig11 = px.line(df_all, x='ano', y='value', color='variable', markers=True, text='value')
    fig11.update_traces(texttemplate='%{text:.1f}', textposition='top center', line=dict(width=4))
    fig11.update_xaxes(tickvals=[2022, 2023, 2024])
    st.plotly_chart(apply_plotly_layout(fig11), use_container_width=True)


elif menu == "🔍 Predição de Risco":
    st.markdown("""
        <style>
        div[data-testid="stNumberInput"] > label, div[data-testid="stSelectbox"] > label, div[data-testid="stRadio"] > label, div[data-testid="stSlider"] > label {
            color: #8be9fd !important;
            font-weight: 800 !important;
            font-size: 16px !important;
        }
        div[data-testid="stNumberInput"], div[data-testid="stSelectbox"], div[data-testid="stRadio"], div[data-testid="stSlider"] {
            background-color: #1a1a2e;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #8be9fd;
            margin-bottom: 10px;
        }
        div[data-baseweb="slider"] div {
            background-color: #ffffff !important;
        }
        .stButton>button {
            background-color: #50fa7b !important;
            color: #0d1117 !important;
            font-size: 20px !important;
            font-weight: bold !important;
            border-radius: 10px !important;
            transition: 0.3s !important;
        }
        .stButton>button:hover {
            box-shadow: 0 0 20px #50fa7b !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Modelo de predição de risco")
    st.markdown("Preencha o formulário abaixo com as informações do aluno. O sistema analisará os dados sociodemográficos e as notas da jornada de base para prever de forma antecipada a probabilidade do jovem entrar em um quadro grave de defasagem, direcionando assim esforços pedagógicos corretivos de maneira certeira.")
    
    if modelo_dict is None:
        st.error("O modelo Preditivo ('modelo_risco.pkl') não foi encontrado.")
    else:
        xgb_model = modelo_dict['modelo']
        le_genero = modelo_dict['le_genero']
        le_bolsa = modelo_dict['le_bolsa']
        
        st.markdown("### 👤 Dados do Aluno")
        c1, c2, c3 = st.columns(3)
        with c1:
            idade = st.number_input("Idade de Ingresso no Curso", min_value=5, max_value=25, value=12)
        with c2:
            bolsa = st.radio("Possui Bolsa em Instituição Privada?", ["Sim", "Não"], horizontal=True)
        with c3:
            genero = st.radio("Gênero", ["Masculino", "Feminino"], horizontal=True)
            gen_val = genero
            
        st.markdown("### 📝 Notas do período atual")
        n1, n2, n3 = st.columns(3)
        with n1:
            ida = st.slider("Desempenho Acadêmico (IDA)", 0.0, 10.0, 6.0, 0.1)
            delta_ida = st.number_input("Variação (IDA)", min_value=-10.0, max_value=10.0, value=0.0)
            ipp = st.slider("Avaliação Psicopedagógica (IPP)", 0.0, 10.0, 7.0, 0.1)
        with n2:
            ieg = st.slider("Engajamento p/ Tarefas (IEG)", 0.0, 10.0, 7.5, 0.1)
            delta_ieg = st.number_input("Variação (IEG)", min_value=-10.0, max_value=10.0, value=0.0)
            iaa = st.slider("Auto-avaliação do Aluno (IAA)", 0.0, 10.0, 8.0, 0.1)
        with n3:
            ips = st.slider("Bem Estar Psicossocial (IPS)", 0.0, 10.0, 8.0, 0.1)
            delta_ips = st.number_input("Variação Emocional (IPS)", min_value=-10.0, max_value=10.0, value=0.0)
            ipv = st.slider("Ponto de Virada (IPV)", 0.0, 10.0, 6.5, 0.1)
            
        st.markdown('<div style="height: 15px;"></div>', unsafe_allow_html=True)
        submit = st.button("Analisar o Risco", use_container_width=True)
        
        if submit:
            ph = st.empty()
            ph.markdown('''
                <div style="background-color: #1a1a2e; border: 2px solid #8be9fd; padding: 20px; text-align: center; border-radius: 10px; box-shadow: 0 0 20px rgba(139, 233, 253, 0.5); margin-bottom: 20px;">
                    <h3 style="color: #8be9fd; margin: 0;">⚡ Rodando o modelo...</h3>
                </div>
            ''', unsafe_allow_html=True)
            
            time.sleep(3)
            ph.empty()
            
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
                st.markdown("## 📊 Resultado da análise")
                
                if classe == 1 or probabilidade > 50:
                    cor = "#ff5555" # vermelho neon
                    titulo = "RISCO ALTO DE DEFASAGEM"
                    texto_peso = "A falta de engajamento aliada a baixas notas atuais refletem uma desmotivação significativa. A tendência atual é o aluno perder o ponto de adesão ao programa da ONG se não acompanhado imediatamente."
                    texto_sugestao = "Ativar uma mentoria urgente e aproximação com os responsáveis. Foque no resgate e suporte emocional num primeiro momento (psicopedagogia) antes de exigir pressão por performance acadêmica, fortalecendo inicialmente a assiduidade."
                elif probabilidade > 30:
                    cor = "#f1fa8c" # amarelo
                    titulo = "ATENÇÃO: RISCO MODERADO"
                    texto_peso = "Ocorrem oscilações preocupantes em campos atitudinais, possivelmente variação negativa indicando uma desmotivação ou dificuldade em algumas disciplinas."
                    texto_sugestao = "Acompanhamento pedagógico quinzenal. Recomendamos oficinas de reforço ou aulas de revisão (atividades extras em que seja cobrado a presença) para evitar que a defasagem se alargue nos próximos meses."
                else:
                    cor = "#50fa7b" # verde neon
                    titulo = "BOM PROGNÓSTICO"
                    texto_peso = "O aluno demonstra excepcional estabilidade nos resultados e níveis altos e promissores de engajamento contínuo. Entendimento pedagógico alinhado."
                    texto_sugestao = "Mantenha ou instigue a autonomia. Desafios que gerem protagonismo da rotina, como colocá-lo no grupo de alunos que auxiliam os iniciantes como monitores, impulsionará em definitivo seu Ponto de Virada."
                
                st.markdown(f'''
                    <div style="background-color: #1a1a2e; border-left: 8px solid {cor}; padding: 30px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.4);">
                        <h2 style="color: {cor}; margin-top: 0;">{titulo} ({probabilidade:.1f}%)</h2>
                        <h4 style="color: #ffffff; margin-top: 20px;">🔍 O que pesou na análise:</h4>
                        <p style="color: #cccccc; font-size: 16px;">{texto_peso}</p>
                        <h4 style="color: #8be9fd; margin-top: 20px;">💡 Sugestão de Intervenção:</h4>
                        <p style="color: #cccccc; font-size: 16px;">{texto_sugestao}</p>
                    </div>
                ''', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Erro ao processar predição: {e}")
