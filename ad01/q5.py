import pandas as pd

# carregar dados
df = pd.read_excel(r"c:\Users\Gustavo\Downloads\campaigns_excel.xlsx")

# tratamento
df["result_value"] = df["result_value"].fillna(0)

df["receive_rate"] = df["receive_rate"] / 100
df["open_rate"] = df["open_rate"] / 100
df["conversion_rate"] = df["conversion_rate"] / 100

# criar country
def identificar_pais(nome):
    if "campanha" in nome.lower():
        return "Brazil"
    elif "campana" in nome.lower():
        return "Mexico"
    else:
        return "Unknown"

df["country"] = df["campaign_name"].apply(identificar_pais)

# visão geral
print("Valores nulos:\n", df.isnull().sum(), "\n")

print("Resumo estatístico:\n", df.describe(), "\n")

print("Campanhas ativas vs finalizadas:\n", df["stopped_at"].isnull().value_counts(), "\n")

print("Resultado por status:\n", df.groupby("status")["result_value"].sum())