# M02 Lab.py
# Thomas Gordon
# This loops through a series of input statements to intake student first name, last name, and GPA, and returns if the student made the Deans List or Honor Roll

while True:
    print("Enter \"ZZZ\" to exit program\n")
    lName = input("Student Last Name:\n")
    fName = input("Studen First Name:\n")
    gpa = float(input("Student GPA:\n"))

    if gpa >= 3.5:
        print("This student has made the Deans List")
    elif gpa >= 3.25:
        print("This student has made the Honor Roll")

    if lName == "ZZZ" or fName == "ZZZ":
        break