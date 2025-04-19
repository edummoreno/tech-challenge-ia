# Pré-processamento de Dados - Tech Challenge

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from pathlib import Path

# Carregar o dataset
path = Path(__file__).parent / "data" / "insurance.csv"
df = pd.read_csv(path)

# 1. Tratar valores nulos
print("\nValores nulos antes do tratamento:")
print(df.isnull().sum())

# (Este dataset não tem nulos, mas normalmente preencheríamos ou excluiríamos aqui.)

# 2. Codificar variáveis categóricas (One Hot Encoding)
categorical_features = ['sex', 'smoker', 'region']

# Aplicar One Hot Encoding
df_encoded = pd.get_dummies(df, columns=categorical_features, drop_first=True)

print("\nDataFrame após One Hot Encoding:")
print(df_encoded.head())

# 3. Separar features (X) e target (y)
X = df_encoded.drop('charges', axis=1)
y = df_encoded['charges']

# 4. Escalar variáveis numéricas
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("\nFormato dos conjuntos:")
print(f"X_train: {X_train.shape}, X_test: {X_test.shape}")
print(f"y_train: {y_train.shape}, y_test: {y_test.shape}")
