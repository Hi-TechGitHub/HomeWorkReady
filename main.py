import os


def create_task():
    print("Что добавить в список? ")
    query = input("Введите заметку: ")
    with open('TextFiles/note.txt', 'a', encoding="utf-8") as file:
        file.write(f'{query}\n')
    print(f'Задача |{query}| выполнена и добавлена в note.txt!')


def open_task():
    os.system('TextFiles\\note.txt')


if __name__ == "__main__":
    allow = input('Создаём заметку? ')
    if allow.lower() == 'да':
        create_task()
    allow = input('Открываем заметки? ')
    if allow.lower() == 'да':
        open_task()
