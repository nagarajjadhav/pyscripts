#python3
#renames file with date from american style(mm-dd-yyyy) to eurpean style(dd-mm-yyyy)
import shutil,re,os
datepat = re.compile(r'''^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
''',re.VERBOSE)
mo = datepat.search('12-03-1991')

for amefile in os.listdir('.'):
    mo = datepat.search(amefile)
    if mo == None:
        continue
    beforedata = mo.group(1)
    monthdata = mo.group(2)
    daydata = mo.group(4)
    yeardata = mo.group(6)
    afterdata = mo.group(8)

    eurofile = beforedata+daydata+'-'+monthdata+'-'+yeardata

    absworkingdir = os.path.abspath('.')
    amefile = os.path.join(absworkingdir,amefile)
    eurofile = os.path.join(absworkingdir,eurofile)

    print('renaming %s with %s'%(amefile,eurofile))
    shutil.move(amefile,eurofile)
    
    
