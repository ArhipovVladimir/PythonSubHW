"""
Задание №3
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.

"""


class UserException(Exception):
    pass


class LevelError(UserException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'ошибка уровня доступа {self.value}'


class AccessError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'ошибка доступа {self.value}'
