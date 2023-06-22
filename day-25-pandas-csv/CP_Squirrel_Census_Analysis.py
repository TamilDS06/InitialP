import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data[data['Primary Fur Color'] == 'Gray'])
print(data['Primary Fur Color'].unique())

data_sq_color = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count' : [len(data[data['Primary Fur Color'] == 'Gray']),len(data[data['Primary Fur Color'] == 'Cinnamon']), len(data[data['Primary Fur Color'] == 'Black'])]
}

data_sq_color = pd.DataFrame(data_sq_color)
data_sq_color.to_csv('data_sq_color')