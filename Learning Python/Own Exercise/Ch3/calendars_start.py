#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print(st)

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)  # STATES STARTING OF CAL
st = c.formatmonth(2018, 1, 0, 0)  # formatting of the month into text string
print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2018, 1):
    print(i)

# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

# Calculate days based on a rule: For example, consider
for day in calendar.day_name:
    print(day)

# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team Meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2018, m)

    # check if the week1 or week2 has the first driday
    week1 = cal[0]
    week2 = cal[1]

    # week1[calendar.FRIDAY] returns the day of the friday of week1 or returns 0 if there is no friday
    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]

    print("%10s %2d %5d" % (calendar.month_name[m], meetday, 2018))
