# simple sample lines for exception handling in python

# try:
#     file = open('data.txt', 'r')
#     sample_dict = {'key': 'value'}
#     value = sample_dict['key']
# except FileNotFoundError as error_message:
#     print(f'{error_message}')
#     file = open('data.txt', 'w')
# except KeyError as error_message:
#     print(f'There is no key that you have entered {error_message}')
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("The file was closed.")

# The raise keyword to raise our own exception
# BMI calculation
weight = int(input("Enter your weight :"))
height = float(input("Enter your height :"))

if height > 3:  # humans might not have height that more than 3 meters.
    raise ValueError("Please enter a valid height.")
bmi = weight / height ** 2
