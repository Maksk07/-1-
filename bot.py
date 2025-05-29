import os
import time
from datetime import date, datetime, timedelta


def clear_console(): #очищення консолі
    os.system('cls')

def exit_pr(): #вихід з програми
    start = 0
    return start

def prhelp(): #вивести команди
    clear_console()
    print('команди:\nВийти - 1\nЗмінити розклад - 2\nВвести дз - 3\nВивести розклад на поточний день - 4\nВивести розклад на завтра - 5\nПодивитися наявне дз - 6\n')

def rozkladinput(): #ввести/змінити розклад
    for i in rozklad.keys():
        k = int(input(f'Введіть кількість предметів у {i}: '))
        rozklad[i] = [] #
        for i1 in range(k):
            predmet = str(input(f'Введіть назву {i1 + 1} предмету: '))
            rozklad[i].append(predmet)
    print(rozklad)
    str(input('Натисніть Enter щоб вийти: '))

def dzinput(): #ввести дз 
    i = 1
    while(i):
        predmet = str(input('Введіть назву предмету з якого задали дз: '))
        deadline1 = str(input('Введіть дату на яку задали дз(ДД.ММ.РРРР): '))
        deadline = datetime.strptime(deadline1, '%d.%m.%Y').date()
        dz = str(input('Введіть короткий опис домашнього: '))
        if deadline not in taskdict:
            taskdict[deadline] = {}
        taskdict[deadline][predmet] = dz
        i = int(input('Введіть 1 щоб продовжити вводити дз або 0 щоб закінчити: '))

def rozkladtoday(): #вивести розклад на поточний день
    print('Розклад на сьогодні:\n')
    if todayd in rozklad:
        for i in rozklad[todayd]:
            print(f'{i}')
    else:
        print(f'Сьогодні {todayd}')

def rozkladtomorow(): #вивести розклад на завтра
    print('Розклад на завтра:\n')
    if tomorrowd in rozklad:
        for i in rozklad[tomorrowd]:
            print(f'{i}')
    else:
        print(f'Завтра {tomorrowd}')

def actualdz(): #подивитися наявне дз
    for i in taskdict.keys():
            for i1 in taskdict[i].keys():
                if i >= today: #перевірка на актуальність
                    print(f'на {i} з предмету - {i1} задано: {taskdict[i][i1]}')
                else:
                    print(f'на {i} з предмету - {i1} було задано: {taskdict[i][i1]}')


def reminder(): #нагадування
    print('Нагадування:')
    for i in taskdict.keys():
        if i == today:
            for i1 in taskdict[i].keys():
                print(f'На сьогодні з предмету {i1} задано: {taskdict[i][i1]}')
        elif i == tomorrow:
            for i2 in taskdict[i].keys():
                print(f'На завтра з предмету {i2} задано: {taskdict[i][i2]}')

today = date.today()
tomorrow = today + timedelta(days=1)
taskdict = {}
t = date.today()
day_number = t.weekday()
days = {
    0: 'Понеділок',
    1: 'Вівторок',
    2: 'Середа',
    3: 'Четвер',
    4: "П'ятниця",
    5: 'Субота',
    6: 'Неділя'
}
todayd = days[day_number]
if day_number < 6:
    tomorrowd = days[day_number + 1]
else:
    tomorrowd = days[0]
rozklad = {
    'Понеділок':[], 
    'Вівторок':[], 
    'Середа':[], 
    'Четвер':[], 
    "П'ятниця":[]
    }
start = bool(input('Введіть один щоб запустити програму... '))
print('Вітаю користувачу!')
time.sleep(2) #затримка щоб прочитати вітання
rozkladinput()
while(start):
        print(f'День тижня: {today}')
        print('0 - вивести команди')
        print('---------------------------')

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        reminder()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        action = (int(input('Введіть дію: ')))
        if action == 0: #вивести команди
            prhelp()
            print('---------------------------')
            str(input('Натисніть Enter щоб вийти: '))

        if action == 1: #вихід з програми
            start = exit_pr()
        
        if action == 2: #змінити розклад
            rozkladinput()
            print(rozklad)
            print('---------------------------')
        
        if action == 3: #ввести дз
            dzinput()
        
        if action == 4: #подивитися розклад на сьогодні
            rozkladtoday()
            print('---------------------------')
            str(input('Натисніть Enter щоб вийти: '))
        if action == 5: #подивитися розклад на завтра
            rozkladtomorow()
            print('---------------------------')
            str(input('Натисніть Enter щоб вийти: '))
        if action == 6: #подивитися наявне дз
            actualdz()
            print('---------------------------')
            str(input('Натисніть Enter щоб вийти: '))


        clear_console()