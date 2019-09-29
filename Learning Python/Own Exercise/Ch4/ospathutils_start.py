#
# Example file for working with os.path module
#
import os
from os import path
import datetime as dt
from datetime import date, time, timedelta
import time

myfile = "textfile.txt"


def main():
    # Print the name of the OS
    print(os.name)
    print(os.path)

    # Check for item existence and type
    print("Item exists: "+str(path.exists(myfile)))  # for from import
    # print("Item exists: "+str(os.path.exist(myfile))) # for without for import

    print("Item is file:" + str(path.isfile(myfile)))
    print("Item is directory:" + str(path.isdir(myfile)))

    # Work with file paths
    print("Item path: " + str(path.realpath(myfile)))
    print("Item path and name: " + str(path.split(path.realpath(myfile))))

    # Get the modification time
    # ctime is the default format of the time with relative to a certain date
    t = time.ctime(path.getmtime(myfile))
    print(t)
    print(path.getmtime(myfile))
    print(dt.datetime. fromtimestamp(path.getmtime(myfile)))

    # Calculate how long ago the item was modified
    td = dt.datetime.now() - dt.datetime.fromtimestamp(path.getmtime(myfile))

    print("It has been " + str(td) + " since the file was modified")
    print("Or " + str(td.total_seconds()) + "secs")


if __name__ == "__main__":
    main()
