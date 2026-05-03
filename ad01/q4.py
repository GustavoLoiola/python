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

# garantir formato de data
df["sent_at"] = pd.to_datetime(df["sent_at"])

# agrupar por mês (corrigido)
q4 = df.set_index("sent_at").resample("ME").agg({
    "receive_rate": "mean",
    "open_rate": "mean",
    "conversion_rate": "mean"
})

print(q4.round(4))