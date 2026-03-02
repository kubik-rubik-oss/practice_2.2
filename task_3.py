import requests
import json

list_groups = {}

def viewing_all_currencies(data):
    print("\nКод, Имя, Номинал, Стоимость")

    for code, info  in data['Valute'].items():
        name = info['Name']
        nominal = info['Nominal']
        value = info['Value']
        print(f"{code}, {name}, {nominal}, {value} руб.")

def viewing_specific_currency(data):
    choice_id = input("Введите ID валюты, которую хотите посмотреть: ").upper()

    for code, info in data['Valute'].items():
        name = info['Name']
        nominal = info['Nominal']
        value = info['Value']
        if choice_id == code:
            print(f"{code}, {name}, {nominal}, {value} руб.")
            return
    print("Ошибка: валюта не найдена!")

def create_group_currency():
    global list_groups

    create_group = input("Введите название группы с валютами: ").lower()

    if create_group in list_groups:
        print(f"Ошибка: группа '{create_group}' уже существует!")
    else:
        list_groups[create_group] = []
        print(f"Группа '{create_group}' создана")

    print("\nДоступные группы:")
    if list_groups:
        for group in list_groups.keys():
            print(group)
    else:
        print("(нет групп)")
        return

    choice_group = input("Выберите группу: ").lower()

    if choice_group in list_groups:
        while True:
            add_currency = input("Введите код валюты (или 'стоп' для завершения): ").upper()

            if add_currency == 'СТОП':
                break
            currency_found = False
            for code, info in data['Valute'].items():
                if code == add_currency:
                    name = info['Name']
                    nominal = info['Nominal']
                    value = info['Value']
                    exists = False
                    for currency in list_groups[choice_group]:
                        if currency['code'] == code:
                            exists = True
                            print(f"Валюта {code} уже есть в группе!")
                            break
                    if not exists:
                        currency_info = {
                            'code': code,
                            'name': name,
                            'nominal': nominal,
                            'value': value
                        }
                        list_groups[choice_group].append(currency_info)
                        print(f"Валюта {code} ({name}) добавлена в группу '{choice_group}'")
                    currency_found = True
                    break
            if not currency_found:
                print("Ошибка: валюта с таким кодом не найдена!")

        if list_groups[choice_group]:
            print(f"\nГруппа '{choice_group}':")
            for currency in list_groups[choice_group]:
                print(f"  {currency['code']}: {currency['name']} - {currency['value']} руб.")
        else:
            print(f"\nГруппа '{choice_group}' пуста")

    else:
        print("Ошибка: группа не найдена!")

def viewing_list_groups():
    global list_groups

    if not list_groups:
        print("Нет созданных групп")
        return

    for group_name, currencies in list_groups.items():
        print(f"\n{group_name}:")
        if currencies:
            for currency in currencies:
                print(f"{currency['code']}: {currency['name']} - {currency['value']} руб.")
        else:
            print("(группа пуста)")

def change_list_groups():
    global list_groups

    if not list_groups:
        print("Ошибка: нет созданных групп!")
        return
    print("\nДоступные группы:")
    for group in list_groups.keys():
        print(group)

    choice_group = input("\nВыберите группу: ").lower()

    if choice_group not in list_groups:
        print("Ошибка: группа не найдена!")
        return

    print(f"\nГруппа '{choice_group}':")
    if list_groups[choice_group]:
        for currency in list_groups[choice_group]:
            print(f"{currency['code']}: {currency['name']}")
    else:
        print("(группа пуста)")

    print("1. Добавить валюту")
    print("2. Удалить валюту")
    print("3. Отмена")

    action = input("Ваш выбор: ")

    if action == "1":
        add_currency = input("Введите код валюты: ").upper()
        currency_found = False

        for code, info in data['Valute'].items():
            if code == add_currency:
                exists = False
                for currency in list_groups[choice_group]:
                    if currency['code'] == code:
                        exists = True
                        print(f"Валюта {code} уже есть в группе")
                        break
                if not exists:
                    currency_info = {
                        'code': code,
                        'name': info['Name'],
                        'nominal': info['Nominal'],
                        'value': info['Value']
                    }
                    list_groups[choice_group].append(currency_info)
                    print(f"Валюта {code} ({info['Name']}) добавлена в группу")
                currency_found = True
                break
        if not currency_found:
            print("Ошибка: валюта с таким кодом не найдена!")

    elif action == "2":
        if not list_groups[choice_group]:
            print("Ошибка: группа пуста, нечего удалять!")
            return
        del_currency = input("Введите код валюты для удаления: ").upper()
        found = False
        for i, currency in enumerate(list_groups[choice_group]):
            if currency['code'] == del_currency:
                del list_groups[choice_group][i]
                print(f"Валюта {del_currency} удалена из группы")
                found = True
                break
        if not found:
            print("Ошибка: валюта с таким кодом не найдена в группе!")

    elif action == "3":
        print("Отмена")

    else:
        print("Ошибка: неверный выбор!")

def save_list_groups():
    global list_groups

    if not list_groups:
        print("Ошибка: сохранять нечего!")
        return
    print("Группы сохранились в файл save.json\n")

    with open("resource/save.json", "w") as file:
        json.dump(list_groups, file)
    print("Содержимое файла save.json:")

    with open("resource/save.json", "r") as file:
        saved_data = json.load(file)
        for group_name, currencies in saved_data.items():
            print(group_name)
            if currencies:
                for currency in currencies:
                    print(f"{currency['code']}: {currency['name']} - {currency['value']} руб.")
            else:
                print("(пусто)")


def load_list_groups():
    global list_groups

    with open("resource/save.json", "r") as file:
        list_groups = json.load(file)
    print("Группы успешно загружены из файла save.json")

    if list_groups:
        print("\nЗагруженные группы:")
        for group_name, currencies in list_groups.items():
            print(f"{group_name}:")
            if currencies:
                for currency in currencies:
                    print(f"{currency['code']}: {currency['name']} - {currency['value']} руб.")
            else:
                print("(группа пуста)")
    else:
        print("Файл пуст или не содержит групп")

url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url, timeout = 5)
response.encoding = 'utf-8'
data = response.json()

while True:
    print("1. Текущий курс всех валют")
    print("2. Просмотр отдельной валюты по её коду")
    print("3. Создание группы с валютами")
    print("4. Просмотр групп с валютами")
    print("5. Изменение групп с валютами")
    print("6. Сохранение группы с валютами в файле save.json")
    print("7. Загрузить созданные группы из файла save.json")
    print("8. Выход")

    user_choice = input("Выберите действие: ")

    if user_choice == "1":
        viewing_all_currencies(data)
    elif user_choice == "2":
        viewing_specific_currency(data)
    elif user_choice == "3":
        create_group_currency()
    elif user_choice == "4":
        viewing_list_groups()
    elif user_choice == "5":
        change_list_groups()
    elif user_choice == "6":
        save_list_groups()
    elif user_choice == "7":
        load_list_groups()
    elif user_choice == "8":
        print("Вы вышли")
        break
    else:
        print("Ошибка: введите 1, 2, 3, 4, 5, 6, 7 или 8!")