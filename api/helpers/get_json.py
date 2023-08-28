import simplejson as json

def get_json(path: str):
    with open(path, encoding="utf8") as f:
        return json.load(f)
