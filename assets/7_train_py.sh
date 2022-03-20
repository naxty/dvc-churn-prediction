touch src/xgboost_train.py

from xgboost import XGBClassifier
import pandas as pd
from joblib import load, dump
import pickle

clf = XGBClassifier()

train_df = pd.read_csv("data/train_processed.csv")

X = train_df[train_df.columns.drop('Exited')]
y = train_df["Exited"]
clf.fit(X, y)


dump(clf, "models/xgboost.joblib")


