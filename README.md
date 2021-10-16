# DVC - DL - TF - AIOPS demo

download data ---> [source](https://drive.google.com/drive/u/0/folders/1tz4IOoJKdi999IRdqJY04VOifyllRzj1)

## commnads - 

### create a new env
```bash
conda create --prefix python=3.7 -y
```

### activate new env
```bash
source activate ./env
```

### init DVC
```bash
dvc init
```

### init GIT
```bash
git init
```

### create empty files - 
```bash
mkdir -p config src/utils
touch src/__init__.py src/utils/__init__.py params.yaml dvc.yaml config/config.yaml src/stage_01_load_save.py src/utils/all_utils.py setup.py .gitignore
```
