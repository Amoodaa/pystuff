year = int(input('Enter a year: '))

leap = f"{year} is a leap year"
not_leap = f"{year} is not a leap year"

if year % 400 == 0:
    print(leap)
elif year % 100 == 0:
    print(not_leap)
elif year % 4 == 0:
    print(leap)
else:
    print(not_leap)

# $ D:\code\pystuff\assignment> python .\118-36-leap-years.py
# Enter a year: 1900
# 1900 is not a leap year

# $ D:\code\pystuff\assignment> python .\118-36-leap-years.py
# Enter a year: 2000
# 2000 is a leap year

# $ D:\code\pystuff\assignment> python .\118-36-leap-years.py
# Enter a year: 1232
# 1232 is a leap year

# $ D:\code\pystuff\assignment> python .\118-36-leap-years.py
# Enter a year: 1234
# 1234 is not a leap year
