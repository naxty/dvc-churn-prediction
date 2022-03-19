import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open("params.yaml"))["prepare"]

columns_to_drop = params["columns_to_drop"]
test_size = params["test_size"]
seed = params["seed"]

df = pd.read_csv("data/raw.csv")

df_columns = df.columns
for column in columns_to_drop:
    assert column in df_columns

df.drop(columns_to_drop, inplace=True, axis=1)
train_df, test_df = train_test_split(df, test_size=test_size, random_state=seed)

train_df.to_csv("data/train.csv", index=False, sep=",")
test_df.to_csv("data/test.csv", index=False, sep=",")

