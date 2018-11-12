name = input("what is your name?  ")
print("hello " + name + ". This is a trial program to output your age range.")
import calendar
yr = int(input("Please type in your year of birth: "))

from _datetime import datetime
currentYear = datetime.now() .year
Age = currentYear - yr

if(Age < 18):
         print("You are a minor. You have a long healthy life ahead of you.")


if(17 < Age < 36):
         print("You are a youth. Enjoy your prime years.")
         


if(Age > 35):
     print("You are an elder. Old is gold.")

input()
