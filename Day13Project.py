#Exam Grade Calculator

print("\033[92mWelcome to the Exam Grade Calculator!\033[0m")
examGrade = int(input("What is your exam grade?: "))

if examGrade >= 90:
    print("\033[94mYour grade is A\033[0m")
elif examGrade >= 80:
    print("\033[92mYour grade is B\033[0m")
elif examGrade >= 70:
    print("\033[93mYour grade is C\033[0m")
elif examGrade >= 60:
    print("\033[38;5;208mYour grade is D\033[0m")
else:
    print("\033[91mYour grade is F\033[0m")
