'''
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

'''
from Seminar_6.Rebus.Task_4 import rebus_todo
import Task_6
def bases_rebus():
    dict_rebus = {'без окон без дверей полна горницъа людей':['огуоец', 'огурчик'],
                  'сто одежек и все без застежек': ['капуста'],
                  'сидет дет во сто шуб одет, кто его раздевает [тот слезы продевает': ['лук']}

    for get_rebus in dict_rebus.items():
        resalt = rebus_todo(get_rebus[0], get_rebus[1])
        if resalt > 0:
             Task_6.save_resalt(get_rebus[0], resalt)


if __name__=='__main__':
    bases_rebus()
    Task_6.output_resalt()





