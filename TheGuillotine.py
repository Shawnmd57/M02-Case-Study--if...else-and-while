#Program: TheGuillotine.py
#Author: Shawn Daumer
#Date: 11/07/2023
#Purpose: Accepts student names and GPAs to test if the student qualifies for either the Dean's List or the Honor Roll.

while True:   
    print("\nWhat is the student's last name? (Enter 'ZZZ' to quit proccessing records.)")
    #Gets the student's last name
    lastName = input()
    if lastName == "ZZZ":
        print("*quit proccessing records*")
        break
    else:
        print("What is the student's first name?")
        #Gets the student's first name
        firstName = input()

        print("What is the student's GPA?")
        #Gets the student's GPA
        gpa = float(input())

        #Decides if the student qualifies for either the Dean's List or the Honor Roll. 
        if gpa >= 3.5:
            print( firstName, lastName, "has made the Dean's List.")
        elif gpa >= 3.25:
                print( firstName, lastName, "has made the Honor Roll.")
        else:
                print( firstName, lastName, "has made neither the Dean's List or Honor Roll.")

