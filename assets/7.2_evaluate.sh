> dvc run -n xgboost_evaluation \
       -d src/evaluate.py -d data/test_processed.csv \
       -m metrics.json --plots plots \
       python src/evaluate.py models/xgboost.joblib

> dvc metrics show
Path          accuray    f1                                           
metrics.json  0.82467    0.4207   
