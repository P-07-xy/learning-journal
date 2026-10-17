import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"]=False
df=pd.read_csv("data/wugongshan_weather.csv")
plt.figure(figsize=(12,5))
plt.plot(df["日期"],df["最高气温"])
plt.title("武功山 90 天最高气温变化")
plt.xlabel("日期")
plt.ylabel("气温(℃)")
plt.xticks(range(0,len(df),10),df["日期"].iloc[::10],rotation=45)
plt.tight_layout()
plt.savefig("data/wugongshan_temperature.png",dpi=150)
plt.show()