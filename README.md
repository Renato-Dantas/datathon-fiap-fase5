# 🔮 Datathon FIAP - Fase 5: Análise e Predição de Risco (Passos Mágicos)

## 📖 Descrição
Este projeto é o produto final do **Datathon da Fase 5** do curso de Pós-Graduação da **FIAP (Tech Challenge)**, desenvolvido em parceria com a ONG **Passos Mágicos**. 

O objetivo central foi receber uma base de dados educacional, realizar todo o processo de limpeza e análise exploratória (EDA) para entender o impacto da metodologia da ONG na vida dos alunos, e, por fim, criar uma solução tecnológica de valor: um dashboard interativo (Streamlit) contendo as principais descobertas analíticas e um sistema preditivo baseado em Machine Learning capaz de identificar, de forma antecipada, alunos com risco de defasagem acadêmica (Ponto de Virada).

## 🛠️ Tecnologias Usadas
- **Linguagem Principal:** Python 3.10+
- **Bibliotecas de Dados e Machine Learning:** Pandas, NumPy, Scikit-learn, XGBoost, SciPy.
- **Visualização de Dados:** Plotly (Express e Graph Objects), Seaborn, Matplotlib.
- **Framework Web (Dashboard):** Streamlit
- **Versionamento:** Git & GitHub

## 🎯 Proposta do Projeto
O Datathon propõe não apenas a análise de indicadores (como Engajamento - IEG, Desempenho - IDA e Avaliação Psicopedagógica - IPP), mas a tradução desses números em narrativa gerencial que prove o valor do projeto social.

Além da análise histórica e comportamental do fluxo de aprendizagem dos alunos da Passos Mágicos, o projeto inova ao entregar um **Sistema de Alerta Precoce** (Machine Learning). Esse modelo preditivo avalia dados demográficos e de desempenho atual do aluno para estimar a probabilidade matemática dele entrar em um quadro grave de defasagem, ajudando coordenadores e professores a aplicarem intervenções direcionadas antes mesmo de um eventual abandono.

## 💾 Base de Dados
A base de dados original foi cedida de forma anonimizada pela ONG Passos Mágicos, contendo registros evolutivos de performance escolar, perfil psicossocial e demográfico (bolsistas, faixas de ingresso etc.) cruzando os anos de 2022, 2023 e 2024.
Durante o projeto, os dados brutos foram higienizados e consolidados (`dataset_passos_magicos.csv`).

## 🚀 Como rodar o projeto localmente

1. Clone o repositório para a sua máquina:
   ```bash
   git clone https://github.com/Renato-Dantas/datathon-fiap-fase5.git
   cd datathon-fiap-fase5
   ```

2. (Opcional, mas recomendado) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows (PowerShell/CMD):
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências essenciais requeridas pelo projeto.
   ```bash
   pip install pandas numpy streamlit plotly scikit-learn xgboost scipy
   ```

4. Execute o Dashboard Streamlit:
   ```bash
   streamlit run app.py
   ```

## 🌐 Link do Deploy
[Link do projeto no ar] (Será atualizado em breve após o deploy final)
