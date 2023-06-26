# INTERVIEW LOGIC QUESTIONS.


print("_____________________________________________________________________")
given_str = "helloworld"
if len(given_str) % 2 == 0:
    first_half = given_str[0:int(len(given_str)/2)]
    secon_half = given_str[int(len(given_str)/2):int(len(given_str))]
    print(first_half,secon_half)
    vowel_str = 'AaEeIiOoUu'
    first_half = [i for i in first_half if i in vowel_str]
    secon_half = [i for i in secon_half if i in vowel_str]
    if len(first_half) == len(secon_half):
        print(True)
    else:
        print(False)
else:
    print("Length is odd.")


print("_____________________________________________________________________")
count = 1
result_dict = {}
given_str = 'babcddc'
given_str_list = [i for i in given_str]
for i in range(len(given_str_list)-1):
    current_str = given_str_list[i]
    cc = 0
    for j in given_str_list:
        if j == current_str:
            result = given_str_list[i+1: cc]
            if len(result) != 0:
                result_dict[count] = result
                count += 1
        cc += 1
print(result_dict)

key_ = ''
length_ = 0
for (key,value) in result_dict.items():
    length = len(value)
    if length > length_:
        length_ = length
        key_ = key
print(result_dict[key_])


print("_____________________________________________________________________")
given_str = 'aabbcca'
given_str = [i for i in given_str]
result = ''
for i in range(len(given_str)-1):
    for j in given_str:
        if j == given_str[i+1]:
            result = given_str.count(given_str[i])
    count = 1
    print(given_str.count(given_str[i]))
    if given_str[i] == given_str[i+1]:
        count += 1
        result = result + str(count) + given_str[i]
print(result)


