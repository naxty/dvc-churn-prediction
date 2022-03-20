> dvc run -n xgboost_training \
       -d src/xgboost_train.py -d data/train_processed.csv \
       -o models/xgboost.joblib \
       python src/xgboost_train.py

> git add dvc.yaml dvc.lock
> git commit -m "Execute xgboost_training stage"