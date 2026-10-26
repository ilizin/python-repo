def is_year_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

def days_in_month(year, month):
    if (month < 1 or month > 12):
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month == 2 and is_year_leap(year)):
        days[1] = 29
    return days[month - 1]

def day_of_year(year, month, day):
    if (month < 1 or month > 12):
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month == 2 and is_year_leap(year)):
        days[1] = 29
    if (day < 1 or day > days[month - 1]):
        return None
    day_of_year = 0
    for current_month in range(1, month):
        day_of_year += days_in_month(year, current_month)
    return day_of_year + day

test_years = [1900, 2000, 2016, 1987, 1987, 1000, 1000, 1000, 1987]
test_months = [2, 12, 9, 11, 13, 7, 4, 2, 2]
test_days = [2, 31, 15, 11, 11, 32, 31, 30, 29]

test_results = [33, 366, 259, 315, None, None, None, None, None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	da = test_days[i]
	print(da,"/",mo,"/",yr, " -> ", sep="", end="")
	result = day_of_year(yr, mo, da)
	print("result=", result, ", expected=", test_results[i], ", ", sep="", end="")
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
