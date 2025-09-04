#  Question 1 Answer

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
       return a / b
    except ZeroDivisionError:
        print("You must enter number greater than zero\n")


while True:
    choice = input("\nchoose an option:\n1. Addition \"+\"\n2. Subtraction \"-\"\n3. Multiplication \"*\"\n4. Division \"/\"\n5. Exit\nEnter your choice: ")


    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input\nEnter a number")
        result = add(num1, num2)
        print(f"Result: {result}")
    elif choice == "2":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input\nEnter a number")
        result = subtraction(num1, num2)
        print(f"Result: {result}")
    elif choice == "3":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input\nEnter a number")
        result = multiplication(num1, num2)
        print(f"Result: {result}")
    elif choice == "4":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input\nEnter a number")
        result = division(num1, num2)
        print(f"Result: {result}")
    elif choice == "5":
        print("Exiting calculator... Goodbye!")
        break
    else:
        print("Enter the right option")







# Question 2 
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break       # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")






# Question 3
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input. Please enter a number.")