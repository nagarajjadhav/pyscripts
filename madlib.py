import re
f = open('content.txt')
a = f.read().split()

f.close()
print(a)
for i in range(len(a)):
    if re.search('ADJECTIVE',a[i]):
        adj = input("enter an adjective :")
        a[i]=adj
    elif re.search('NOUN',a[i]):
        noun = input("enter a noun :")
        a[i]=noun
    elif re.search('VERB',a[i]):
        ver = input("enter a verb :")
        a[i]=ver
newcontent = ' '.join(a)
print(newcontent)
newfile = open('newfile.txt','w')
newfile.write(newcontent)
newfile.close()
