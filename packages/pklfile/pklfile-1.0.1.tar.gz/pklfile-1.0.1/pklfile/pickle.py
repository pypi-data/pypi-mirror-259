import pickle

def read(path):
    with open(path, "rb") as f:
        file = pickle.load(f, encoding='latin1')

def write(data, path):
    with open(path, "wb") as f:
        file = pickle.dump(data, f)
