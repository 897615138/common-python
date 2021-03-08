# windows

'readTextFile.py -- read and display text file'

# get filename
from pip._vendor.distlib.compat import raw_input

fname = raw_input("Enter filename:")
# attempt to open file for reading
try:
    fObj = open(fname, 'r')
    # display contents to the screen
    for eachLine in fObj:
        print(eachLine)
        fObj.close()
    print()
    raw_input("Press Enter to Continue !")
except IOError as e:
    print("*** file open error:", e)
