import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
for root,dirs,files in os.walk(file_from)
relative_path=os.path.relpath(local_path,file_from)
dropbox_path=os.path.join(file_to,relative_path)
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)


    with open(local_path,'rb') as f:
        dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
 

def main():
    access_token='https://auth0.com/docs/tokens/access-tokens'
    transferData=TransferData(access_token)
    file_from=input('Enter the file path to transfer:-')
    file_to=input('enter the full path to upload to dropbox:-')

    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")