#This program will be used for the logic of a simple Python calculator.
#I will first create a terminal version of the application, then implement a GUI at a future date.
# I will create fuctions for addition, subtraction, multiplication, division,
# square root, squared, and cubed functions.

#Importing the math class, and time class to allow 3 secs before calculator resets
import math
import time


def main():
    #Addition function, retuns the sum of 2 numbers
    def addition(x,y):
        return x + y
    #Subtraction funciton, retuns the difference between 2 numbers
    def subtraction(x,y):
        return x - y
    #Multiplication function, returns the product of 2 numbers
    def multiplication(x,y):
        return x * y
    #Division function, returns the quotient of 2 numbers
    def division(x,y):
        return float(x / y)
    #Square Root function, returns the square root of 1 number
    def squareRoot(x):
        return float(math.sqrt(x))
    #Squared function, returns a number to the power of 2.
    def squared(x):
        return x ** 2
    #Cubed function, returns a number to the power of 3.
    def cubed(x):
        return x ** 3
    #Single number validation function, used for single number operations
    def singleNumberValid():
        testX = 0
        while True:
            print("Please input your number for this operation: ")
            x = input()
            try:
                testX = int(x)
            except:
                print("Please enter a valid integar")
                continue
            break
        return x
    #Double number validation function, used for double number operations
    def doubleNumberValid():
        testX = 0
        testY = 0
        while True:
            print("Please input your first number for your operation: ")
            x = input()
            try:
                testX = int(x)
            except:
                print("Please enter a valid integar")
                continue
            break
        while True:
            print("Please input your second number for your operation: ")
            y = input()
            try:
                testY = int(y)
            except:
                print("Please enter a valid integar")
                continue
            break
        return (x,y)
    
    print("Welcome to my calculator app!")
    #calKill used to kill the while loop for calculator, optNum used to capture the approiate operation,
    #num1 used for single and double number operations, num2 only used in 2 number operations
    calKill = 0
    optNum = ""
    optNumI = 0
    num1 = 0
    num2 = 0
    #Main loop for calculator app
    while(calKill != 1):
        #Prints the calculator for the user to input one of the numbers to run that operator
        print("Please select one of the following options by typing the number of the option.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root of any number")
        print("6. Any number Squared")
        print("7. Any number cubed")
        print("8. Quit the Calculator")
        #Captures user input for their selected option and assigns the value to optNum, uses a Try-Except statement for validating user input
        while True:
            optNum = input()
            try:
                tempNum = int(optNum)
            except:
                print("Please enter a valid numeric integar.")
                continue
            if(tempNum < 0 or tempNum > 8):
                print("Please enter an option between 1 - 8.")
                continue
            break
        #Once try-expect is successful, optNumI will be used to change optNum to an integar
        optNumI = int(optNum)
        #Match-case to simulate a switch-case, used to perform the option selected by the end user
        match optNumI:
            #Addition
            case 1:
                tempTup = doubleNumberValid()
                num1 = int(tempTup[0])
                num2 = int(tempTup[1])
                print("The number %d added to the number %d is %d." % (num1,num2,addition(num1,num2)) + '\n')
                time.sleep(3)
            #Subtraction
            case 2:
                tempTup = doubleNumberValid()
                num1 = int(tempTup[0])
                num2 = int(tempTup[1])
                print("The number %d subtracted from the number %d is %d." % (num2,num1,subtraction(num1,num2)) + '\n')
                time.sleep(3)
            #Multiplication
            case 3:
                tempTup = doubleNumberValid()
                num1 = int(tempTup[0])
                num2 = int(tempTup[1])
                print("The number %d multiplied by the number %d is %d." % (num1,num2,multiplication(num1,num2)) + '\n')
                time.sleep(3)
            #Division
            case 4:
                tempTup = doubleNumberValid()
                num1 = int(tempTup[0])
                num2 = int(tempTup[1])
                print("The number %d divided by the number %d is %.3f." % (num1,num2,division(num1,num2)) + '\n')
                time.sleep(3)
            #Square Root
            case 5:
                num1 = int(singleNumberValid())
                #Will round float to only 3 decimal places
                print("The square root of %d is %.3f." % (num1, squareRoot(num1)) + '\n')
                time.sleep(3)
            #Squared
            case 6:
                num1 = int(singleNumberValid())
                print("The number %d squared is %d." % (num1,squared(num1)) + '\n')
                time.sleep(3)
            #Cubed
            case 7:
                num1 = int(singleNumberValid())
                print("The number %d cubed is %d." % (num1,cubed(num1)) + '\n')
                time.sleep(3)
            #Close the calculator
            case 8:
                calKill += 1
                time.sleep(3)

    print("Thank you for using my Calculator!")
main()