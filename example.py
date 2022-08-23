from platform import java_ver


user = input("Hi welcome to temperature converter, what is your name? ")

rpt = 'y'

while rpt == 'y' :

    greet = input("Hi " + user + ", please put c or f to choose to convert. ")

    if greet == 'c' or 'f':

        tempNum = int(input('What is the number you want to convert? '))

    elif greet != 'c' or 'f':

        print('Please choose f or c. ')


    if greet == 'f':

        print((tempNum - 32) * 5 / 9)

    elif greet == 'c':

        print((tempNum * 9) / 5 + 32)


    rpt = input('do you want to continue? (y or n) ')

    print('Thamk you for using this!')