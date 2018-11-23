# 分治法；二分查找

def func(lst,k):
    return lst[0] == k


def solve(lst,k):
    if len(lst) == 1:
        return func(lst,k)

    m = len(lst)//2
    left_list = lst[:m]
    right_list = lst[m:]

    # or:从左边开始算，算完后，没出结论，再算or右边
    return solve(left_list,k) or solve(right_list,k)



if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    k = int(input('输入一个数：'))

    re = solve(lst, k)
    print(re)





























