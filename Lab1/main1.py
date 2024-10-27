numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Вычисление суммы всех элементов, кроме None
sum_numbers = sum([num for num in numbers if num is not None])

# Подсчёт количества всех элементов, включая None
count_numbers = len(numbers)

# Вычисление среднего арифметического
average = sum_numbers / (count_numbers)  # минус 1, потому что пропуск не учитывается в сумме

# Замена None на среднее арифметическое
numbers[numbers.index(None)] = average

print("Измененный список:", numbers)
