salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.03  # Ежемесячный рост цен

money_needed = 0  # Необходимая подушка безопасности

for month in range(months):
    # Рассчитываем недостающую сумму для каждого месяца
    shortfall = spend - salary

    if shortfall > 0:
        money_needed += shortfall

    # Увеличиваем расходы на 3% на следующий месяц
    spend *= (1 + increase)

# Округляем результат до целого числа
money_needed = round(money_needed)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_needed)
