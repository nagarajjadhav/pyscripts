#!python3
#script to add bullets to each newline
import pyperclip
text = pyperclip.paste()
line = text.split('\n')
for i in range(len(line)):
    line[i]= '* '+line[i]
text = '\n'.join(line)
pyperclip.copy(text)
