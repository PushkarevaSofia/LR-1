numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

 # TODO заменить значение пропущенного элемента средним арифметическим

a = numbers[:4] # Числа до None
b = numbers[5:] # Числа после None

ab = a + b      # Соединили два списка в один, без None
none_new = round(sum(ab) / len(numbers), 2) # Нашли ср.ариф.
numbers[4] = none_new # Заменили

print("Измененный список:", numbers)
