import random
numbers = []

for i in range(1000):
    random_number = random.randint(1, 10)
    numbers.append(random_number)
    precent_of_oddcount = (random_number % 1000) * 100
    precent_of_evencount = (random_number / 1000) * 100
    numbers_count = numbers.count(random_number)
    print(precent_of_oddcount, precent_of_evencount)
    print(numbers_count)

def my_count(lst,number):
    counter = 0
    for i in lst:
        if i == number:
            counter += 1
    return counter

numbers = list(random_number)
for i in range(1000):
    numbers.append(random.randint(1, 10))
for number in range(1,11):
    print(number, my_count(numbers, number))

