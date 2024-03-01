import json

# Save object in a JSON file
def saveJSON(data: object, file: str) -> None:
  with open(file, 'w') as fp:
      json.dump(data, fp, ensure_ascii=False)

# Load JSON file
def loadJSON(file: str) -> list:
  try:
    with open(file) as json_file:
        data = json.load(json_file)
    return data
  except:
    print("Cound not load %s"%file)
    return []