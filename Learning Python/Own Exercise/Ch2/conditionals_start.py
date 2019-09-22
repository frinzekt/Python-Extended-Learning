#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100
    st = ""

    # conditional flow uses if, elif, else
    if(x < y):
        st = "x is less than y"
    elif(x > y):
        st = "x is greater than y"
    else:
        st = "x is the same as y"

    print(st)

    # there is no such thing as switch statement
    st = "x is less than y" if (x < y) else "x is greater or equal than y"
    print(st)

    # Not valid
    # st = (x < y) ? "x is less than y": "x is greater or equal to y"


if __name__ == "__main__":
    main()
