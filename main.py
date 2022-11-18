# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# This function return a percentage
def percentage(x, y):
    return divide(x, y) * 100


# This function verify if s is a number
def isNotNumber(s):
    try:
        float(s)
        return False
    except ValueError:
        return True


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):

        num1 = input("Enter first number: ")
        while isNotNumber(num1):
            print("- Invalid Input, try again")
            num1 = input("Enter first number: ")

        num1 = float(num1)
        num2 = input("Enter second number: ")
        while isNotNumber(num2):
            print("- Invalid Input, try again")
            num2 = input("Enter second number: ")

        num2 = float(num2)

        if choice == '1':
            print(num1, "+", num2, " = ", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, " = ", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, " = ", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, " = ", divide(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "*100" " = ", percentage(num1, num2), "%")

        # check if user wants another calculation
        # break the while loop if answer is no
        leave = True
        while leave:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            next_calculation = next_calculation.lower()
            if next_calculation == "no" or next_calculation == "n":
                break
            if next_calculation == "yes" or next_calculation == "y":
                leave = False
            else:
                print("- Invalid Input")

        if leave:
            print("- Closing Program")
            break


    else:
        print("- Invalid Input")
