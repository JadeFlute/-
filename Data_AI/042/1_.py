import pandas as pd


order = pd.read_table('meal_order_info.csv',sep=',',encoding='gbk')
# print(order)

print(order['lock_time'].dtype)
# 字符串转换成时间格式
order['lock_time'] = pd.to_datetime(order['lock_time'])
print(order['lock_time'].dtype)
# object
# datetime64[ns]


print('最小时间：',pd.Timestamp.min)
print('最大时间：',pd.Timestamp.max)
# 最小时间： 1677-09-21 00:12:43.145225
# 最大时间： 2262-04-11 23:47:16.854775807


dateindex = pd.DatetimeIndex(order['lock_time'])
print(dateindex)

# 前五条数据的年份
year5 = [i.year for i in order['lock_time']]
print(year5[:5])

weeks = [i.weekday_name for i in order['lock_time']]
print(weeks[:5])


time_1 = order['lock_time'] + pd.Timedelta(days=1)
print(time_1[:5])

# 广播机制
time_2 = order['lock_time'] - pd.to_datetime('2017-1-1 0:0:0')
print(time_2[:5])


timemin = order['lock_time'].min()
timemax = order['lock_time'].max()
print('订单持续时间：',timemax-timemin)


# 点餐用时最少和最多的时间是多少
# 时间计算，要转格式
order['use_start_time'] = pd.to_datetime(order['use_start_time'])
checktime = order['lock_time'] - order['use_start_time']
print('最少点餐时间：',checktime.min())
print('最多：',checktime.max())
print('平均：',checktime.mean())

#？每天点餐用时最少，最多，平均时间



