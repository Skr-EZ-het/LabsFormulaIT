import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Чтение данных из CSV файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # Используем DictReader для преобразования строк в словари
        data = [row for row in csv_reader]  # Сохраняем все строки в список словарей

    # Запись данных в JSON файл с отступом в 4 пробела
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Выполняем функцию для конвертации
    task()

    # Открываем JSON файл и выводим его содержимое
    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
