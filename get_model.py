import sys
import json
import subprocess

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

for i,link in enumerate(links):
    src = models[link]
    command = f"kaggle kernels output {src} -p ml/models/"
    print(f"Downloading {i+1}/{len(links)}")
    print(command)
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print("Command executed successfully:")
            print(result.stdout)
        else:
            print("Command failed with error:")
            print(result.stderr)
    except Exception as e:
        print("An error occurred:", str(e))
