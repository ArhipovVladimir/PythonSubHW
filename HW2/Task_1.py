"""Здание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""
import decimal

START_SUM = 0
DEV = 50
BONUS_VALUE = 0.03
COUNT_BONUS_OPER = 3
TASK_RICH = 5000_000
TASK = 0.10
decimal.getcontext().prec=2

def sum_m(sum_tran):
    if sum_tran * 0.015 < 30:
        print(f'за снятие 30')
        return 30
    if sum_tran * 0.015 > 600:
        print(f'за снятие 600')
        return 600

    res_m = round(sum_tran * 0.015, 2)
    print(f'за снятие {res_m}')
    return res_m


def add_money(account_add, sum_tranz, bonus_add):
    if bonus_add:
        return account_add + sum_tranz + round(sum_tranz * BONUS_VALUE, 2)

    return  account_add + sum_tranz


def pop_money(account_pop, sum_tranz, bonus_pop):
    morj = sum_m(sum_tranz)
    res = account_pop + round(sum_tranz * bonus_pop, 2) - morj - sum_tranz
    if res < 0:
        print(f'недостаточно средств баланс - {account_pop}')
        return account_pop

    return res


def valid_oper(dev_sum):
    while True:
        sum_oper = int(input(f'введите сумму кратную {dev_sum}: '))
        if sum_oper % dev_sum == 0:
            return sum_oper


account = START_SUM
count = 1
while True:
    choice = input('Выберите дествие (1-пополнить, 2-снять, 3-выйти): ')
    flag = False
    match choice:
        case '1':
            cahe_oper = valid_oper(DEV)
            if count % COUNT_BONUS_OPER == 0:
                flag = True
            account = add_money(account, cahe_oper, flag)
            print(f'останток на счете  {account}')
            count += 1
        case '2':
            cahe_oper = valid_oper(DEV)
            if count % COUNT_BONUS_OPER == 0:
                bonus = BONUS_VALUE
            else:
                bonus = 0
            account = pop_money(account, cahe_oper, bonus)
            print(f'останток на счете  {account}')
            count += 1
        case '3':
            if account > TASK_RICH:
                print(f'налог  {round(account * TASK, 2)}')
                account = round(account * (1 - TASK), 2)
                print(f'останток на счете  {account}')
            else:
                print(f'останток на счете  {account}')
            exit()
