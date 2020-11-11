import datetime

from Programmer import Programmer


def get_avg_salary(company_name):
    devs = companies.get(company_name)
    avg_salary = 0
    for i in devs:
        a = i.get_salary()
        avg_salary += a

    return avg_salary / len(devs)


def get_cheapest_proj(company_name):
    devs = companies.get(company_name)
    min = float("inf")
    projects = {}
    for i in devs:
        if projects.get(i.project) is None:
            projects[i.project] = i.get_salary()
        else:
            projects[i.project] += i.get_salary()
    for j in projects:
        if projects.get(j) < min:
            min = projects.get(j)
    for key, value in projects.items():
        if value == min:
            return key


companies = {}
print('How many people you wold like to add')
n = int(input())

for i in range(0, n):
    print('Person number ', i)
    print('Enter Name: ')
    name = input()
    print('Enter Surname: ')
    surname = input()
    print('Enter Fathers name: ')
    father_name = input()

    print('Enter Company: ')
    company = input()
    print('Enter Specialisation: ')
    spec = input()
    print('Enter Position: ')
    pos = input()
    print('Enter Project: ')
    proj = input()
    print('Enter Salary: ')
    sal = input()
    print('Enter Birth day: ')
    birth_day = datetime.datetime.strptime(input(), '%d.%m.%Y').date()
    if companies.get(company) is None:
        a = []
        b = Programmer(name, surname, father_name, birth_day, company, spec, pos, sal, proj)
        a.append(b)
        companies[company] = a
    else:
        b = Programmer(name, surname, father_name, birth_day, company, spec, pos, sal, proj)
        a = companies.get(company)
        a.append(Programmer(name, surname, father_name, birth_day, company, spec, pos, sal, proj))
        companies[company] = a


print('Enter company you`r interested in: ')
comp = input()
print(get_avg_salary(comp))
print('Cheapest project: ', get_cheapest_proj(comp))


