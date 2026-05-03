import pandas as pd

# carregar dados
df = pd.read_excel(r"c:\Users\Gustavo\Downloads\campaigns_excel.xlsx")

# tratamento
df["result_value"] = df["result_value"].fillna(0)

df["receive_rate"] = df["receive_rate"] / 100
df["open_rate"] = df["open_rate"] / 100
df["conversion_rate"] = df["conversion_rate"] / 100

# criar country (mantemos padrão)
def identificar_pais(nome):
    if "campanha" in nome.lower():
        return "Brazil"
    elif "campana" in nome.lower():
        return "Mexico"
    else:
        return "Unknown"

df["country"] = df["campaign_name"].apply(identificar_pais)

# Q3 — funil por canal
q3 = df.groupby("channel").agg(
    avg_receive_rate=("receive_rate", "mean"),
    avg_open_rate=("open_rate", "mean"),
    avg_conversion_rate=("conversion_rate", "mean"),
    total_campaigns=("campaign_id", "count")
).sort_values("avg_conversion_rate", ascending=False)

print(q3.round(4))