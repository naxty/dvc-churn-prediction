dvc run -n preprocess \
        -d src/preprocess.py -d data/train.csv -d data/test.csv \
        -o data/train_processed.csv -o data/test_processed.csv \
        python src/preprocess.py

git add src/preprocess.py
git add dvc.yaml data/.gitignore dvc.lock
git commit -m "Execute preprocess stage"