import argparse
import json
import tempfile
import os


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as f:
        content = f.read()
        if content:
            return json.loads(content)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def store(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def retrieve(storage_path, key):
    data = read_data(storage_path)
    print(*data.get(key, []), sep=', ')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Desired key to add/get a value',
                        required=True)
    parser.add_argument('--value', help='Desired value to store')
    return parser.parse_args()


def _main():
    """
    Key-value storage implementation
    :return:
    """
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    args = parse_args()
    if args.value:
        store(storage_path, args.key, args.value)
    else:
        retrieve(storage_path, args.key)


if __name__ == '__main__':
    _main()
