from secrets import choice
from turtle import done
from sqlalchemy import true


print('Welcome to U of M Dearborn School Tool')
print ('This tool is case sensitive so make sure to enter just as instructed')

def calcGPA():
    print(' ')
    qPointTotal = 0.0
    CreditHourTotal = 0.0
    while true:
        GradeLetter = input('Enter the grade that you received, (A+ - E) or enter "DONE" when finished ')
        if not(GradeLetter == 'DONE'):
            CreditHours = input('Enter Number of credit hours: ')
            try:
                test = float(CreditHours)
            except:
                print('ERROR: IMPROPER INPUT RECEIVED')
                continue
            CreditHours = float(CreditHours)
        if GradeLetter == 'DONE':
            print('Your GPA is', qPointTotal / CreditHourTotal)
            break
        elif not (GradeLetter == 'A+' or GradeLetter =='A' or GradeLetter =='A-' or GradeLetter =='B+' or GradeLetter =='B' or GradeLetter =='B-' or GradeLetter =='C+' or GradeLetter =='C' or GradeLetter =='C-' or GradeLetter =='D+' or GradeLetter =='D' or GradeLetter =='D-' or GradeLetter =='E'):
            print('Error, Grade letter in Range not Entered')
            continue
        else:
            CreditHourTotal = CreditHourTotal + CreditHours

            if GradeLetter == 'A+' or GradeLetter == 'A' :
                qPointTotal =  qPointTotal + CreditHours * 4.0 #based on Honor Points
            elif GradeLetter == 'A-' :
                qPointTotal =  qPointTotal + CreditHours * 3.7
            elif GradeLetter == 'B+' :
                qPointTotal =  qPointTotal + CreditHours * 3.3
            elif GradeLetter == 'B' :
                qPointTotal =  qPointTotal + CreditHours * 3.0
            elif GradeLetter == 'B-' :
                qPointTotal =  qPointTotal + CreditHours * 2.7
            elif GradeLetter == 'C+' :
                qPointTotal =  qPointTotal + CreditHours * 2.3
            elif GradeLetter == 'C' :
                qPointTotal =  qPointTotal + CreditHours * 2.0
            elif GradeLetter == 'C-' :
                qPointTotal =  qPointTotal + CreditHours * 1.7
            elif GradeLetter == 'D+' :
                qPointTotal =  qPointTotal + CreditHours * 1.3
            elif GradeLetter == 'D' :
                qPointTotal =  qPointTotal + CreditHours * 1.0
            elif GradeLetter == 'D-' :
                qPointTotal =  qPointTotal + CreditHours * 0.7
    return 0



def calcFinalGrade():
    print(' ')
    CurrentGrade = 0
    GradeWanted = 0
    FinalGradeWeight = 0
    while true:
        CurrentGrade = input('Current Grade PERCENT: ')
        try:
            CurrentGrade = float(CurrentGrade)
        except:
            print('Error: Invalid input entered, try again')
            print(' ')
            continue
        CurrentGrade = float(CurrentGrade)
        print(' ')
        break
    while true:
        GradeWanted = input('What Grade PERCENT do you want: ')
        try:
            GradeWanted = float(GradeWanted)
        except:
            print('Error: Invalid input entered, try again')
            print(' ')
            continue
        GradeWanted = float(GradeWanted)
        print(' ')
        break
    while true:
        FinalGradeWeight = input('What is your Final exam grade weight?: ')
        try:
            FinalGradeWeight = float(FinalGradeWeight)
        except:
            print('Error: Invalid input entered, try again')
            print(' ')
            continue
        FinalGradeWeight = float(FinalGradeWeight)
        print(' ')
        break
    CurrentGradeVal = (CurrentGrade)*(1-(FinalGradeWeight/100))
    ExamGradeNeed = ((GradeWanted - CurrentGradeVal) / FinalGradeWeight)*100 
    print('You need a', ExamGradeNeed,'%', 'To achieve a', GradeWanted,"%")
    return 0


    
option = None

while true:

    print('A: GPA Calculator')
    print('B: Final Grade Calculator')
    print('C: Quit')
    print(' ')
    option = input('Enter a letter for option: ')
    if not (option == 'A' or option == 'a' or option == 'B' or option == 'b' or option == 'C' or option == 'c'):
        print('ERROR: choice chosen not in list, try again')
        print(' ')
        continue
    elif option == 'A' or option == 'a':
        calcGPA()
    elif option == 'B' or option == 'b':
        calcFinalGrade()
    else:
        break
print('Thank you for using this tool. Have a nice day')


