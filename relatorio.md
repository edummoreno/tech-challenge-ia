# Tech Challenge - Previsão de Custos Médicos 🏥📊

---

## 1. Introdução

Este projeto busca desenvolver um modelo de regressão capaz de prever o custo médico de clientes de seguros de saúde, baseado em informações como idade, IMC, número de filhos, tabagismo e região.

A previsão de custos médicos ajuda seguradoras a precificar planos de maneira justa e equilibrada, além de contribuir para estratégias de gerenciamento de riscos.

---

## 2. Base de Dados

- **Nome**: insurance.csv
- **Fonte**: [Dataset Insurance - GitHub](https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv)
- **Número de registros**: 1338
- **Principais variáveis**:
  - `age`: Idade do paciente
  - `sex`: Gênero
  - `bmi`: Índice de Massa Corporal
  - `children`: Número de filhos
  - `smoker`: Se o paciente é fumante
  - `region`: Região geográfica
  - `charges`: Custo médico (variável alvo)

---

## 3. Exploração de Dados

Foram analisadas estatísticas descritivas e visualizações gráficas:

- **Distribuições**:
  - Idade, IMC, Número de filhos e Custos médicos mostraram distribuições variadas.
- **Fumantes**:
  - Pessoas fumantes apresentam custos médicos muito mais elevados.
- **Correlação**:
  - O custo médico apresentou correlação positiva com idade, IMC e hábito de fumar.

---

## 4. Pré-Processamento

As seguintes etapas foram realizadas:

- Não havia valores nulos a tratar.
- Codificação das variáveis categóricas utilizando **One Hot Encoding**.
- Escalonamento das variáveis numéricas utilizando **StandardScaler**.
- Separação dos dados:
  - 80% para treino (`X_train`, `y_train`)
  - 20% para teste (`X_test`, `y_test`)

---

## 5. Modelagem

- **Modelo utilizado**: Regressão Linear.
- **Treinamento**: Modelo treinado com `X_train` e `y_train`.
- **Avaliação**:
  - **MSE (Erro Quadrático Médio)**: 33701904.5
  - **R² (Coeficiente de Determinação)**: 0.75

---

## 6. Resultados Visuais

### Comparação entre Valores Reais e Previstos:
- **Scatter plot**:
  - A maioria dos pontos ficou próxima da linha ideal (predição perfeita).
- **Histograma dos Erros**:
  - Distribuição dos erros concentrada próxima a zero, indicando boa performance.

---

## 7. Conclusões e Melhorias Futuras

- **Conclusão**:
  - O modelo é eficiente para prever custos médicos baseando-se nas variáveis disponíveis.
- **Possíveis Melhorias**:
  - Testar modelos mais complexos (Random Forest, XGBoost).
  - Realizar seleção de features para reduzir ruído.
  - Ajustar hiperparâmetros para otimizar o modelo.

---

## 8. Links Importantes

- [🔗 Repositório no GitHub](#)
- [🔗 Vídeo de Apresentação no YouTube](#)

---

