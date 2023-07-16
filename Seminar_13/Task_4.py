"""
Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Магический метод на равенство пользователей

Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.

"""
class User:

    def __init__(self, user_di, user, level):
        self.user_id = user_di
        self.user = user
        self.level = level

    def __eq__(self, other):
        return self.user_id == other.user_id and self.user == other.user

    def __str__(self):
        return f'польз {self.user} id {self.user_id} уровень {self.level}'


if __name__ == '__main__':
    u1 = User("1", "Владимир", "1")
    u2 = User("4", "Никита", "1")
    u3 = User("4", "Никита", "1")
    print(u1 == u2)
    print(u3 == u2)
    print(u1, u2, u3, sep='\n')