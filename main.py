print("Программа запущена")

request = []

# Логин
users = {'admin': {'password': 'admin123', 'role': 'manager'}, 'worker': {'password': 'worker123', 'role': 'executor'}}
current_user = None

def login():
    global current_user
    username = input("Логин: ")
    password = input("Пароль: ")
    if users.get(username, {}).get('password') == password:
        current_user = username
        print(f"Добро пожаловать, {username}!")
    else:
        print("Неверный логин или пароль.")
        login()

def start():
    request.append({
        'id': input("ID заявки: "), 
        'date': input("Дата: "), 
        'fault': input("Тип неисправности: "), 
        'desc': input("Описание проблемы: "), 
        'client': input("Клиент: "), 
        'status': 'ожидание', 
        'exec': 'Кто-то', 
        'manager': 'Кто-то',  # По умолчанию назначен неизвестный менеджер
        'time_started': datetime.now()
    })
    print("Заявка создана")

def end():
    i = input("Введите номер заявки: ")
    for r in request:
        if r['id'] == i:
            r['status'] = input("Новый статус заявки: ")
            r['desc'] = input("Новое описание: ")
            r['exec'] = input("Исполнитель: ")
            r['time_completed'] = datetime.now()
            print("Заявка обновлена")
            return
    print("ID заявки не найден")

def show():
    if not request:
        print("Заявки не найдены")
        return
    for r in request:
        print(f"ID: {r['id']}, Статус: {r['status']}, Исполнитель: {r['exec']}, Менеджер: {r['manager']}")

def assign_manager():
    i = input("Введите ID заявки, чтобы назначить менеджера: ")
    for r in request:
        if r['id'] == i:
            r['manager'] = input("Введите имя менеджера: ")
            r['status'] = 'Менеджер назначен'
            print(f"Менеджер {r['manager']} назначен для заявки {r['id']}")
            return
    print("ID заявки не найдено")

actions = {
    '1': start,
    '2': end,
    '3': show,
    '4': assign_manager,
}

login()

while True:
    choice = input("\n1 - Создать заявку\n2 - Редактировать заявку\n3 - Показать заявку\n4 - Назначить менеджера\n0 - Выход\nВаш выбор: ")
    if choice == '0':
        break
    actions.get(choice, lambda: print("Неверный выбор."))()

print("Программа завершена")
