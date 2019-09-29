#
# Example file for parsing and processing XML
#
# This is done for operating on ENTIRE DOCUMENT IN MEMORY
# operating on document DOM eg. python mini-DOM XML class

import xml.dom.minidom as xdm


def main():
    # use the parse() function to load and parse an XML file
    doc = xdm.parse("./Own Exercise/Ch5/samplexml.xml")

    # print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    # create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    # PRINTING OUT WILL RESULT IN A NEW THING


if __name__ == "__main__":
    main()
