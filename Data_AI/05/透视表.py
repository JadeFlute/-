import pandas as pd
import numpy as np


detail = pd.read_excel('meal_order_detail.xlsx')


pivot = pd.pivot_table(detail[['order_id','counts','amounts']],index='order_id')
print(pivot.head())

pivot = pd.pivot_table(detail[['order_id','counts','amounts']],index='order_id',aggfunc=np.sum)
print(pivot.head())


# 以order_id 和 dishes_name作为分组键
# 创建的订单销量和售价总和透视表
# 以'order_id','dishes_name'为键，计算counts和amounts的和；
# 如果有两条数据的'order_id','dishes_name'都一样，这两个数据就会求和；否则不求和
pivot = pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index=['order_id','dishes_name'],aggfunc=np.sum)
print(pivot.head())

# 以 'order_id'为行,'dishes_name'为列
pivot = pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index='order_id',columns='dishes_name',aggfunc=np.sum)
print(pivot.head())
# dishes_name  42度海之蓝  北冰洋汽水  38度剑南春   ...   黄油曲奇饼干 黄花菜炒木耳 黑米恋上葡萄
# order_id                             ...
# 137             NaN     NaN     NaN  ...      NaN    NaN    NaN
# 165             NaN     NaN    80.0  ...      NaN    1.0    NaN
# 166             NaN     NaN     NaN  ...      NaN    NaN    NaN
# 171             NaN     NaN     NaN  ...      NaN    NaN    NaN
# 177             NaN     NaN     NaN  ...      NaN    NaN    NaN




# order_id 为键，counts 为值；计算每个订单点了多少菜
pivot = pd.pivot_table(detail[['order_id','dishes_name','counts','amounts']],index='order_id',values='counts',aggfunc=np.sum)
print(pivot.head())



# 交叉表--特殊的透视表;需要使用时间字段
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
detail['date'] = [i.date() for i in detail['place_order_time']]
# 提取时间：天，作为行索引，这样一天就是一条数据
crosstab = pd.crosstab(index=detail['date'],
            columns=detail['dishes_name'],
            values=detail['amounts'],
            aggfunc=np.sum)
# 统计每天，每种菜的销售额
print(crosstab)
















