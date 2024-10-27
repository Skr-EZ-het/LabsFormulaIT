# Данные задачи
disk_size_mb = 1.44  # Объем дискеты в Мб
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
symbols_per_line = 25  # Количество символов в строке
bytes_per_symbol = 4  # Объем памяти на один символ в байтах

# Перевод объема дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024  # 1 Мб = 1024 * 1024 байт

# Вычисление объема одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * symbols_per_line * bytes_per_symbol

# Вычисление количества книг, которые можно поместить на дискету
books_on_disk = disk_size_bytes // book_size_bytes  # Целочисленное деление

print("Количество книг, помещающихся на дискету:", int(books_on_disk))

