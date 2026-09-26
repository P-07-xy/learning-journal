import numpy as py 
import pandas as pd 
data={
    "姓名": ["卡西魔多","爱丝美拉达","佛罗洛","格兰古瓦","浮比斯"],
    "年龄": [20,16,40,23,18],
    "成绩": [2,68,90,78,45],
}
df=pd.DataFrame(data,index=["甲","已","丙","丁","戊"])
print(df)
print("\nloc取一行:",df.loc["丙"])
print("\n取某行某列:",df.loc["丙","成绩"])
print("\n切多行多列:",df.loc["甲":"丙",["姓名","成绩"]])
print("\niloc取第0行:",df.iloc[0])
print("\n取前三行，第0和第二列:",df.iloc[0:2,[0,2]])
print("\n成绩大于60的人:")
print(df[df["成绩"]>60])
print("\n成绩 >= 60 且 年龄 < 30 的人：")
print(df[(df["成绩"]>60) & (df["年龄"]<30)])