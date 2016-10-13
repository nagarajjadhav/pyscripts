#!python3
#creates a copy of zip file to backup our content
import zipfile,os,sys

def backuptozip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipfilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1
    print('creating %s............'%(zipfilename))
    backupzip = zipfile.ZipFile(zipfilename,'w')

    for foldername,subfoldername,filename in os.walk(folder):
        print('adding files in %s.....'%(foldername))
        backupzip.write(foldername)
        
        for filename in filename:
            newbasefile=os.path.basename(folder)+'_'
            if filename.startswith(newbasefile) and filename.endswith('.zip'):
                continue
            backupzip.write(os.path.join(foldername,filename))
    print('done')
backuptozip('projects')



        
           
