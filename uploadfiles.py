import dropbox
import os

class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        relative_path=os.path.relpath(file_from)
        dropbox_path=os.path.join(file_to,relative_path)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode=dropbox.files.WriteMode.overwrite)

def main():
        access_token="cTLGrtkiY1IAAAAAAAAAAWnW4MXsG7Cic9NEGSkOQJx9n-M5nQnbrZaHQjLK_FzO"
        transfer_data=Transferdata(access_token)
        file_from="test.txt"
        file_to="/project_dropbox/test.txt"

        transfer_data.upload_file(file_from,file_to)

main()