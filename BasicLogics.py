def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i != 0:
                continue
            else:
                return False
    return True

# c = is_prime(44)
# print(c)

def cal_prime(start,end):
    prime_list = []
    for i in range(start,end):
        if is_prime(i):
            prime_list.append(i)
    return prime_list