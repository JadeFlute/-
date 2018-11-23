import pandas as pd
import numpy as np


detail = pd.read_excel('meal_order_detail.xlsx')
# 分组
group = detail[['order_id','counts','amounts']].groupby(by='order_id')
# print('求每组均值，取前五个',group.mean().head())
# print(group.size().head())
# print(group.std().head())

# 求 菜品销量和售价的均值，以及总和
# ps: 本来只能有一个参数的变量，如果想赋多个值，
# 将多个值放进列表
print(detail[['counts','amounts']].agg([np.mean,np.sum]))

print(detail.agg({'counts':np.sum,'amounts':[np.mean,np.sum]}))


def double_sum(data):
    return np.sum(data)*2


print('离差标椎化',group.transform(lambda x:(x.mean()-x.min())/(x.max()-x.min())))
