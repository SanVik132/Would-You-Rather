# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2021.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    pass



# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    pass



# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    pass



# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
try:
    # Open a file
    file = open('data.txt','r')
    data = json.load(file)
    # Close opend file
    file.close()
except:
    data = []


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "Would You Rather" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() # Convert input to lowercase to make choice selection case-insensitive.
        
    if choice == 'a':
        while(1):
            option_1 = input_something('Enter 1st option')
            if option_1 == '':
                save_data()
                break
            option_2 = input_something('Enter 2nd option')
            choice = input_something('if the question is intended for mature audiences')
            if choice =="y" or "Y":
                mature = True
            elif choice == "N" or "n":
                mature = False

            dict={
                "option_1": option_1,
                "option_2": option_2,
                "mature": mature,
                "votes_1": 0,
                "votes_2": 0
            }

            data.append(dict)
        
            
        # Add a new question.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
       


    
    elif choice == 'l':
        if len(data) == 0:
            print('No questions saved')
        else:
            for i in enumerate(data):
                my_string = "{} ) {} / {}".format(i[0],i[1]['option_1'] , i[1]['option_2'])
                print(my_string)






    elif choice == 's':
        if len(data) == 0:
            print('No questions saved')
        else:
            while(True):
                search_term= input_something('Enter the search term')
                search_term = search_term.lower()
                for i in enumerate(data):
                    if search_term in (i[1]['option_1'] or i[1]['option_2']):
                        my_string = "{} ) {} / {}".format(i[0],i[1]['option_1'] , i[1]['option_2'])
                        print(my_string)




    elif choice == 'v':
        if len(data) == 0:
            print('No questions saved')
            while(True):
                search_term = input_something('Enter the Index ')
                try:
                    val = int(search_term)
                    for i in enumerate(data):
                        if i[o]==val:
                            my_string = "{} ) {} / {}".format(i[0],i[1]['option_1'] , i[1]['option_2'])
                            print(my_string)
                except ValueError:
                    break
        

        

    elif choice == 'd':
        # Delete a question.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        pass

        

    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        pass



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        pass



# If you have been paid to write this program, please delete this comment.

input_int()