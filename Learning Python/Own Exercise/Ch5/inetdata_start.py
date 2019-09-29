#
# Example file for retrieving data from the internet
#
import urllib.request  # url requesters HTTP


def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code:" + str(webUrl.getcode()))
    print("URL:" + str(webUrl.geturl()))

    data = webUrl.read()
    print(data)

    # save HTML code
    with open("htmlcode.html", "w+") as myfile:
        myfile.write(str(data))


if __name__ == "__main__":
    main()
