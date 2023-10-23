# This function asks the user for two numbers and apllies the operation '+','-','/','*' 
# And save the results in file named calculator_review.txt 
def num_input():
    while True:
        try:
            print("Please enter two numbers: ")
            num1 = int(input(" 1'st: "))
            num2 = int(input(" 2'nd: "))      
            print("Enter the operation ( +, -, /, * ): ")
            oper = input()

        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            continue

        try:   
            if oper == '+':
                output = f'\n{num1} + {num2} = {add(num1, num2)}'
                print (output)
            elif oper == '-':
                output = f'\n{num1} - {num2} = {sub(num1, num2)}'
                print(output)
            elif oper == '*' or oper == 'x':
                output = f'\n{num1} x {num2} = {multip(num1, num2)}'
                print(output)
            elif oper == '/':
                output = f'\n{num1} / {num2} = {div(num1, num2)}'
                print(output)
            with open('calculator_review.txt','a') as file:
                file.write(output)
                break
        except ValueError():
            print('Invalid option. Please try again')   
        pass

# These are functions with the operators addition, substruction, multiplication, division 
def add (num1, num2):      
    return num1 + num2
def sub (num1, num2):
    return num1 - num2
def div (num1, num2):
    return round((num1 / num2),2)
def multip (num1, num2):
    return num1 * num2   


# In this loop the user is asked to choose an option 
# Option 'N' acces the num_input() function 
# Option 'R' asks the user to enter the file name and prints out the all previous ecuations and results 
# Option 'E' breaks the loop 

while True:
    try:
        print("\nTo choose calculator enter 'N' \nTo review all the written ecuations enter 'R':\nTo exit enter 'E'")
        next_step = str(input()).lower()
        if next_step=="n":
            num_input()
        elif next_step == 'r':
            
            print(f"To view the ecuations please enter the file name:")
            file_name = str(input())
            if file_name == 'calculator_review.txt':
                with open('calculator_review.txt', 'r') as file:
                        print("\n", file.read())
            else:
                print('Invalid name. Try again')
        elif next_step == 'e':
            break                    
        else:
            print('Invalid input. Please try again!')             
    except ValueError():
        print('Invalid input. Please try again!')
