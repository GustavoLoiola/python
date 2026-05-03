import pandas as pd

df = pd.read_excel(r"c:\Users\Gustavo\Downloads\campaigns_excel.xlsx")

# tratamento
df["result_value"] = df["result_value"].fillna(0)

df["receive_rate"] = df["receive_rate"] / 100
df["open_rate"] = df["open_rate"] / 100
df["conversion_rate"] = df["conversion_rate"] / 100

# criar país
def identificar_pais(nome):
    if "campanha" in nome.lower():
        return "Brazil"
    elif "campana" in nome.lower():
        return "Mexico"
    else:
        return "Unknown"

df["country"] = df["campaign_name"].apply(identificar_pais)

# Q1
q1 = df.groupby("country").agg(
    total_campaigns=("campaign_id", "count"),
    avg_receive_rate=("receive_rate", "mean"),
    avg_open_rate=("open_rate", "mean"),
    avg_conversion_rate=("conversion_rate", "mean"),
    total_result=("result_value", "sum")
)

print(q1.round(4))