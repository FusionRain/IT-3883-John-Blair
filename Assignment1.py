# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: John Blair
# Assignment Number: 1
# Due Date: 09/05/2025
# Purpose: Text Menu to edit a buffer

buffer=[]
select=0
while select != 4:
    select=int(input("Please select and option by entering its number:\nOption 1: Append data to the input buffer\nOption 2: Clear the input buffer\nOption 3: Display the input buffer\nOption 4: Exit the program\n"))
    match select:
        case 1:
            newstring=input("Please enter your new text\n")
            buffer.append(newstring)
        case 2:
            buffer.clear()
        case 3:
            print(buffer)
        case 4:
            print("Closing Program")