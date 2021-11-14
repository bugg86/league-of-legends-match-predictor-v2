import json

with open("data/matchDataset.json", "r") as f:
    print(len(json.load(f)))
f.close()