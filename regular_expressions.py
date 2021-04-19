import re


def fun1():
    with open('simpsons_phone_book.txt') as file:
        for line in file:
            if re.search(r'J.*Neu', line):
                print(line)


def fun2():
    data = "Allison Neu 555-8396\nC. Montgomery Burns \nLionel Putz 555-5299\nHomer Jay Simpson 555-7334"
    for line in data.split("\n"):
        result = ""
        # Check if phone number exists
        phone = re.search(r'([A-Za-z ]+) ([A-Za-z]+) (\d{3}-\d{4})*', line)
        if phone is not None:
            result = (phone.group(3) + " " if phone.group(3) is not None else "") + phone.group(2) + ", " + phone.group(1)
            print(result)

        #

fun2()