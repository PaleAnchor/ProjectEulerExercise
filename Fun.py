import numpy as np


def is_prime(num):  # 检验素数函数
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if (num % 2 == 0) or (num % 3 == 0):
        return False
    for i in range(5, num, 6):
        if num % i == 0:
            return False
        if i + 2 < num and num % (i + 2) == 0:
            return False
    return True


def factor_num(num):  # 计算因子数量函数
    factorNum = 0
    for i in range(1, int(np.sqrt(num))):
        if num % i == 0:
            factorNum = factorNum + 2
    return factorNum


def add(ori_num: list, add_num: list):  # 超大数相加
    while len(ori_num) != len(add_num):
        if len(ori_num) > len(add_num):
            add_num.append(0)
        else:
            ori_num.append(0)
    sum_num = [0] * len(ori_num)
    for i in range(0, len(add_num)):
        if ori_num[i] + add_num[i] <= 9:
            sum_num[i] = sum_num[i] + ori_num[i] + add_num[i]
        else:
            sum_num[i] = ori_num[i] + add_num[i] + sum_num[i] - 10
            if i != len(ori_num) - 1:
                sum_num[i + 1] = sum_num[i + 1] + 1
            else:
                sum_num.append(1)
    return sum_num
