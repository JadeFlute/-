import numpy as np

#
new_type = np.dtype([('name',np.str_,40),('num',np.int64),('price',np.float64)])
print(new_type)
print(new_type['name'])
# [('name', '<U40'), ('num', '<i8'), ('price', '<f8')]
# <U40

goods_info = np.array([('白菜',100,1.5),('土豆',200,1)],dtype=new_type)
print(goods_info)







































