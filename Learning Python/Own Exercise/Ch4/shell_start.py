#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

myfile = "textfile.txt"


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):

        # get the path to the file in the current directory
        src = path.realpath(myfile)

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"
        pathdst, taildst = path.split(dst)

        # copy over the permissions, modification times, and other info
        shutil.copy(src, dst)

        # for copying metadata included
        shutil.copystat(src, dst)

        # rename the original file
        #os.rename(dst, "newfile.txt.bak")

        # now put things into a ZIP archive
        # REMEMBER LIKE ES6 Destructuring
        # root_dir, tail = path.split(src)
        # make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        # object constructor
        """ with creates local scope simplifying working with object
        creates object that is temporarily named"""

        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write(myfile)
            newzip.write(taildst)


if __name__ == "__main__":
    main()
