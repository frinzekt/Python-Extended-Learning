#
# Example file for working with loops
#


def main():
    x = 0

    # define a while loop

    while(x < 5):
        print(x)
        x += 1

    # define a for loop
    # python does not have for(int i =0; i<0; i++)
    # for loop operates on range of numbers/ collection

    for x in range(5, 10):
        print(x)

    # use a for loop over a collection
    days = ["Monday", "tue", "wed"]
    for d in days:
        print(d)

    # use the break and continue statements
    for i in range(5, 10):
        if(i == 7):
            break
        print(i)

    for i in range(5, 10):
        if(i == 7):
            continue
        print(i)

    # using the enumerate() function to get index
    days = ["Monday", "tue", "wed"]
    # enumaration mixes both the index and the value of the list together
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()
