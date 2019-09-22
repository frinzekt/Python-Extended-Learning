#
# Example file for formatting time and date output
#

from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()

    # Formatting with string holders
    print(now.strftime("Current year is: %Y"))

    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("%a, %d, %B, %y"))
    print(now.strftime("%A, %D, %b, %y"))

    # Local convention
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %x"))
    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Curretn time: %I:%M:%S %p"))
    print(now.strftime("Curretn time: %H:%M:%S"))


if __name__ == "__main__":
    main()
