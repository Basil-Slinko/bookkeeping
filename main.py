from application.db import people
from application import salary
from datetime import date

if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    current_date = date.today()
    print(f'\nТекущая дата: {current_date}')