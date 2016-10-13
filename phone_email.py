#!python3
# fetches phone and email id from a web page if present

import pyperclip
import re

phone_pat = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

email_pat = re.compile(r'''(
[a-zA-Z0-9_%+.-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,3})
)''',re.VERBOSE)

website_pat = re.compile(r'(http)')

text = str(pyperclip.paste())
matches = []

for groups in phone_pat.findall(text):
    phonenum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phonenum += ' x'+groups[8]
    matches.append(phonenum)
for groups in email_pat.findall(text):
    matches.append(groups[0])

'''for groups in website_pat.sub('https',text):
    matches.append(groups[0])'''

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print("no phone number or email id found")

#r'^\d{3}(,\d{3})*$'(regex to find three numbers repeated by comma)
    
    
