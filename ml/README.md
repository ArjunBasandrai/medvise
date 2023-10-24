## Instructions to download the models

### Setup Kaggle API
- [Create a Kaggle account](https://www.kaggle.com/account/login?phase=startRegisterTab) if you dont have one
- Go to your [Account](https://www.kaggle.com/settings/account) page and click on `Create New Token`
- This will download a `kaggle.json` file
  - For Windows Users: Put the `kaggle.json` file in `C:\Users\<Windows-username>\.kaggle\` directory
  - For Linux/OSX Users: Put the `kaggle.json` file in `~/.kaggle/` directory

### Install dependencies
- Run `pip install -r requirements.txt` command to install all dependencies

### Download model(s)
- Run the `get_model.py` script in the root directory using `python get_model.py model <specify-models>`
- Replace `<specify-models>` using the following codes:
  - `all` to download all available models
  - `kidney` to download the Kidney Cancer Classification model
  - `cervix` to download the Cervix Cancer Classification model
  - `alzheimer` to download the Alzheimer Classification model
  - `monkeypox` to download the Monkeypox Classfication model
  - `tubercolosis` to download Tubercolosis Classification model
  - `covid_x_ray` to download Covid X Ray Classification model


## Training Script

The training scripts in this repository were initially developed on Kaggle. The links to which can be found below :-

- <a href="https://www.kaggle.com/code/arjunbasandrai/kidney-cancer-classification-99-5" target="_blank">Kidney Cancer Classification</a>
- <a href="https://www.kaggle.com/code/arjunbasandrai/cervical-cancer-classification-99-15" target="_blank">Cervical Cancer Classification</a>
- <a href="https://www.kaggle.com/code/madbonze/alzheimer-detection-mri" target="_blank">Alzheimer Classification</a>
- <a href="https://www.kaggle.com/code/madbonze/monkeypox-classification" target="_blank">Monkeypox Classification</a>
- <a href="https://www.kaggle.com/code/madbonze/tubercolosis-classification-x-ray" target="blank">Tubercolosis Classification</a>
- <a href = "https://www.kaggle.com/code/madbonze/covid-classification-x-ray" target="blank">Covid X Ray Classification</a>


**NOTE**: Models will be downloaded in the `ml/models/` directory

## Kaggle Dataset

The training data used in this script can be found [here](https://www.kaggle.com/datasets/arjunbasandrai/medical-scan-classification-dataset)
