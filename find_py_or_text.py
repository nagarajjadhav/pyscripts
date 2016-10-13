#!python3
#script to create bcakup for files ending with .py
import zipfile,os,re

def findpy(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipfilename = os.path.basename(folder)+'_'+str(number)+'_'+'py'+'.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1
    print('creating %s............'%(zipfilename))
    backupzip = zipfile.ZipFile(zipfilename,'w')

    for foldername,subfoldername,filename in os.walk(folder):
        print('adding files in %s.....'%(foldername))
        backupzip.write(foldername)
        
        for filename in filename:
            mo = re.search(r'^(.*)\.py',filename)
            if mo:
                backupzip.write(os.path.join(foldername,filename))
            else:
                continue
    print('done')
findpy('projects')

#*******************************creates backup for non .py**************************

#!python3
import zipfile,os,re

def findpy(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipfilename = os.path.basename(folder)+'_'+str(number)+'_'+'py'+'.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1
    print('creating %s............'%(zipfilename))
    backupzip = zipfile.ZipFile(zipfilename,'w')

    for foldername,subfoldername,filename in os.walk(folder):
        print('adding files in %s.....'%(foldername))
        backupzip.write(foldername)
        
        for filename in filename:
            mo = re.search(r'^(.*)\.py',filename)
            if not mo:
                backupzip.write(os.path.join(foldername,filename))
            else:
                continue
    print('done')
findpy('projects')

