salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен (3%)

# Нулевая подушка безопасности
money_capital = 0

for month in range(months):
    # Рассчет нехватки средств
    deficit = spend - salary

    # Если есть нехватка, добавляем ее к подушке безопасности
    if deficit > 0:
        money_capital = money_capital + deficit

    spend *= (1 + increase)

import math
money_capital = math.ceil(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
