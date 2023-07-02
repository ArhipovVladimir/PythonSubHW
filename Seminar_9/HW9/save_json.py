import json
import os
from typing import Callable
from functools import wraps
def funk_save_json(func):
    file = f'{func.__name__}.json'
    print(file)
    if file in os.listdir():
        with open(file, 'r', encoding='utf-8') as f_json:
            json_file = json.load(f_json)
    else:
        json_file = []

    @wraps(func)
    def wrapper(**kwargs):
        for arg, result in func(**kwargs):
            # if result:
            dct = {'args': arg, 'result': str(result)}
            json_file.append(dct)
            with open(file, 'w', encoding='utf-8') as json_f:
                json.dump(json_file, json_f, indent=2)
        # else:
        #     break

    return wrapper
