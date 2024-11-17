import json
def task() -> float:
    # Открываем и читаем JSON файл
    with open('input.json', 'r') as f:
        data = json.load(f)

    # Инициализируем переменную для хранения суммы произведений
    total_sum = 0.0

    # Проходим по каждому словарю в списке
    for entry in data:
        score = entry.get("score", 0)
        weight = entry.get("weight", 0)
        total_sum += score * weight

    # Округляем результат до трех знаков после запятой и возвращаем его
    return round(total_sum, 3)
print(task())