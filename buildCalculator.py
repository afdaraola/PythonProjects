from logging import exception

print("Building calculator project")

def add(num1,num2):
    return num1+num2

def substrat(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def division(num1, num2):
    return num1/num2

print("1 - Addition \n 2 - Substration \n 3 - Multiplication \n 4 - division")

choice = int(input("select option 1/2/3/4 to perform operation"))



try:
    firstNumber = int(input("supply first number"))
    secondNumber = int(input("supply second number "))

    if choice == 1:
        print(f"addition of {firstNumber} and {secondNumber} is equal "+ str(add(firstNumber,secondNumber)))
    elif choice ==2:
        print(f"Substraction of {firstNumber} and {secondNumber} is equal "+ str(substrat(firstNumber,secondNumber)))
    elif choice==3:
        print(f"product of {firstNumber} and {secondNumber} is equal "+ str(multiply(firstNumber,secondNumber)))
    elif choice==4:
        print(f"Division of {firstNumber} and {secondNumber} is equal "+ str(division(firstNumber,secondNumber)))
    else:
        print("Select valid choice ")
except ZeroDivisionError:
    print("division by zero")
except:
    print("Something went wrong")



