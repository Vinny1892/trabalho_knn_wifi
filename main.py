import pandas as pd

df = pd.read_pickle('utils/wifi_dict.pkl')
pd2 = pd.DataFrame(df[0])
print(pd2.head())