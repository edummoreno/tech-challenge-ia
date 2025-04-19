# Exploracao de Dados - Tech Challenge

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Carregando o dataset
path = Path(__file__).parent / "data" / "insurance.csv"
df = pd.read_csv(path)

# Ver primeiras linhas
print("Primeiras linhas do dataset:")
print(df.head())

# Informações gerais
print("\nInformações gerais:")
print(df.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Verificar dados nulos
print("\nDados nulos por coluna:")
print(df.isnull().sum())

# Visualizar distribuição das variáveis numéricas
num_cols = ['age', 'bmi', 'children', 'charges']

for col in num_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribuição de {col}')
    plt.xlabel(col)
    plt.ylabel('Contagem')
    plt.show()

# Verificar variáveis categóricas
cat_cols = ['sex', 'smoker', 'region']

for col in cat_cols:
    plt.figure()
    sns.countplot(x=df[col])
    plt.title(f'Contagem por categoria - {col}')
    plt.xlabel(col)
    plt.ylabel('Contagem')
    plt.show()

# Matriz de Correlação (apenas colunas numéricas)
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()
