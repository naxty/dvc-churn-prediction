import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve
import json
import seaborn as sns
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython evaluate.py path_to_model \n")
    sys.exit(1)

model_file = sys.argv[1]
clf = load(model_file)
import os
if not os.path.exists("plots"):
    os.mkdir("plots")
test_df = pd.read_csv("data/test_processed.csv")

X_test = test_df[test_df.columns.drop("Exited")]
y_test = test_df["Exited"]
y_pred = clf.predict(X_test)

results = {
    "f1":  f1_score(y_test, y_pred),
    "accuray": accuracy_score(y_test, y_pred)
}

json.dump(results, open("metrics.json", "w"))

feature_imp = pd.Series(clf.feature_importances_,
                        index=X_test.columns).sort_values(ascending=False)

sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title("Feature Importance")
plt.savefig("plots/feature_importance.png")

plot_confusion_matrix(clf, X_test, y_test)
plt.savefig("plots/confusion_matrix.png")
plot_roc_curve(clf, X_test, y_test)
plt.savefig("plots/roc.png")
