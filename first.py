import os, re

# iмпотруємо потрібні модулі 
# з самого початку перевіряємо чи снує файл, з яким будемо працювати

if os.path.exists("first_zp.txt"):
# відкриваємо файл за допомогою менеджера контексту with, який автоматично забезпечує поавельне закриття файлу
    with open(file="first_zp.txt", mode="r", encoding="utf-8") as fh:
#  читаємо текст у рядках у тексті
        lines = [el.strip() for el in fh.readlines()]
# для розрахунку використовуємо re модуль, за домомогою якого, шукаємо цифри у тексті
# та використовуємо метод join для обедняння результату у один рядок з роздільником 
        # k = (len(lines))
        nombers = lines
        pattern = r"\d+"
        matches = re.findall(pattern, nombers)
        nombers_new = (",".join(matches))
# знаходимо кількість працівників за допомогою функціі len
        person = len(nombers_new)
# знаходимо загальну сумму заробітної птати
        total = sum(nombers_new)
#знаходимо середню сумму заробітної птати
        average = total/person
# виводимо результат за домомою print та це і закриє наш файл
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    