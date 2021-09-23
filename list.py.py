def main():
    text = input("Текст: ")
    days = int(input("Дни: "))
    len(text.replace(' ', ''))
    count = len(text.replace(' ', ''))
    if days < 5:
        print(count * 10)
    elif 5 <  days < 10:
        print(count * 6)
    elif days >= 50:
        print(count * 3)
    return count

result = main()
print(result)


