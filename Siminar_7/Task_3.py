"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.

"""


def mult_digit(name, num):
    result = 'result.txt'
    with(open(name, 'r', encoding='utf-8') as f_name,
         open(num, 'r', encoding='utf-8') as f_num,
         open(result, 'a', encoding='utf-8')as f_res
        ):
        while res_num := f_num.readline():
             line_num = f_num.tell()
        f_num.seek(0)
        while res_name := f_name.readline():
             line_name = f_name.tell()
        f_name.seek(0)
        max_line = max(line_num, line_name)

        for _ in range(max_line):
            res_num = f_num.readline()
            dig_1, dig_2 = res_num.split('|')

            res_mult = int(dig_1) * float(dig_2)
        # print(res_mult)
            if f_num.tell() == line_num:
                 f_num.seek(0)


            res_name = f_name.readline()
            if res_mult < 0:
                res_name = res_name.lower()
                f_res.write(f'{res_name} {abs(res_mult)}\n')
            elif res_mult > 0:
                res_name = res_name.upper()
                f_res.write(f'{res_name} {round(res_mult, 0)}\n')

            if f_name.tell() == line_name:
                f_name.seek(0)


if __name__ == '__main__':
    name = 'file_name.txt'
    num = 'file_num.txt'
    mult_digit(name, num)

