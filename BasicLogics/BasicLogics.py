from constant import constant
class armath:
    
    def __init__(self, num, start, end):
        try:
            self.num = num
            self.start = start
            self.end = end
        except Exception as exception:
            print("constructor method failed", exception.args)
            constant.error.append({"Module name":"constructor", "Message":"Failed to initialize instance variables"})

    # prime number or not => int(1) <= bool(1)
    def is_prime(self):
        try:
            result = {"IsSuccess":True, "Message":"Is_Prime method failed", str(self.num)+"is Prime?":"yes"}
            self.num = int(self.num)
            if self.num > 1:
                for i in range(2,self.num):
                    if self.num % i != 0:
                        continue
                    else:
                        result['IsSuccess'] = False
                        result[str(self.num)+"is Prime?"] = 'No'
                        return False
            return True
        except Exception as exception:
            print("is_prime method failed", exception.args)
            constant.error.append({"Module name":"is_prime", "Message":result['Message']})

    #prime numbers between specified range => int(2),<= list(1)
    def cal_prime(self):
        try:
            result = {"IsSucces":False, "Prime_List":[], "Message":"Prime Calculation method is failed"}
            for i in range(self.start,self.end+1):
                if self.is_prime(i):
                    result['Prime_List'].append(i)
            result['Message'] = constant.Message.format("Prime Calculation")
            result['IsSucces'] = True
        except Exception as exception:
            print("cal_prime method failed", exception.args)
            constant.error.append({"Module name":"cal_prime", "Message":result['Message']})
        finally:
            return result

    # to seperate odd or even in given range => int(2),<= dict(1)
    def cal_odd_even(self):
        try:
            result = {"IsSuccess":False, "odd_list":[], "even_list":[], 'merged_odd_even_list':[], \
             'Message':"odd_even method failed"}
            for i in range(self.start, self.end+1):
                if i % 2 == 0:
                    result['even_list'].append(i)
                else:
                    result['odd_list'].append(i)
            result['merged_odd_even_list'] = [(i, 'even' if i%2 == 0 else 'odd') for i in range(self.start, self.end+1)]
            result['IsSuccess'] = True
            result['Message'] = constant.Message.format("odd_even Calculation")
        except Exception as exception:
            print("odd_even method failed", exception.args)
            constant.error.append({"Module name":"cal_odd_even", "Message":result['Message']})
        finally:
            return result
