> dvc add data/raw.csv
# Folgender Befehl wird direkt von DVC generiert und
# muss manuell ausgeführt werden, um die Daten im
# im Repository zu tracken
> git add data/.gitignore data/raw.csv.dvc
> cat data/raw.csv.dvc
outs:
- md5: 7321aa9a1e24a9e139f42124f736b415
  size: 684858
  path: raw.csv