# Відкриваємо для читання файл, та створюємо пустий словник словник
my_dict = {}
fh = open("second_2.txt", 'r')
# Перевіряємо чи існує файл для читання
while True:
    line = fh.readline()
    if not line:
        break
# Читаємо текст використовуючи метод split, та присвоюємо значення рядка, що буде мати ключ value
    lines2 = (line.split(","))
    print(lines2)
# Присвоюємо значення значення для key
    lines1 = ["id","name","age"]
# За допомогою метододу  ziр у словниках, обеєнуємо два списки, де присвоюємо значення key, value
    for key, value in zip(lines1, lines2):
        my_dict = (key, value)
# Bиводимо утворений словник
        print(my_dict)
# обовязково закриваємо файл. 
fh.close()