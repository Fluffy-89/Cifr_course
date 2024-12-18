money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0

while True:
    # бюджет текущего месяца
    budget = money_capital + salary

    # Проверяем, можем ли мы покрыть расходы
    if budget >= spend:
        months += 1
        money_capital -= spend - salary
        spend *= 1 + increase
    else:
        break  # При бюджете меньше расходов, выходим из цикла

print("Количество месяцев, которое можно протянуть без долгов:", months)
