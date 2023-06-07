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
DEV = 50
BONUS_VALUE = 0.03
count =0

def add_money(account, sum_tranz, bonus):
    if bonus:
        account = account + round(sum_tranz * BONUS_VALUE, 2)
    else: account = account + sum_tranz
    return account

def pop_money(account, sum_tranz):
    return account

def exit(account):
    print(f'останток на счете  {account}')


def valid_oper (dev):
    global DEV
    while True:
        sum_oper = int(input(f'введите сумму кратную {dev}'))
        if sum_oper % DEV != 0:
            break
        return sum_oper


account = START_SUM

while True:
    choice = input('Выберите дествие (1-пополнить, 2-снять, выйти сумма операции кратна 50')
    flag = False
    match choice:
        case '1':
            cahe_oper = valid_oper(DEV)
            if count % 3 == 0 and count != 0:
                flag = True
            res = add_money(account, cahe_oper, flag)
            print(f'останток на счете  {res}')
        case '2':
            cahe_oper = valid_oper(DEV)
            res = pop_money(account, cahe_oper)
            print(f'останток на счете  {res}')
        case '3':
            exit(account)
            exit()

