import os
import requests
import sys
import json

try:
    args = sys.argv[1:]
    if (args[0] != "model"):
        raise ValueError(f"Invalid argument: {args[0]}")
except:
    raise ValueError("No model argument found")

with open("ml/scripts/models.json", "r") as f:
    models = json.loads(f.read())

for i in args[1:]:
    if i == "all":
        links = list(models.keys())
    else:
        links = []
        for link in args[1:]:
            if link in list(models.keys()):
                links.append(link)
            else:
                raise ValueError(f"Invalid Argument: {link}")
    
save_dir = "ml/models/"
for i,key in enumerate(links):
    link = models[key]
    model = link.split("/")[-1]
    file_name = os.path.join(save_dir, model)

    print(f"Fetching {model} {i+1}/{len(links)}")
    response = requests.get(link)
    
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            print(f"Downloading {model} {i+1}/{len(links)}")
            file.write(response.content)
        print(f"Downloaded model file to {file_name}")
    else:
        print(f"Failed to download model. Status code: {response.status_code}")