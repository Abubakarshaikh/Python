# comparison operators
 
print("English")
eng = int(input())

print("Math")
math = int(input())

print("Science")
sci = int(input())

print("Urdu")
urdu = int(input())

print("Islamiat")
ist = int(input())

print("Total marks: ")
total_marks = int(input())

print("")
if eng < 33:
    print("Fail in english. ")
else:
    print("Pass in English. ")

if math > 33:
    print("Pass in math. ")
else:
    print("Fail in math")

if sci < 33:
    print("Fail in Science. ")
else:
    print("Pass in Science. ")

if urdu < 33:
    print("Fail in urdu. ")
else:
    print("Pass in urdu")

if ist < 33:
    print("Fail in islamiat")
else:
    print("Pass in islamiat")

print("")
sum_all_subjects_marks = eng + math + sci + urdu + ist

print("Total marks. ",total_marks)
print("Obtain marks. ",sum_all_subjects_marks)
if sum_all_subjects_marks < 165:
    print("You are Fail")
else:
    print("Congratulations You are Pass. ")

percentage = sum_all_subjects_marks * 100 / total_marks 
print("Your Percentage is: ",percentage)

if percentage <= 33:
    print("F grade. ")
elif percentage <= 70:
    print("B grade. ")
elif percentage <= 90:
    print("A Grade. ")
else:
    print("Topper")
