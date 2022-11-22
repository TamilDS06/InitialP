class armath:
    
    def __init__(self, num, start, end):
        self.num = num
        self.start = start
        self.end = end

    # prime number or not => int(1) <= bool(1)
    def is_prime(self,num):
        num = int(num)
        if num > 1:
            for i in range(2,num):
                if num % i != 0:
                    continue
                else:
                    return False
        return True

    #prime numbers between specified range => int(2),<= list(1)
    def cal_prime(self):
        prime_list = []
        for i in range(self.start,self.end+1):
            if self.is_prime(i):
                prime_list.append(i)
        return prime_list

    # to seperate odd or even in given range => int(2),<= dict(1)
    def odd_even(self):
        odd_list = []
        even_list = []
        for i in range(self.start, self.end+1):
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
        mergerd_odd_even = [(i, 'even' if i%2 == 0 else 'odd') for i in range(self.start, self.end+1)]
        return {"Odd_list":odd_list, 'Even_list':even_list, 'merged_odd_even_list':mergerd_odd_even}


    