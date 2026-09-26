import numpy as py 
import pandas as pd 
data = {
    "姓名": ["卡西莫多", "爱丝美拉达", "弗罗洛", "格兰古瓦", "弗比斯"],
    "年龄": [20, 16, 40, 25, 18],
    "语文": [18, 67, 96, 85, 58],
    "数学": [3, 86, 92, 60, 45],
}
df=pd.DataFrame(data,index=["甲", "乙", "丙", "丁", "戊"])
print("原始表格:",df)
df["总分"]=df["语文"]+df["数学"]
print("\n加了总分列:",df)
df["班级"]="大二"
print("\n加了班级列:",df)
df["是否及格"]=df["总分"]>=120
print("\n加了是否及格",df)
df2=df.drop(columns=["班级"])
print("\n删除班级",df2)
df3=df.drop(columns=["总分","是否及格"])
print("\n一次删2列",df3)
df4=df.rename(columns={"语文":"chinese","数学":"math"})
print("\n改名",df4)
print(df)