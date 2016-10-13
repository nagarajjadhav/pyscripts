#!python3
#script to open top searched websites for a keyword
import sys,webbrowser,bs4,requests

print("googling.........")
res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'lxml')
linkelements = soup.select('.r a')

numopen = min(5,len(linkelements))
for i in range(numopen):
    webbrowser.open('http://google.com'+linkelements[i].get('href'))
