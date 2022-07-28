from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
import time

if __name__ == '__main__':
    loger = 0
    while loger <= 100:
        time.sleep(0.25)
        print('Loading', loger, '%')
        loger += 10
    print('Loading successful! :)\n')
    get_employees()
    calculate_salary()
    today = datetime.today().replace(microsecond=0)
    print(today.isoformat(' '))