import pandas as pd

df = pd.read_excel(r"c:\Users\Gustavo\Downloads\campaigns_excel.xlsx")

df["result_value"] = df["result_value"].fillna(0)

df["receive_rate"] = df["receive_rate"] / 100
df["open_rate"] = df["open_rate"] / 100
df["conversion_rate"] = df["conversion_rate"] / 100

def identificar_pais(nome):
    if "campanha" in nome.lower():
        return "Brazil"
    elif "campana" in nome.lower():
        return "Mexico"
    else:
        return "Unknown"

df["country"] = df["campaign_name"].apply(identificar_pais)

q2 = df.groupby("tag").agg(
    total_result=("result_value", "sum"),
    avg_conversion_rate=("conversion_rate", "mean"),
    total_campaigns=("campaign_id", "count")
).sort_values("total_result", ascending=False)

print(q2.round(4))