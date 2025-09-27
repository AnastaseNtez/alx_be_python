def perform_operation(num1, num2, operation):
#    num1 = float(input("Enter the first number: ")) 
#    num2 = float(input("Enter the second number: "))
#    operation = input("Enter the operation (add, subtract, multiply, divide):")
   match operation:
      case "add":
           Result = num1 + num2
      case "subtract":
            Result = num1 - num2
      case "multiply":
            Result = num1 * num2
      case "divide":
            if num2 > 0:
                Result = num1 / num2
            else:
                print("Can't divide by zero")
      case _:
           print("Please enter the right operation.")
   return Result
