#Declarations
number1 = 0
number2 = 0
operation = "+"
keepGoing = "T"

print("Thank you for using our calculator - \n" + "it will ask you for two numbers, then \n" +
      "prompt you for the operations (either '+','-','/','*'). \n" +
      "The calculator will display the results and ask you\n" +
      "want to do another caculation. If not, the program will end.")

while keepGoing =="T":
    number1 = input ("Please enter your first number: ")
    number2 = input ("Please enter your second number: ")

    number1 = int(number1)
    number2 = int(number2)

    operation = input ("Please enter the operation you wishto perform. (+, -, /, *)")

    if(operation == '+'):
        answer = number1 + number2
    elif(operation == '-'):
        answer = number1 - number2
    elif(operation == '/'):
        answer = number1 / number2
    else:
        answer = number1 * number2

    print(f"The answer to {number1} {operation} {number2} = {answer}")
    keepGoing = (input("Do you wish to perform another calcuation? (T or F)" ))

print("Thanks for using our caluclator")
