#!python3
# open a map for the particular address passed
import webbrowser,pyperclip,sys

if len(sys.argv)>1:
    address = ' '.join(sys.argrv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://maps.google.com/maps/place/'+address)
