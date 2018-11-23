import pandas as pd

detail = pd.read_excel('meal_order_detail.xlsx')
# 取出一列的值（dishes_name，不包括第一行的列名）
dish = detail['dishes_name']
# print(dish)


# 获取前6行
detail_pre6 = dish[:7]
print(detail_pre6)


# print('整个表的前五行',detail.head())
# print('菜品名称后五行',dish.tail)


# 1-7行，列名：['dishes_name','amounts']
d1 = detail.loc[1:7,['dishes_name','amounts']]
print(d1)
print('描述信息',d1.describe())
# count   7.000000
# mean   49.571429
# std    29.748149
# min    13.000000
# 25%    27.500000
# 50%    48.000000
# 75%    71.500000
# max    88.000000


# 1-2列，1-6行数据（下标不算表头）
d2 = detail.iloc[1:7,1:3]
print(d2)


# 筛选
# 筛选：条件：列名order_id中等于458的行
r1 = detail.loc[detail['order_id'] == 458]
print(r1)



