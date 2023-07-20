"""
Доработаем задачи 3 и 4.
Создайте класс Project, содержащий атрибуты – список пользователей проекта
 и админ проекта. Класс имеет следующие методы:

Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)

Метод входа в систему – требует указать имя и id пользователя.
Далее метод создает пользователя и проверяет есть ли он в списке
пользователей проекта. Если в списке его нет, то вызывается исключение доступа.
Если пользователь присутствует в списке пользователей проекта, то пользователь,
который входит получает его уровень доступа и становится администратором.

Метод добавление пользователя в список пользователей. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня доступа.

* метод удаления пользователя из списка пользователей проекта
* метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
"""
import json

from Task_4 import User
from Task_3 import AccessError, LevelError

class Project:

    def __init__(self, list_user):
        self.list_user = list_user
        self.admim_project = None

    @classmethod
    def load_json (cls, json_file):
            list_user = []
            with open(json_file, 'r', encoding='utf-8') as f_read:
                user_dict = json.load(f_read)

            for level, in user_dict:
                for user_id in user_dict[level]:
                    list_user.append(User(user_dict[level][user_id], user_id, level))

            return Project(list_user)

    # вхид в систему
    def enter(self, user_name, id_user):
        # user_name, id_user = input('введите имя пользователя и id').split(" ")
        user_new = User(user_name, id_user)
        # print(user)
        if user_new not in self.list_user:
            raise AccessError(user_name)

        for user in self.list_user:
             if user == user_new:
                self.admim_project = user

    # добавление пользовалеля
    def add_user(self, user, user_id, level):
        # print((level))
        # print(self.admim_project.level)
        if int(self.admim_project.level) > int(level):
            raise LevelError(user)
        self.list_user.append(User(user, user_id, level))

    # self.admim_project == None or
    def __str__(self):
        return f'пользователи {self.list_user} админ {self.admim_project}'



if __name__ == '__main__':
    p = Project.load_json('user_id.json')
    print(p)
    p.enter('Федор', '3')
    print(p)
    p.add_user('Степан', '7', '7')
    print(p)
    # p.add_user('Илья', '8', '1')
    print(p)
