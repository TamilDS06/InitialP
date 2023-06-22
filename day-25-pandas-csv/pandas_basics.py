# import csv
#
# with open('weather_data.csv', mode='r') as data_file:
#     data_file = csv.reader(data_file)
#     temperature_list = []
#     total_list = []
#     print(data_file)
#     for row in data_file:
#         if row[1] != 'temp':
#             temperature_list.append(int(row[1]))
# print(temperature_list)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data['temp'])
print(type(data))

data_dict = data.to_dict()
print(data_dict)

data_list = data['temp'].to_list()
print(data_list)

temp_mean = data['temp'].mean()
print(temp_mean)

max_temp = data['temp'].max()
print(max_temp)

# Get column in data
print(data['temp'])
print(data.temp)

# Get row in data
print(data[data.day == 'Monday'])
print(data[data.temp == data['temp'].max()])

monday = data[data.day == 'Monday']
print(monday.condition)
print((int(monday.temp)*(9/5))+35)

# create dataframe from scratch

data_dict = {
    'name': ['T', 'J', 'G'],
    'Age': [26, 24, 22]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('my_data.csv')

