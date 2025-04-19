# Modelo de Regressão - Tech Challenge
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path

# Carregar o dataset
path = Path(__file__).parent / "data" / "insurance.csv"
df = pd.read_csv(path)

# Pré-processamento (mesmo processo anterior)
df_encoded = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)

X = df_encoded.drop('charges', axis=1)
y = df_encoded['charges']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 1. Instanciar o modelo
model = LinearRegression()

# 2. Treinar o modelo
model.fit(X_train, y_train)

# 3. Fazer previsões
y_pred = model.predict(X_test)

# 4. Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMSE (Erro Quadrático Médio): {mse:.2f}")
print(f"R² (Coeficiente de Determinação): {r2:.2f}")

# 5. Comparar previsões vs valores reais
results = pd.DataFrame({'Real': y_test, 'Previsto': y_pred})
print("\nComparação entre valores reais e previstos:")
print(results.head())


# Comparação visual: Valores Reais vs Previstos

# 1. Scatter plot (Dispersão)
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Valor Real')
plt.ylabel('Valor Previsto')
plt.title('Valores Reais vs Valores Previstos')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Linha ideal
plt.show()

# 2. Histograma dos Erros
errors = y_test - y_pred
plt.figure(figsize=(8,6))
sns.histplot(errors, kde=True)
plt.title('Distribuição dos Erros')
plt.xlabel('Erro (Real - Previsto)')
plt.ylabel('Frequência')
plt.show()