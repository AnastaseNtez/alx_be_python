def perform_operation(num1, num2, operation):
  #    num1 = float(input("Enter the first number: ")) 
  #    num2 = float(input("Enter the second number: "))
  #    operation = input("Enter the operation (add, subtract, multiply, divide):")
   
    if operation == "add":
           Result = num1 + num2
    elif  operation == "subtract":
            Result = num1 - num2
    elif operation == "multiply":
            Result = num1 * num2
    elif operation == "divide":
        if num2 > 0:
            Result = num1 / num2
        if num2 == 0 and num1 == 0:
            print("Can't divide by zero")
    else :
        print("Please enter the right operation.")
    return Result
