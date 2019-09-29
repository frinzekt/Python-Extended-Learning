#
# Example file for parsing and processing JSON
#
import urllib.request
import json

"""data Feed:
{
  type: "FeatureCollection",
  metadata: {
    generated: Long Integer,
    url: String,
    title: String,
    api: String,
    count: Integer,
    status: Integer
  },
  bbox: [
    minimum longitude,
    minimum latitude,
    minimum depth,
    maximum longitude,
    maximum latitude,
    maximum depth
  ],
  features: [
    {
      type: "Feature",
      properties: {
        mag: Decimal,
        place: String,
        time: Long Integer,
        updated: Long Integer,
        tz: Integer,
        url: String,
        detail: String,
        felt:Integer,
        cdi: Decimal,
        mmi: Decimal,
        alert: String,
        status: String,
        tsunami: Integer,
        sig:Integer,
        net: String,
        code: String,
        ids: String,
        sources: String,
        types: String,
        nst: Integer,
        dmin: Decimal,
        rms: Decimal,
        gap: Decimal,
        magType: String,
        type: String
      },
      geometry: {
        type: "Point",
        coordinates: [
          longitude,
          latitude,
          depth
        ]
      },
      id: String
    },
    …
  ]
}
"""


def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    # this is accessed using dictionary
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

      # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + "  events recorded")

    # for each event, print the place where it occurred
    for i, item in enumerate(theJSON["features"], 1):
        print(str(i)+". ", item["properties"]["place"])
    print("----------------")

    # print the events that only have a magnitude greater than 4
    for i, item in enumerate(theJSON["features"], 1):
        if item["properties"]["mag"] >= 4.0:
            print(str(i)+". ", "%2.1f" %
                  item["properties"]["mag"], item["properties"]["place"])
    print("----------------")

    # print only the events where at least 1 person reported feeling something
    print("Events that were felt:")
    for i, item in enumerate(theJSON["features"], 1):
        feltReports = item["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(str(i)+". ", "%2.1f" % item["properties"]["mag"],
                      item["properties"]["place"], " reported " + str(feltReports) + " times ")


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("ERROR")


if __name__ == "__main__":
    main()
