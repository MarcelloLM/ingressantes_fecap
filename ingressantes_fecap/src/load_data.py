import pandas as pd

def carregar_csv():
    url = "https://raw.githubusercontent.com/MarcelloLM/ingressantes_fecap/refs/heads/main/ingressantes_fecap/data/ingressantes_2025.csv"
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        raise Exception(f"Erro ao carregar a base de dados: {e}")
