
import os
import logging
from collections import namedtuple
import argparse


FORMAT = '{msg}'

logging.basicConfig(filename='log1.txt', format=FORMAT, style='{', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)
Object_dir = namedtuple('Object', ['name', 'exemp', 'is_dir', 'path'])



def dir_write(dir_=os.getcwd()):
    os.chdir(dir_)
    # print(dir_)
    list_obj = []
    for obj in os.listdir(os.getcwd()):
        # print(obj)
        if os.path.isdir(obj):
            logger.info(f'{obj} {None} {os.path.isdir(obj)} {os.getcwd()}')
            list_obj.append(Object_dir(obj, None, os.path.isdir(obj), os.getcwd()))
        if os.path.isfile(obj):
            obj, exem = obj.split('.')
            logger.info(f'{obj} {exem} {os.path.isdir(obj)} {os.getcwd()}')
            list_obj.append(Object_dir(obj, exem, os.path.isdir(obj), os.getcwd()))

    # print(list_obj)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='dir info')
    parser.add_argument('args', metavar='path', type=str, help='get dir path', default=os.getcwd())
    args = parser.parse_args()
    # print(args)
    # dir_write(args)
    # dir_write()
    # dir_write('C:\\Users\\arhip\\OneDrive\\Документы\\GB\\Python2\\PythonSubHW\\Seminar_9')
    print(args.args)
    # _, args = argv
    dir_write(args.args)

