# write a program to check age in between child , teen and adult

age = int(input("enter age please : "))

if (age < 13):
    print("you are child ")
elif(age >= 13 and age <= 18):
    print("you are teen")
else:
    print("you are adult!")       