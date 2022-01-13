print(2**3) # 2^3
def raise_to_power(base_num,pow_num):
    res = 1
    for index in range(pow_num):
        res = res * base_num
    return res

print(raise_to_power(3,3))