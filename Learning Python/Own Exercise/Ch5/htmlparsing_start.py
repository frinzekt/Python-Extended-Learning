#
# Example file for parsing and processing HTML
#

from html.parser import HTMLParser
import os

# OVERWRITE THE ALREADY BUILT CLASS BY INHERITANCE

metacount = 0  # counter of meta tags


class MyHTMLParser(HTMLParser):
      # the name of the method SHOULD BE THE NAME OF THE ORIGINAL METHOD
    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        # returns line number and position
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
          # start at the TITLE TAG
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encountered tag: ", tag)
        pos = self.getpos()
        # returns line number and position
        print("\tAt line: ", pos[0], " position ", pos[1])

        # checking presence of attributes by the length
        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])
                # attribute name and value

    def handle_endtag(self, tag):
        print("Encountered comment: ", tag)
        pos = self.getpos()
        # returns line number and position
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if (data.isspace()):
            return  # for return if empty data NO PRINT
        print("Encountered data: ", data)
        pos = self.getpos()
        # returns line number and position
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("./Own Exercise/Ch5/samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

    print("Meta count: ", str(metacount))


if __name__ == "__main__":
    main()
