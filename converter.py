import json
import pandas as pd
import chardet


def detect_encoding(filepath):
    try:
        with open(filepath, 'rb') as f:
            result = chardet.detect(f.read())
        return result['encoding']

    except FileNotFoundError:
        return 'file not found'
    except Exception as e:
        return f'error: {e}'

try:
    with open('data.json', 'r', encoding=detect_encoding('data.json')) as f:
        data = json.load(f)
        df = pd.DataFrame(data)
        df.to_excel('data.xlsx', index=False)

except Exception as e:
    print(f'error: {e}')


