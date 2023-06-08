import csv
from datetime import date


def add_notebook(title, text):
    # Генерация нового идентификатора заметки (максимальный идентификатор + 1)
    if len(notebook) > 0:
        note_id = max(notebook.keys()) + 1
    else:
        note_id = 1
    # Создание новой заметки
    note = {
        "id": note_id,
        "title": title,
        "text": text,
        "created_at": date.today().strftime("%Y-%m-%d")
    }
    # Добавление заметки в список заметок
    notebook[note_id] = note
    # Сохранение заметок в файл
    save_notebook()


def show_notebook():
    # Вывод списка заметок
    for note_id, note in notebook.items():
        print(f"{note_id}. {note['title']} ({note['created_at']})")


def get_notebook(id):
    # Получение заметки по идентификатору
    if id in notebook:
        note = notebook[id]
        print(f"{note['title']} ({note['created_at']})\n{note['text']}")
    else:
        print("Заметка не найдена")


def edit_notebook(id):
    # Редактирование заметки по идентификатору
    if id in notebook:
        note = notebook[id]
        note["title"] = input("title: ")
        note["text"] = input("text: ")
        print("Заметка успешно отредактирована")
    else:
        print("Заметка не найдена")
    # Сохранение заметок в файл
    save_notebook()


def delete_notebook(id):
    # Удаление заметки по идентификатору
    if id in notebook:
        del notebook[id]
        print("Заметка успешно удалена")
    else:
        print("Заметка не найдена")
    # Сохранение заметок в файл
    save_notebook()


def save_notebook():
    # Сохранение заметок в файл
    with open(NOTEBOOK_FILE, "w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file, delimiter=";")
        for note_id, note in notebook.items():
            writer.writerow([note["id"], note["title"], note["text"], note["created_at"]])


def load_notebook():
    # Загрузка заметок из файла
    try:
        with open(NOTEBOOK_FILE, "r", encoding="UTF-8") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                note_id = int(row[0])
                note = {
                    "id": note_id,
                    "title": row[1],
                    "text": row[2],
                    "created_at": row[3]
                }
                notebook[note_id] = note
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    # Имя файла для сохранения заметок
    NOTEBOOK_FILE = "notebook.csv"
    # Загрузка заметок из файла

    notebook = {}
    load_notebook()
    while True:
        allow = input("Добавляем записку?: ")
        if allow.lower() == "да":
            add_notebook(input("Заголовок записки: "), input("Текст записки: "))

        allow = input("Показать записки?: ")
        if allow.lower() == "да":
            show_notebook()

        allow = input("Показать записку используя id?: ")
        if allow.lower() == "да":
            get_notebook(int(input("Введите id: ")))

        allow = input("удалить записку используя id?: ")
        if allow.lower() == "да":
            delete_notebook(int(input("Введите id: ")))

        allow = input("Отредактировать записку по id?: ")
        if allow.lower() == "да":
            edit_notebook(int(input("Введите id: ")))
