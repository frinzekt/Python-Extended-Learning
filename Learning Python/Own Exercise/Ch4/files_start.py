#
# Read and write files using the built-in Python file methods
#


def main():
    # Open a file for writing and create it if it doesn't exist
   # myfile = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    myfile = open("textfile.txt", "a+")

    # write some lines of data to the file
    for i in range(10):
        # myfile.write("this is line " + str(i) + "\n")
        print("this is line", i, file=myfile)

    # close the file when done
    myfile.close()

    # Open the file back up and read the contents
    """ myfile = open("textfile1.txt", "r")
    if myfile.mode == 'r':  # check if successfully loaded
        # contents = myfile.read()  # reading full content
        fl = myfile.readlines()  # aarray of string lines

        print(fl)

    myfile.close()"""

    # With open no need closing
    with open("textfile1.txt", "r") as myfile:
        fl = myfile.readlines()
        print(fl)


if __name__ == "__main__":
    main()
