import dropbox

class TransferData:
    def __init__(self,access_token):
        self.accessToken=access_token
    
    def uploadFile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accessToken)

        f=open(filefrom,"rb")
        dbx.files_upload(f.read(),fileto)

def main():
    accesToken="sl.A_Il3FBIbul69jPkgia6zUdvgbOs4rW115ukDVAJLjb3h467aQo_VuvB4WkvItbOnU4g8AtJnz46nI3GBxCW9QwIs7h0wx-yepuUv9l2pcqUzmgeXH7qymFtfSrSD-SF0es1NgE"
    transferdata=TransferData(accesToken)

    fileFrom=input("your  file name : ")
    fileTo=input("the destination : ")

    transferdata.uploadFile(fileFrom,fileTo)
    print("the files have been saved")

main()