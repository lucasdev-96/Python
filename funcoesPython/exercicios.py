
def returnBiggerNumber(num1, num2):
    biggerNumber = num2
    if num1 > num2:
        biggerNumber = num1
    return biggerNumber


print(returnBiggerNumber(30000, 50000))


def aritmetica(array):
    number = 0
    for index in array:
        number += index
    return number


print(aritmetica([30, 30, 30, 30]))


def asteristico(n):
    x = ''
    for index in range(n):
        x += '*'
    for i in range(1, n):
        print(x)


asteristico(6)


names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

print('------------------------------------------------------------')


def returnBiggerName(names):
    number = 0
    name = ''
    for index in names:
        if number < len(index):
            number = len(index)
        if number == len(index):
            name = index
    return name      


print(returnBiggerName(names))
    