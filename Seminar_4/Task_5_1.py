def make_salary(names, salaries, premiums):
    salary_dict = {}
    for name, salary, premium in zip(names, salaries, premiums):
        salary_dict[name] = salary * float(premium[:-1]) / 100
    return salary_dict


name = ['Петя', 'Вася', 'Маша']
salary = [100_000, 150_000, 200_000]
premium = ['5.25%', '7.5%', '10%']

print(make_salary(name, salary, premium))