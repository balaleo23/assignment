import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


## input from the user for choosing the function to trigger
""" 
  function_requested_by_the_user :
      
      Expected commands to work:
        ls - list files,
        rm - remove file,
        cp - copy file from local to drive, drive to local
        help - to list usage

//  Note: all the functionality is extended only for the root folder. //

"""



    

def ls():
    
        # View all folders and file in your Google Drive
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()  #get the list of files
    for file in fileList:
        #print('Title: ' + file['title'] + " ID: " + file['id'])
        print('Title: %s, ID: %s' % (file['title'], file['id']))

def rm():
    
    
    file_to_be_removed = sys.argv[2]
    #print(file_to_be_removed)
    file_to_be_removed_id = ""
    #get the id of the file to be removed
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()  #get the list of files
    for file in fileList:
        if(file['title'] == file_to_be_removed):
                file_to_be_removed_id = file['id']

    if file_to_be_removed_id == "":
        print("File not found")

    else:
        delete_the_file = drive.CreateFile({'id': file_to_be_removed_id}) 
        delete_the_file.Delete()
        print("file deleted")

def cptodrive():

    file_to_be_uploaded = sys.argv[2]
    upload_the_file = drive.CreateFile() 
    upload_the_file.SetContentFile(file_to_be_uploaded) #the file path has to be mentioned here while uploading
    upload_the_file.Upload()
    print("file successfully uploaded")

def cptolocal():


    file_to_be_downloaded = sys.argv[2]
    file_to_be_downloaded_id = ""
    #get the id of the file to be removed
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()  #get the list of files
    for file in fileList:
        if(file['title'] == file_to_be_downloaded):
                file_to_be_downloaded_id = file['id']

    if file_to_be_downloaded_id != "":

        download_file_to_local = drive.CreateFile({'id': file_to_be_downloaded_id})
        download_file_to_local.GetContentFile(file_to_be_downloaded) # Download file as 'catlove.png'.
        print("The requested file is downloaded")

    else:
        print("File not found")

def details():
        
            print("ls command use to list the files")
            print("rm command use to remove the files")
            print("cptodrive command use to upload the files")
            print("cptolocal command use to download the files")

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)  

try:
    function_requested_by_the_user = sys.argv[1]
except:
    function_requested_by_the_user = 'values for argument is missing'


if function_requested_by_the_user == 'ls':
     ls()
elif function_requested_by_the_user == 'rm':
     rm()
elif function_requested_by_the_user == 'cptodrive':
     cptodrive()
elif function_requested_by_the_user == 'cptolocal':
     cptolocal()
elif function_requested_by_the_user == 'details':
     details()
else:   
    print('values for argument is missing')

