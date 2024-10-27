# Функция для поиска индекса товара
def find_item_index(items, item):
    try:
        # Поиск индекса первого вхождения
        return items.index(item)
    except ValueError:
        # Если элемент не найден, возвращаем None
        return None

# Список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Поиск элементов в списке
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
