import matplotlib.pyplot as plt 
plt.rcParams["font.sans-serif"]=["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"]=False
subjects=["Python","高数","英语","电路","大物"]
scores=[95,68,61,78,82]
plt.figure(figsize=(8,5))
plt.bar(subjects,scores)
plt.title("我的第一张柱状图")
plt.xlabel("科目")
plt.ylabel("分数")
plt.show()