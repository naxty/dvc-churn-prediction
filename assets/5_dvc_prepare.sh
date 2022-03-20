> dvc run -n prepare \
        -d src/prepare.py -d data/raw.csv \
        -o data/train.csv -o data/test.csv \
        -p seed \
        python src/prepare.py

> git add dvc.yaml data/.gitignore dvc.lock
> git commit -m "Execute prepare stage"