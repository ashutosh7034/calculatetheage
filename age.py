import datetime

def year_when_100(age):
    now = datetime.datetime.now()
    current_year = now.year
    years_until_100 = 100 - age
    year_when_100 = current_year + years_until_100
    return year_when_100

name = input("What is your name? ")
age = int(input("How old are you? "))

year_100 = year_when_100(age)

print(f"Hi {name}, you will turn 100 years old in the year {year_100}.")
