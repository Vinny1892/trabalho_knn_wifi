import pickle as pkl
import pandas as pd
with open("wifi_dict.pkl", "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(object)
df.to_csv('./dataset.csv')