number = int(input("enter num: "))
def fact(number):
    count = 1
    for i in range(1,number+1):
        count *= i
    return count
print(fact(number))