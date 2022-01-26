from calendar import month
from datetime import date
import time

print("Welcome.")

td = date.today()
todays_date = date.today()
print(td)
m = input("Birthday month: ")
y = int(input("Birthday year: "))
d = int(input("Birthday day: "))
if(type(m) == str):
     if(m == "janurary"):
         m = 1
     elif(m == "february"):
         m = 2
     elif(m == "march"):
         m = 3
     elif(m == "april"):
         m = 4
     elif(m == "may"):
         m = 5
     elif(m == "june"):
         m = 6
     elif(m == "july"):
         m = 7
     elif(m == "august"):
         m = 8
     elif(m == "september"):
         m = 9
     elif(m == "october"):
         m = 10
     elif(m == "november"):
         m = 11
     else:
         m = 12

age = todays_date.year - y
if(m > todays_date.month):
    age = age - 1
    
if((m == todays_date.month) & (d > todays_date.day)):
    age = age - 1
    

print("You are", age, "years old")

print("You were born on", m, d, y)


print("hapi berth bay :)")
