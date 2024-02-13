from ScientificCalculatorMethods import compute_sqrt,print_result,compute_factorial,compute_log,compute_power

flag=1

while(flag):
    print("-------------------------- Welcome to Scientific Calculator -----------------------------")
    print("Press 1 for Square root function")
    print("Press 2 for Factorial function")
    print("Press 3 for Natural Logarithm function")
    print("Press 4 for Power function")
    print("Press 0 to exit")
    choice=int(input("Enter the choice:"))
    if(choice==1):
        try:
            number=int(input("Enter the number:"))
            result= compute_sqrt(number)
            print_result(result)
        except:
            print("Please enter a valid input")
    elif(choice==2):
        try:
            number=int(input("Enter the number:"))
            result=compute_factorial(number)
            print_result(result)
        except:
            print("Please enter a valid input")
    elif(choice==3):
        try:
            number=int(input("Enter the number:"))
            result=compute_log(number)
            print_result(result)
        except:
            print("Please enter a valid input")
    elif(choice==4):
        try:
            base=int(input("Enter the base number:"))
            power=int(input("Enter the power:"))
            result=compute_power(base,power)
            print_result(result)
        except:
            print("Please enter a valid input")
    elif(choice==0):
        flag=0
    else:
        print("Invalid choice. Please enter a valid choice")
