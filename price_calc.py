# price_calc.py

# Ввод данных от пользователя
cost_price = float(input("Введите себестоимость товара (€): "))
markup_percent = float(input("Введите наценку (%) : "))

# Формула расчета
final_price = cost_price + (cost_price * markup_percent / 100)

# Вывод результата
print(f"Итоговая цена: {final_price:.2f} €")
