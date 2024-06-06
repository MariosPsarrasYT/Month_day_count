month = input("Give me a month (with capitals) ")
year = int(input("Give me a year" ))

d = year % 4

if month == "September" or month == "April" or month == "June" or month == "November":
    print(month, "has 30 days")
elif month == "February" and d == 0:
    print(month, "has 29 days")
elif month == "February" and d != 0:
    print(month, "has 28 days")
else:
    print(month, "has 31 days")


