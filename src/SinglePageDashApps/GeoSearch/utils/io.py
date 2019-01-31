import json

def JSON_write(config, to_file):

    with open(to_file, 'w') as f:
        json.dump(config, f)

def JSON_update(config, to_file):

    with open(to_file, 'a') as f:
        json.dump(config, f)

def JSON_read(from_file):

    with open(from_file, 'r') as f:
        config = json.load(f)
        f.close()
        return config

def func_name():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]

def cat(filepath):
    with open(filepath) as f:
        res = f.read()
    return res
