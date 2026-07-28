import json

scores = [100, 74, 23, 3]

with open("AutoSortDatabase.JSON", "w") as f:
    json.dump(scores, f)