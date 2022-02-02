import dropbox

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,source,destination):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(source,'rb')
        dbx.files_upload(f.read(),destination)

def main():
    access_token="sl.BBMijlzV6JSnhVlFCBEs9fB6m6w-mOgF6IjZNofViMUV4_J402QEa-kJ2YTqWySbCcC3C6Y54CmtK-O0vJhPaIn7qc2hqDzlpoOnyKQuyrp6Vk_ggjsxY69OC9adVKMS88mmkFd00OVe"
    object= Transferdata(access_token)
    source= input("Enter the file path to transfer:")
    destination=input("Enter the path to upload dropbox:")
    object.upload_file(source,destination)
    print("File uploaded successfully")

# if __name__ == _main_:
main()


