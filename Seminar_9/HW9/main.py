import get_sqr
from star_funk import statr_funk
from save_json import funk_save_json

@funk_save_json
@statr_funk('gen_kt_abc')
def start_sqr(**kwargs):
    return get_sqr(**kwargs)


start_sqr()

