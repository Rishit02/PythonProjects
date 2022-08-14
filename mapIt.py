# mapIt.py launches a map in the browser using an address
# command line or clipboard

import webbrowser, sys, pyperclip
# sys.argv variable stores a list of the program’s filename and command line arguments
# if its len is greater than one than command line arguments hv been provided
# sys.argv is a list of strings
if len(sys.argv)>1:
    # Get address from commandline and store it as a string
    address = "".join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
 
