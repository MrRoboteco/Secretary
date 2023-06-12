import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print('Текущая дата: ', datetime.datetime.today().strftime('%d.%m.%Y'))
    # Вызываем функции из других модулей
    calculate_salary()
    get_employees()
