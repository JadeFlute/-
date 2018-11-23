# 分治

# 有一个问题：
# (1) 将问题的规模 缩小到一定的程度 就可以相对容易的解决
# (2) 该问题可以分解为若干个规模较小的相同问题，即该问题具有最优子结构性质
# (3) 利用该问题分解出的子问题的解可以合并为该问题的解
# (4) 该问题所分解出的各个子问题是相互独立的，即问题之间不包含公共的子问题
# m = [1,2,3]
# print(m[2:4])


# 基本子算法
def get_max(lst):
    if len(lst) == 1:
        return lst[0]

    if lst[0] > lst[1]:
        return lst[0]
    else:
        return lst[1]

def solve(init_list):
    n = len(init_list)
    if n <= 2:
        return get_max(init_list)

    # 每次从列表取出两个元素;生成一个二维列表
    temp_list = (init_list[i:i+2] for i in range(0,n,2))

    result_list = []
    for num in temp_list:
        value = get_max(num)
        result_list.append(value)

    if len(result_list) >= 2:
        return solve(result_list)



def func(lst):
    n = len(lst)//2
    left_list = lst[:n]
    right_list = lst[n:]

    if len(right_list) <= 2:
        r_max = max(right_list)
        l_max = max(left_list)
        if r_max > l_max:
            return r_max
        else:
            return l_max

    if len(right_list) >= 3:
        return func(left_list)


if __name__ == '__main__':
    lst = [11, 2, 33, 4, 55]

    res1 = solve(lst)
    res2 = func(lst)
    print(res1)
    print(res2)



























