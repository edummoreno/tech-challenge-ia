# 📋 PLANO DE AÇÃO – TECH CHALLENGE

## Fase 1: Configurar o ambiente
- Criar uma pasta local para o projeto.
- Criar repositório no GitHub (nome sugerido: `tech-challenge-ia`).
- Configurar ambiente de trabalho (ex.: instalar Jupyter, Pandas, Scikit-Learn, Matplotlib, Seaborn).

## Fase 2: Exploração de Dados
- Carregar o dataset no Python.
- Mostrar primeiras linhas (`head()`).
- Verificar informações (`info()`, `describe()`).
- Plotar gráficos:
  - Histograma de cada variável numérica.
  - Gráfico de barras para variáveis categóricas (como gênero, fumante, região).

## Fase 3: Pré-processamento de Dados
- Tratar valores nulos (se tiver).
- Transformar variáveis categóricas:
  - `OneHotEncoder` para região, gênero e fumante.
- Escalar variáveis (opcional para regressão, mas recomendado para alguns modelos).

## Fase 4: Criação e Treinamento do Modelo
- Dividir os dados:
  - 80% para treino
  - 20% para teste (`train_test_split` do Sklearn)
- Escolher o modelo:
  - Sugestão simples: **Regressão Linear** para começar.
- Treinar o modelo (`fit`).

## Fase 5: Avaliação do Modelo
- Fazer previsões no conjunto de teste (`predict`).
- Avaliar o modelo:
  - **R² Score** (coeficiente de determinação).
  - **MSE** (Erro Quadrático Médio).
- Analisar resíduos (erros).

## Fase 6: Validação Estatística
- Calcular o **p-value** e os **intervalos de confiança** (usando `Statsmodels` ou `SciPy`).
- Interpretar se as variáveis são estatisticamente significativas.

## Fase 7: Resultados Visuais e Relatório
- Criar gráficos:
  - Gráfico de dispersão (valores reais vs previstos).
- Escrever relatório explicando:
  - O que foi feito em cada fase.
  - Quais insights você teve.
  - Validação do modelo.

## Fase 8: Entrega
- Gravar um vídeo de até 10 minutos:
  - Mostrando o código.
  - Explicando o processo.
  - Falando dos resultados.
- Subir o vídeo no YouTube (modo **não listado**).
- Atualizar o repositório do GitHub:
  - Código + link do vídeo no `README.md`.
