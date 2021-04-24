import pickle as pkl
import pandas as pd

object = pd.read_pickle('wifi_dict.pkl')
df = pd.DataFrame(object[0])
df.to_csv('./dataset.csv', index=False)