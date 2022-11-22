class armath:
    def __init__(self,num):
        self.num = num
    #prime number or not => int(1) <= bool(1)
    def is_prime(self,num):
        num = int(num)
        if num > 1:
            for i in range(2,num):
                if num % i != 0:
                    continue
                else:
                    return False
        return True

    # c = is_prime(44)
    # print(c)

    #prime numbers between specified range => int(2),<= list(1)
    def cal_prime(self, start, end):
        prime_list = []
        for i in range(start,end+1):
            if self.is_prime(i):
                prime_list.append(i)
        return prime_list

    # lst = cal_prime(10,37)
    # print(lst)


    # to seperate odd or even in given range => list(1),<= list(2)
    def odd_even(self, start, end):
        odd_list = []
        even_list = []
        for i in range(start, end+1):
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
        mergerd_odd_even_dict = {i for i in range(start, end+1)}
        return {"Odd_list":odd_list,'Even_list':even_list}
