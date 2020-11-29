import os,shutil

folder={
'audio_extensions':('.mp3','.m4a','.wav'),
'vedios_extensions':('.mp4','.mkv','.mpeg'),
'documents_extensions':('.doc','.txt','.pdf','.py','.cpp'),
'Software_extensions':('.exe')

}
folderpath=input("enter path of folder :".title())

def file_finder(folder_path,file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files
##
##
##t=file_finder(folderpath,documents_extensions)
##for i in t:
##    print(i)
##        


for i,j in folder.items():# here i,j is key and value pair respectively
    folder_name=i.split('_')[0]+' Files'
    folder_path=os.path.join(folderpath,folder_name)
    files=(file_finder(folderpath,j))
    if files:
        os.mkdir(folder_path)
        for item in  files:# j is tuple of extensions
            itempath=os.path.join(folderpath,item)
            new_itempath=os.path.join(folder_path,item)
            shutil.move(itempath,new_itempath)
##        
##        shutil.move('itempath',folder_path+'\\item')
      





















      
##    a=a+'.txt'
##    open(a,'a').close()
##    with open(a,'a') as cf:
##        l=cf.readlines()
##        index=len(l)-1
##        for add_file in t:
##            index+=1
##            cf.write(f'{index}... {add_file} \n')
##            
          

    ## printing files in folder
##    print(f'\n-------------------{a} files------------------\n')
##    c=1
##    for f in t:
##        print(f'{c}._  {f}')
##        c+=1






















    
