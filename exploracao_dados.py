from pathlib import Path
import pandas as pd

# Caminho dinâmico
path = Path(__file__).parent / "data" / "insurance.csv"
df = pd.read_csv(path)

print(df.head())
