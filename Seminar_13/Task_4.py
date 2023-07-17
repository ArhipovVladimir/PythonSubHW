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

    def __init__(self, user, user_id, level=None):
        self.user_id = user_id
        self.user = user
        self.level = level

    def __eq__(self, other):
        return self.user == other.user and self.user_id == other.user_id

    def __str__(self):
        return f'польз {self.user} id {self.user_id} уровень {self.level}'

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #         return self

        # raise StopIteration





if __name__ == '__main__':
    u1 = User("1", "Владимир", "1")
    u2 = User("4", "Никита", "1")
    u3 = User("4", "Никита", "1")
    u4 = User("2", "Иван", "1")
    u5 = User("2", "Иван", "1")
    print(u1 == u2)
    print(u3 == u2)
    print(u3 == u4)
    print(u4 == u5)
    print(u1, u2, u3, u4, u5, sep='\n')