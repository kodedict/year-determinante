year = int(input("Enter a year: "))

if(year < 1582):
    year_type = 'Not within the Gregorian calendar period'
else:
    if(year%4 != 0):
        year_type = 'Common year'
    elif(year%100 !=0):
        year_type = 'Leap year'
    elif(year%400 !=0):
        year_type = 'Common year'
    else:
        year_type = 'Leap year'
    
print(year_type)    
