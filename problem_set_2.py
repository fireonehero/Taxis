# CREDENTIALS #
Author = "Darrian Holley"
Version = "2.5.2"
Publicly_Available = True


try:
    #Imports
    import os
    import time

    #Allows it to clear terminal on both Linux and Windows
    os.system('cls' if os.name == 'nt' else 'clear')

    #Color Dic
    COLORS = {\
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "magenta":"\u001b[35m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
    "yellow-background":"\u001b[43m",
    "black-background":"\u001b[40m",
    "cyan-background":"\u001b[46;1m",
    }

    #Color Converter Function
    def colorText(text):
        for color in COLORS:
            text = text.replace("[[" + color + "]]", COLORS[color])
        return text


    #Intro Messages
    print(colorText("""
    [[red]]#  #  #                                                      [[white]]######                               [[blue]]#     #               ######                                             
    [[red]]#  #  #  ######  #        ####    ####   #    #  ######      [[white]]#     #    ##     ####   #    #      [[blue]]##   ##  #####        #     #    ##    #####   #####   #    ##    #    # 
    [[red]]#  #  #  #       #       #    #  #    #  ##  ##  #           [[white]]#     #   #  #   #    #  #   #       [[blue]]# # # #  #    #       #     #   #  #   #    #  #    #  #   #  #   ##   # 
    [[red]]#  #  #  #####   #       #       #    #  # ## #  #####       [[white]]######   #    #  #       ####        [[blue]]#  #  #  #    #       #     #  #    #  #    #  #    #  #  #    #  # #  # 
    [[red]]#  #  #  #       #       #       #    #  #    #  #           [[white]]#     #  ######  #       #  #        [[blue]]#     #  #####   ###  #     #  ######  #####   #####   #  ######  #  # # 
    [[red]]#  #  #  #       #       #    #  #    #  #    #  #           [[white]]#     #  #    #  #    #  #   #       [[blue]]#     #  #   #   ###  #     #  #    #  #   #   #   #   #  #    #  #   ## 
    [[red]] ## ##   ######  ######   ####    ####   #    #  ######      [[white]]######   #    #   ####   #    #      [[blue]]#     #  #    #  ###  ######   #    #  #    #  #    #  #  #    #  #    # 
                                                                                                                                                                            
    """))

    print("\nInitialization Loading --> ",end="")
    time.sleep(1)
    print(colorText("[[green]]Success[[white]]"))

except:
    print("\nInitialization Loading --> ",end="")
    time.sleep(1)

    print(colorText("[[red]]Failure[[white]]"))
    time.sleep(1)

    print(colorText("\nSystem [[red]]Shutting Off[[white]]"))
    time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')

    exit()


#Square Function
def square(x):
    y = x ** 2
    print(f'The number squared is {y}')
    return
    #X to the 2 power

#Great Function
def greet(name):
  return "Hello " + colorText("[[red]]") + name + colorText("[[white]]") + "!"

#Convert Function
def convert(amount:float, endval): return str(round(amount*2.54, 2) if endval == "cm" else round(amount/2.54, 2)) + " " + endval

#Fade Function
def fade(phrase):
    splitphrase = phrase.splitlines()
    splitphrase2 = []
    for line in splitphrase:
        splitphrase2.append(line[0:-1]) if line[-2] != "]" else splitphrase2.append("[[".join(line.split("[[")[0:-1]))
    return "\n".join(splitphrase2)

#Choosing Question
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
command = None
while True:
    while command not in ['original', 'q1', 'q2', 'q3', 'q4', 'commands', 'exit', 'version', "studentinfo"]:
        command = input(colorText('\n\n[[white]]Please select what question you would like to view. Use [[red]]Exit[[white]] to quit the program. Please enter [[magenta]]Commands [[white]]for more assistance: ')).lower()

    ##############
    #Problem List

    if command == 'original':
        print(colorText("""\n
        [[green]]# Q1 Can you add some comments to this python program so that it is more understandable, can you also change the variable name to mean something sensible, the program is meant to be for a user to enter their name:
        # your code below this line:[[white]]

        x123 = input('Enter123name: ')
        print('Hello............', x123, '!')
        print('Exiting x123 progggggram')


        [[green]]# Q2 Make the following program more readable and add an in-line comment at the end of each line, fix any syntax errors.[[white]]
        number_entered = input('Enter a number and i will square it: ')
        number_squared = number_entered * numbre_enterd
        print('The number squared is, (number_squared, '!')


        [[green]]# Q3 Fix the syntax in this program so that it runs, add a comment to explain what it is doing?
        # the program should sum two numbers and have 3 variables[[white]]

        number1 = 1
        number2 = 2
        number4 = number4 + number3


        [[green]]# Q4 Create a program with sensible comments and variable names that 
        # takes a number and divides it by 2.54. The title of the program should be "Inches to cm Converter"
        # your code here[[white]]
        """))


    #Question 1
    elif command == 'q1':
        print(greet(input("\nPlease enter your name: ")))
        
    #Question 2
    elif command =='q2':
        #Calls the square function.
        square(int(input('\nEnter number to square: ')))

    #Question 3
    elif command =='q3':
        def sum(num1:float, num2:float):
            #Adds together the two given numbers for a third returnable number
            num3 = num1+num2
            #Fancies up the return
            return "\nThe sum of your two numbers is " + colorText("[[yellow]]" + str(num3) + "[[white]]")

        #Defines Numbers 1 and 2
        num1,num2 = float(input("\nNumber 1: ")),float(input("\nNumber 2: "))

        #Adds Numbers 1 and 2 to return Number 3
        print(sum(num1,num2))

    #Question 4
    elif command =='q4':
        val=""
        while val not in ["in", "cm"]: val=input("What would you like to convert into (in/cm): ").lower()
        unit="in" if val!="in" else "cm"
        amount=float(input(f"\nWhat's the original value in [{unit}.] (just the number)? "))
        print(f"{convert(amount,val)}")

    #Version
    elif command == 'version':
        print(colorText(f'\n[[yellow]]You are currently in - '),end="")
        time.sleep(1)
        print(colorText(f'[[blue]]v{Version}[[white]]'))

    #Commands
    elif command == 'commands':
        print(colorText("[[yellow]]Use Q1 for Question 1\nUse Q2 for Question 2\nUse Q3 for Question 3\nUse Q4 for Question 4"))
        print('Use Original to see the original questions.')
        print('Use Version to see the programs current version.')
        print('Use StudentInfo to see the Student Info.')
        print(colorText('Use Exit to quit the program.[[white]]'))

    elif command == 'studentinfo':
        print(colorText("""
Name: [[cyan]]Darrian Holley[[white]]
Student ID: [[yellow]]EC[[white]]
Date: [[blue]]21 9 2021[[white]]"""))

    #Exit Command
    elif command == 'exit':
        goodbye="""[[red]]   ####  [[yellow]]        [[green]]        [[cyan]]        [[blue]] ######                
[[red]] #     # [[yellow]]  ####  [[green]]  ####  [[cyan]] #####  [[blue]] #     # [[magenta]] #   # [[red]] ######
[[red]] #       [[yellow]] #    # [[green]] #    # [[cyan]] #    # [[blue]] #     # [[magenta]]  # #  [[red]] #     
[[red]] #  #### [[yellow]] #    # [[green]] #    # [[cyan]] #    # [[blue]] ######  [[magenta]]   #   [[red]] ##### 
[[red]] #     # [[yellow]] #    # [[green]] #    # [[cyan]] #    # [[blue]] #     # [[magenta]]   #   [[red]] #     
[[red]] #     # [[yellow]] #    # [[green]] #    # [[cyan]] #    # [[blue]] #     # [[magenta]]   #   [[red]] #     
[[red]]  #####  [[yellow]]  ####  [[green]]  ####  [[cyan]] #####  [[blue]] ######  [[magenta]]   #   [[red]] ######"""

        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colorText(goodbye))
                goodbye=fade(goodbye)
                time.sleep(0.03)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colorText('[[white]]'))
                exit()

    #Loops
    command = 'Breaking'