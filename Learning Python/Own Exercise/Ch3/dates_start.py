#
# Example file for working with date information
#
from datetime import date  # only for date
#from datetime import time
from datetime import datetime  # for mix retrieval


def main():
    # DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today is ", today)
    # print out the date's individual components
    day = today.day
    month = today.month
    year = today.year

    print("Date components: ", day, month, year)
    # retrieve today's weekday (0=Monday, 6=Sunday)
    weekday = today.weekday()
    print("Today Weekday # is", weekday)
    # Weekday number could be used as an index for a weekday list

    # DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print(today)

    # Get the current time
    t = datetime.time(today)
    print((t))


if __name__ == "__main__":
    main()
