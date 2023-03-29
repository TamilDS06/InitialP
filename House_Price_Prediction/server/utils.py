from constant import constant
import pickle
import numpy as np
import json

model = None
data_columns = None
locations = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    return round(model.predict([x])[0], 2)

def load_saved_Base():
    print("Load Saved Base... Started")
    global data_columns
    global locations
    global model
    with open(constant.ROOT_DIR+"\\server\\Base\\columns.json", 'r') as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]
    with open(constant.ROOT_DIR+"\\server\\Base\\banglore_home_prices_model.pickle", 'rb') as f:
        model = pickle.load(f)
    print("Load Saved Base... Done")

def get_locations():
    return locations

def get_data_columns():
    return data_columns

if __name__ == '__main__':
    load_saved_Base()
    print(get_locations())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location