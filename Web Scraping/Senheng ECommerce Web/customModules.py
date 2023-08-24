import pandas as pd

def list_dict_to_excel(list_dict):    
    df = pd.DataFrame.from_dict(list_dict)
    df.to_excel('result.xlsx', index=False)