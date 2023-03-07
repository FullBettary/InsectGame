import json


path = "notes"


def write(score, t):
    try:
        file_to_read = open(path, "r")
    except FileNotFoundError:
        file_to_read = open(path, 'w')
        file_to_read.close()
        file_to_read = open(path, "r")

    try:
        record = json.loads(file_to_read.read())
    except Exception:
        record = {'score': 0, 'time': 0}

    file_to_read.close()

    try:
        record['score']
    except KeyError:
        record = {'score': 0, 'time': 0}

    if record['score'] < score:
        record['score'] = score
    if record['time'] < t:
        record['time'] = t

    json_str = json.dumps(record)

    file_to_write = open(path, "w")
    file_to_write.write(json_str)
    file_to_write.close()


def read():
    try:
        file_to_read = open(path, "r")
    except FileNotFoundError:
        return 0, 0

    try:
        record = json.loads(file_to_read.read())
    except Exception:
        return 0, 0

    file_to_read.close()

    try:
        record['score']
    except KeyError:
        return 0, 0

    return record['score'], record['time']


def reset():
    file = open(path, "w")

    record = {'score': 0, 'time': 0}

    json_str = json.dumps(record)

    file.write(json_str)

    file.close()


