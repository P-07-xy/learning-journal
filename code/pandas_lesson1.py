import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series:\n", s)

dates = pd.date_range('20260915', periods=6)
print("\n日期索引:\n", dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print("\nDataFrame:\n", df)

print("\n列名:", df.columns.tolist())
print("行索引:", df.index)

df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20260915'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
})
print("\n字典创建:\n", df2)
print("\n每列的类型:\n", df2.dtypes)
