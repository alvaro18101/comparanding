import pandas as pd

def create_dataset(columns, data):
    df = pd.DataFrame(columns=columns)
    j = 0
    for i in columns:
        df[i] = data[j]
        j += 1
    return df