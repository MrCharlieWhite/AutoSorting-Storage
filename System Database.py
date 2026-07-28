import json
from pathlib import Path

a = Path("AutoSortDatabase.JSON")
if a.exists():
    with open('AutoSortDatabase.JSON', 'r') as jsonfile:
        fullDatabase = json.load(jsonfile)
else:
    fullDatabase = [
        [{i: "" for i in range(5)} for _ in range(3)]
        for _ in range(20)
    ]
# Iterating through all dimensions in the database array




# Way to easily update data within the array via narrowing parameters down
sector = int(input("Enter sector (0-19): "))
unit = int(input("Enter unit (0-2): "))
module = int(input("Enter module (0-4): "))
value = input("Enter new value: ")

# Updating the array
fullDatabase[sector][unit][module] = value

# Printing changes
print(fullDatabase[sector][unit])

# Updating the JSON File
with open("AutoSortDatabase.JSON", "w") as f:
    json.dump(fullDatabase, f)
