import math
import numpy as np

movie_data = {"宝贝当家": [45, 2, 9, "喜剧片"],
              "美人鱼": [21, 17, 5, "喜剧片"],
              "澳门风云3": [54, 9, 11, "喜剧片"],
              "功夫熊猫3": [39, 0, 31, "喜剧片"],
              "谍影重重": [5, 2, 57, "动作片"],
              "叶问3": [3, 2, 65, "动作片"],
              "伦敦陷落": [2, 3, 55, "动作片"],
              "我的特工爷爷": [6, 4, 21, "动作片"],
              "奔爱": [7, 46, 4, "爱情片"],
                "夜孔雀": [9, 39, 8, "爱情片"],
              "代理情人": [9, 38, 2, "爱情片"],
              "新步步惊心": [8, 34, 17, "爱情片"]}


# 计算新样本与上面每个数据的欧式距离
x = [23,3,17]
knn = []
for key,val in movie_data.items():
    d = math.sqrt((x[0]-val[0])**2+(x[1]-val[1])**2+(x[2]-val[2])**2)
    knn.append([key,round(d,2),val[3]])

print(knn)
knn.sort(key=lambda movie:movie[1])
print('排序后',knn)

# xj = 0
# dz = 0
# aq = 0
#
# for i in range(5):
#     movie = knn[i]
#     t = movie[2]
#
#     if t == '喜剧片':
#         xj += 1
#     elif t == '动作片':
#         dz += 1
#     elif t == '爱情片':
#         aq += 1
#
# re_list = [['喜剧片',xj],['动作片',dz],['爱情片',aq]]
#
# re_list.sort(key=lambda result:result[1],reverse=True)
# print(re_list[0])

# 方法2：
re_dict = {'喜剧片':0,'动作片':0,'爱情片':0}

for label in knn[:5]:

    re_dict[label[2]] += 1

print(re_dict.items())
re_dict = sorted(re_dict.items(),key=lambda result:result[1],reverse=True)
print(re_dict)


# 计算欧氏距离--排序--取前五个--计算各标签总数--根据总数倒序--取第一个--获得结果标签

















