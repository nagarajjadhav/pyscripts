#!python3
#download every single xkcd comics right untill top
import os ,bs4,requests

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('1739/'):
    print('downloading the web page %s........'%url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'lxml')
    comicEle = soup.select('#comic img')
    if comicEle == []:
        print("couldnot find image.")
    else:
        comicUrl = 'http:'+comicEle[0].get('src')
        print("Downloading comic image %s........."%(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imgfile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imgfile.write(chunk)
        imgfile.close()
    prevlink =  soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevlink.get('href')
print('done')
  


    
