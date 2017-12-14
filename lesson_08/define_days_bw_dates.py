# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
def days_of_month(month):

	days_of_month = 0

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 31	

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 28

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 31

	if month > 1:

		month = month - 1		

		days_of_month = days_of_month + 30

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 31

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 30

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 31

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 31

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 30

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 31

	if month > 1:

		month = month - 1

		days_of_month = days_of_month + 30

	return days_of_month        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
	result = (year2 - year1) * 365 + days_of_month(month2) - days_of_month(month1) + day2 - day1

	year = year1

	while True:

		if isLeapYear(year):

			result = result + 1

			year = year + 1

			if year > year2:

				break

		year = year + 1

		if year > year2:

			break
    return

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
