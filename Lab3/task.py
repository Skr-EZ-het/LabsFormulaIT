# Функция для поиска общих участников
def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки на списки участников по разделителю
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общие элементы
    common_participants = participants1 & participants2

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Данные участников
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем '|'
common = find_common_participants(participants_first_group, participants_second_group, separator='|')

print("Общие участники:", common)
