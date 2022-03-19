from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from sklearn.preprocessing import RobustScaler
from joblib import dump, load
import pickle


non_scaling_columns = ["Geography_Germany", "Geography_Spain", "HasCrCard","IsActiveMember", "Exited"]
train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

scaler = RobustScaler()

def feature_engineering(df):

    df["CreditsScore"] = pd.qcut(df['CreditScore'], 10, labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    df["BalanceScore"] = pd.qcut(df['Balance'].rank(method="first"), 10, labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    df["SalaryScore"] = pd.qcut(df['EstimatedSalary'], 10, labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    df["MonthlySalary"] = df["EstimatedSalary"] / 12

    df = pd.get_dummies(df, columns =["Geography"], drop_first = True)

    return df


def scale_features(df, is_training_data=False):

    index = df.index
    non_scaling_df = df[non_scaling_columns]
    scaling_df = df.drop(non_scaling_columns, axis = 1)
    cols = scaling_df.columns

    if is_training_data:
        X = scaler.fit_transform(scaling_df)
    else:
        X = scaler.transform(scaling_df)

    X = pd.DataFrame(X, columns = cols, index = index)
    X = pd.concat([X, non_scaling_df], axis = 1)
    return X


train_df = feature_engineering(train_df)
test_df = feature_engineering(test_df)
train_df = scale_features(train_df, is_training_data=True)
test_df = scale_features(test_df, is_training_data=False)


train_df.to_csv("data/train_processed.csv", index=False, sep=",")
test_df.to_csv("data/test_processed.csv", index=False, sep=",")
