> dvc run -n catboost_training \
       -d src/catboost_train.py -d data/train_processed.csv \
       -o models/catboost.joblib \
       python src/catboost_train.py

> dvc run -n catboost_evaluation \
       -d src/evaluate.py -d data/test_processed.csv \
       -m metrics.json --plots plots \
       python src/evaluate.py models/catboost.joblib

> dvc exp run -n exp-catboost
> dvc exp branch exp-catboost exp-catboost
> git add src/catboost_train.py
> git commit -m "Catboost experiment"