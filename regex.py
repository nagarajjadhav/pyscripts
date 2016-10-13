#script to find a particluar file and content in an directory.
import re,os
pat = re.compile('.*\.txt')
for i in os.listdir():
    if pat.search(i):
        print("Bingo!!!!found the file you were looking :",i)
        print("enter your string to be serached in the file")
        str1 = input()
        f = open(i)
        if re.search(str1,f.read()):
            print("found your string %s in %s file"%(str1,i))
        else:
            print("sorry we didnt found what you were looking for")
        f.close()

    
