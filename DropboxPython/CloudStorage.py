
import dropbox
import os

class TransferData :
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'F88mcCUNBDoAAAAAAAAAAWpTKLlhrcX_oa-Gc3THMG_uqs3frBwAjH_Cv7MLIcZZ'
    transferData = TransferData(access_token)

    file_from = input("Enter The File Path To Transfer")
    file_to = input("Enter The Full Path To Upload To Dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

    main()
