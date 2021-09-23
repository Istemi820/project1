import math
a = int(input("Введите: "))
b = int(input("Введите: "))
def gipotenuza():
    ag = a * a
    bg = b * b
    count = ag + bg
    print(math.sqrt(count))
gipotenuza()
