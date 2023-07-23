"""
Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”,
“3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.

"""
from datetime import datetime

def get_date(date_text):
    text_ = f'{datetime.now().year}'
    text_date = datetime.strptime(date_text, f'{text_} %A. Время %H:%M:%S. Это %W неделя и %j день года.')




if __name__ == '__main__':
    print(get_date('1-й четверг ноября')




d = datetime.now()
date_text = 'Дата 15 June 2007. День недели Friday. Время 02:14:00. Это 24 неделя и 166 день года.'
text_date = datetime.strptime(date_text, 'Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.')
print(text_date)
print(d.year)
print(d.weekday())
print(d.day)