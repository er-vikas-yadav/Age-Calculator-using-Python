import datetime
def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    print(today)
    dob = datetime.date(y, m, d)
    print(dob)
    oo = (today-dob).days
    print(oo)
    age = int((today-dob).days / 365.25)
    print(age)
y = int(input("Enter your year "))
m = int(input("Enter your month "))
d = int(input("Enter your date "))
ageCalculator(y, m, d)