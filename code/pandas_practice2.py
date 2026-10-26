# ============================================================
# 阶段一结业项目：武功山 90 天天气 EDA
# EDA = Exploratory Data Analysis（探索性数据分析）
# 说人话：拿到一份陌生数据，先摸清它长什么样，再画成图找规律
# 完整流程：读 CSV → 清洗 → 统计 → 画图 → 存成 png
# ============================================================

# 导入 pandas 库，起个小名叫 pd
# 以后写 pd.xxx 就是调用 pandas 的功能
# ⚠️ 这个 pd 是全网通用的写法，别写成 py（py 是你跑程序的命令，不是这里的名字）
import pandas as pd

# 导入 matplotlib 里的画图工具，起个小名叫 plt
# plt 同样是通用写法
import matplotlib.pyplot as plt

# 设置中文字体为微软雅黑
# 不加这行：图里的中文会显示成一个个方框 □□□（这个现象术语叫 tofu）
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

# 让负号正常显示
# 不加这行：出现负数时（比如 -5℃）那个减号也会变成方框
# ⚠️ 注意 unicode_minus 中间是下划线 _ ，不是空格，你上次就是敲成了空格
plt.rcParams["axes.unicode_minus"] = False

# ---------- 第 1 步：把数据读进来 ----------

# read_csv 读取 CSV 文件，读出来的东西叫 DataFrame（一张数据表），存进变量 df
# df 是 data frame 的缩写
# 括号里是"相对路径"：从你运行命令时所在的文件夹开始找
# 所以必须在 D:/神临/learning-journal 目录下运行，否则找不到 data 文件夹
df = pd.read_csv("data/wugongshan_weather.csv")

# shape 返回 (行数, 列数)，用来看看这张表有多大
print("行数列数:", df.shape)

# isnull() 检查每个格子：是空值就标记 True，否则 False
# .sum() 再按列数一数有多少个 True
# 结果能一眼看出：哪几列有空缺、各缺几个
print("缺失值:\n", df.isnull().sum())

# describe() 对数值列做统计摘要
# 输出：个数 count、平均值 mean、标准差 std、最小值、25%、50%、75%、最大值
# 这是摸清一份数据的第一刀，不用自己一个个算
print("统计摘要:\n", df.describe())

# ---------- 第 2 步：清洗数据 + 造新列 ----------

# 把"日期"这一列从文字（字符串）转成真正的日期类型
# 不转的话它只是一串字，没法取月份、没法算间隔
# ⚠️ 是 pd.to_datetime（pandas 的工具），不是 df.to_datetime，你上次写反了
df["日期"] = pd.to_datetime(df["日期"])

# 新增一列叫"温差"，值 = 最高气温 减 最低气温
# pandas 里两列相减会自动一行一行对齐着算，不用写循环
# ⚠️ 减号右边也要写 df，写成 ["最低气温"] 就变成普通列表了
df["温差"] = df["最高气温"] - df["最低气温"]

# 新增一列叫"月份"，从日期里取出月份数字（7、8、9、10）
# .dt 是"日期工具箱"，.month 从中取月份
# ⚠️ month 是属性不是函数，后面不加括号；也别拼成 moth
df["月份"] = df["日期"].dt.month

# ---------- 第 3 步：分组统计 ----------

# groupby("月份") 先按月份把 90 行分成 4 组（7月、8月、9月、10月）
# 后面跟上要统计的列：最高气温、最低气温、降水量
# .mean() 再对每组求平均值
# 结果存进 month_mean，是一张 4 行 3 列的小表
month_mean = df.groupby("月份")[["最高气温", "最低气温", "降水量"]].mean()

# 把这张月度汇总表打印出来看看
print("每月平均:\n", month_mean)

# ---------- 第 4 步：四张图拼在一张画布上 ----------

# subplots(2, 2) 创建一张大画布，上面切出 2 行 2 列共 4 个格子
# figsize=(14, 9) 是整张画布的尺寸，单位英寸，14 宽 9 高
# 它返回两个东西，所以左边要写两个变量来接：
#   fig  = 整张纸（这张纸我们基本不用管它，但必须接住）
#   axes = 纸上的 4 个格子
fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# axes 是一个 2 行 2 列的数组，用 axes[行, 列] 取格子，序号从 0 开始：
#   axes[0, 0] 左上    axes[0, 1] 右上
#   axes[1, 0] 左下    axes[1, 1] 右下

# ---------- 图 1（左上角）：最高温和最低温两条折线 ----------

# 在左上格子里画折线：X 轴是日期，Y 轴是最高气温
# label 是这条线的名字，配合下面的 legend() 才会显示出来
# color 是颜色，tomato 是番茄红
axes[0, 0].plot(df["日期"], df["最高气温"], label="最高温", color="tomato")

# 在同一个格子里再画一条线：最低气温，用钢蓝色
# 两条线画在同一个 axes[0, 0] 上，就会叠在一起方便对比
axes[0, 0].plot(df["日期"], df["最低气温"], label="最低温", color="steelblue")

# 给这个格子加标题
# 注意：这里是 set_title（前面有 set_），跟单图时的 plt.title 不一样
axes[0, 0].set_title("90 天最高温 / 最低温")

# 给这个格子的 Y 轴加标签
axes[0, 0].set_ylabel("气温 (℃)")

# 显示图例（右上角那个小方框，标着哪条线是什么）
# 不写这行，上面 label 写的名字就不会显示
axes[0, 0].legend()

# ---------- 图 2（右上角）：每日降水量柱状图 ----------

# 在右上格子画柱状图：X 轴日期，Y 轴降水量
# width=1.0 让每根柱子宽度占满一天，不然 90 根柱子会细成一条条线
axes[0, 1].bar(df["日期"], df["降水量"], color="seagreen", width=1.0)

# 给右上格子加标题
axes[0, 1].set_title("每日降水量")

# 给右上格子的 Y 轴加标签
axes[0, 1].set_ylabel("降水量 (mm)")

# ---------- 图 3（左下角）：温差散点图 ----------

# 在左下格子画散点图：X 轴日期，Y 轴温差
# s=12 是每个点的大小（s = size）
# 散点图用来看"每一天温差是多少"，不像折线那样强调趋势
axes[1, 0].scatter(df["日期"], df["温差"], s=12, color="darkorange")

# 给左下格子加标题
axes[1, 0].set_title("每日温差")

# 给左下格子的 Y 轴加标签
axes[1, 0].set_ylabel("温差 (℃)")

# ---------- 图 4（右下角）：每月平均气温并排柱状图 ----------

# 这一张换成用 pandas 自带的画图功能
# 取 month_mean 里的两列（最高气温、最低气温）
# kind="bar" 表示画柱状图
# ax=axes[1, 1] 指定画到右下那个格子（不指定的话它会自己新开一张图）
# color 传一个列表，第一列用番茄红、第二列用钢蓝
month_mean[["最高气温", "最低气温"]].plot(
    kind="bar", ax=axes[1, 1], color=["tomato", "steelblue"]
)

# 给右下格子加标题
axes[1, 1].set_title("每月平均气温")

# 给右下格子的 Y 轴加标签
axes[1, 1].set_ylabel("气温 (℃)")

# tight_layout 自动调整四个格子之间的间距
# 不加这行，标题和坐标轴标签会互相压住、甚至被裁掉
plt.tight_layout()

# savefig 把整张图保存成图片文件
# dpi=150 是清晰度，数字越大越清楚、文件也越大
plt.savefig("data/wugongshan_eda.png", dpi=150)

# show 把图弹窗显示出来
# ⚠️ 这行必须放最后：窗口不关掉，程序就停在这行不往下走
plt.show()
