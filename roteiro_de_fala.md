# 🎤 ROTEIRO DE FALA PARA O VÍDEO

---

## 0. Apresentação (30 segundos)

- "Olá! Meu nome é **Eduardo Moreno Neto**, e esse é o projeto desenvolvido para o **Tech Challenge da Pós-Tech FIAP**."
- "O desafio era criar um **modelo de regressão** capaz de prever **custos médicos individuais** baseado em dados pessoais."

---

## 1. Apresentação do problema e do dataset (1 minuto)

- "O objetivo do projeto é **estimar o valor do custo médico** de um paciente, usando informações como idade, IMC, se a pessoa fuma, entre outros."
- "O dataset utilizado foi o **insurance.csv**, contendo **1338 registros** de pacientes de diferentes regiões dos Estados Unidos."
- "As variáveis principais foram: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, e `charges`."

---

## 2. Exploração de Dados (1,5 minutos)

- "Realizamos uma **análise exploratória** para entender as distribuições das variáveis."
- "Observamos, por exemplo, que **pacientes fumantes apresentavam custos médicos significativamente maiores**."
- "Utilizamos **histogramas** para visualizar variáveis numéricas e **gráficos de contagem** para variáveis categóricas."
- "Também criamos uma **matriz de correlação** para identificar relações entre as variáveis."

---

## 3. Pré-processamento dos dados (1,5 minutos)

- "As variáveis categóricas foram transformadas usando **One Hot Encoding**."
- "Utilizamos o **StandardScaler** para normalizar as variáveis numéricas."
- "A separação dos dados foi feita com **80% para treino** e **20% para teste**, garantindo uma avaliação imparcial do modelo."

---

## 4. Modelagem e Avaliação (2 minutos)

- "Escolhemos um modelo de **Regressão Linear** como ponto de partida para prever os custos médicos."
- "Treinamos o modelo utilizando o conjunto de treino e avaliamos utilizando métricas como o **MSE (Erro Quadrático Médio)** e o **R² (Coeficiente de Determinação)**."
- "Obtivemos um **MSE de aproximadamente 33.701.904,5** e um **R² de 0.75**, indicando uma boa capacidade de explicação dos dados."

---

## 5. Resultados Visuais (1,5 minutos)

- "Geramos um **gráfico de dispersão (scatter plot)** para comparar os valores reais versus os valores previstos."
- "A maioria dos pontos ficou próxima da linha ideal, indicando que o modelo teve uma **performance satisfatória**."
- "Também visualizamos a **distribuição dos erros**, onde observamos que eles estavam concentrados próximos de zero."

---

## 6. Conclusão e Melhorias Futuras (1 minuto)

- "O modelo de **Regressão Linear** se mostrou eficaz para a tarefa proposta, mas existem melhorias possíveis."
- "Futuramente, poderíamos testar algoritmos mais avançados, como **Random Forest** ou **XGBoost**, além de trabalhar no ajuste de hiperparâmetros e criação de novas features."
- "Esse projeto foi uma excelente oportunidade de aplicar na prática os conceitos de **Machine Learning e Ciência de Dados**."

---

## 7. Encerramento (15 segundos)

- "Muito obrigado por acompanhar a apresentação!  
Espero que tenham gostado. 🚀"

---
