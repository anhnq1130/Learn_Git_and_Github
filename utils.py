import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def save_data(data, file_path):
    data.to_csv(file_path, index=False)
    return None

def preprocess_data(data):
    '''
    This function will remove any missing values and duplicates from the data.
    
    Parameters:
    data: pandas DataFrame
    
    Returns:
    data: pandas DataFrame
    '''
    data = data.dropna()
    data = data.drop_duplicates()
    return data

def normalize_data(data):
    '''
    This function will normalize the data.
    
    Parameters:
    data: pandas DataFrame
    
    Returns:
    data: pandas DataFrame
    '''
    data = (data - data.mean()) / data.std()
    return data