#--------------------------------------------------------------------------
#  Flie   |          (CS112_A1_T3_problem1_20231200.py)                    |
#--------------------------------------------------------------------------|
#         |                                                                |
# Purpose |          You have to input your grade and                      |
#         |      the programe will tell you the score.                     |  
#--------------------------------------------------------------------------|               
#  Author |                 Walid Adel Mordy Rohaim                        |
#--------------------------------------------------------------------------|
#   ID    |                         20231200                               |                        
#--------------------------------------------------------------------------|

def stage():
    #start
    # Check the validety of the input. 
    while True:
        try:
            grade=int(input("Please, Enter your grade: "))
            break
        except ValueError:
            print("\nInvalid Input! youer input has to be integer, So please, Follow the instructionsz.")
    while grade<0:
        print('\nYour grade has to be greater than or equal to zero. ')
        while True:
            try:
                grade=int(input("Please, Enter your grade: "))
                break
            except ValueError:
                print("\nInvalid Input! youer input has to be integer. So please, Follow the instructionsz.")

    # set and output the score of the student. 
    if 100>=grade>=90:
        print('A+') 
    elif 90>grade>=85:
        print('A')
    elif 85>grade>=80:
        print('B+')
    elif 80>grade>=70:
        print("B")
    elif 70>grade>=65:    
        print('C+')
    elif 65>grade>=60:
        print("C")
    elif 60>grade>=55:
        print("D")
    elif 55>grade>=50:
        print('E')
    elif grade < 50 :
        print("F")
    else:
        print('\nYour number has to be less than 100\n')
        stage()

stage()
