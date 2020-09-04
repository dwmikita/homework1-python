gradepoint1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
if(gradepoint1 == 'A'):
    gradepoint1 = 4.0
elif (gradepoint1 == 'A-'):
    gradepoint1 = 3.67
elif (gradepoint1 == 'B+'):
    gradepoint1 = 3.33
elif (gradepoint1 == 'B'):
    gradepoint1 = 3.0
elif (gradepoint1 == 'B-'):
    gradepoint1 = 2.67
elif (gradepoint1 == 'C+'):
    gradepoint1 = 2.33
elif (gradepoint1 =='C'):
    gradepoint1 = 2.0
elif (gradepoint1 == 'D'):
    gradepoint1 = 1.0
else:
    gradepoint1 = 0.0
print("Grade point for course 1 is:", gradepoint1)

gradepoint2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
if(gradepoint2 == 'A'):
    gradepoint2 = 4.0
elif (gradepoint2 == 'A-'):
    gradepoint2 = 3.67
elif (gradepoint2 == 'B+'):
    gradepoint2 = 3.33
elif (gradepoint2 == 'B'):
    gradepoint2 = 3.0
elif (gradepoint2 == 'B-'):
    gradepoint2 = 2.67
elif (gradepoint2 == 'C+'):
    gradepoint2 = 2.33
elif (gradepoint2 =='C'):
    gradepoint2 = 2.0
elif (gradepoint2 == 'D'):
    gradepoint2 = 1.0
else:
    gradepoint2 = 0.0
print("Grade point for course 2 is:", gradepoint2)

gradepoint3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
if(gradepoint3 == 'A'):
    gradepoint3 = 4.0
elif (gradepoint3 == 'A-'):
    gradepoint3 = 3.67
elif (gradepoint3 == 'B+'):
    gradepoint3 = 3.33
elif (gradepoint3 == 'B'):
    gradepoint3 = 3.0
elif (gradepoint3 == 'B-'):
    gradepoint3 = 2.67
elif (gradepoint3 == 'C+'):
    gradepoint3 = 2.33
elif (gradepoint3 =='C'):
    gradepoint3 = 2.0
elif (gradepoint3 == 'D'):
    gradepoint3 = 1.0
else:
    gradepoint3 = 0.0
print("Grade point for course 3 is:", gradepoint3)

GPA = (gradepoint1 * int(credit1) + gradepoint2 * int(credit2) + gradepoint3 * int(credit3)) / (int(credit1) + int(credit2)+ int(credit3))
print("Your GPA is:", GPA)