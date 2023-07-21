import json

class Model:
    def __init__(self):
        pass


def save_json(path,data):
    file = open(path,'w')
    json.dump(file, path)
    file.close()

def load_json(path):
    file = open(path,'r')
    data = json.load(file)
    file.close()
    return data