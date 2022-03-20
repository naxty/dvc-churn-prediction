from catboost import CatBoostClassifier
import pandas as pd
from joblib import load, dump
import pickle

# pipeline = pickle.load(open("models/preprocessing_pipeline.pkl", "rb"))

clf = CatBoostClassifier()

train_df = pd.read_csv("data/train_processed.csv")


X = train_df[train_df.columns.drop('Exited')]
y = train_df["Exited"]
clf.fit(X, y)


dump(clf, "models/catboost.joblib")


