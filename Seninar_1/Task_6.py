'''
дание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''

START_SUM = 0

def add_money(account):
    pass

def pop_money(account):
    pass

def exit(account):
    return account

def valid_oper ():
    while True:
        sum_oper = int(input('введите сумму кратную 50'))
        if sum_oper % 50 == 0:
            break
        return sum_oper


account = START_SUM

while True:
    choice = input('Выберите дествие (1-пополнить, 2-снять, выйти сумма операции кратна 50')
    match choice:
        case '1':
            cahe_oper = valid_oper()
            add_money(account, cahe_oper)
        case '2':
            pop_money(account)
        case '3':
            exit(account)
