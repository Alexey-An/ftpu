import ftplib
import os


# данный метод принимает три параметра:
# 1) ftp-сервер (в данном примере используется ftp-сервер запущенный локально)
# 2) имя файла, который необходимо загрузить с сервера
# 3) путь на локальной машине, куда будет записан файл, загружаемый с сервера
def download_file(ftp_server, filename, savepath):
    try:
        local = open(savepath, 'wb')
        ftp_server.retrbinary('RETR ' + filename, local.write, 1024)
        local.close()
        return True
    except:
        print("Something's gone wrong. Download failed.")
        return False


# данный метод принимает два параметра:
# 1) ftp-сервер (в данном примере используется ftp-сервер запущенный локально)
# 2) имя файла, который необходимо выгрузить на сервер

def upload_file(ftp_server, filename):
    try:
        ext = os.path.splitext(filename)[1]
        if ext in (".txt", ".htm", ".html"):
            ftp_server.storlines("STOR " + filename, open(filename))
            return True
        else:
            ftp_server.storbinary("STOR " + filename, open(filename, "rb"), 1024)
            return False
    except:
        print("Something's gone wrong. Upload failed.")

def uploadF(ftp_server, filename):
    try:
        ftp_server.storbinary('STOR ' + filename, open(filename, 'rb'), 1024)
        ftp_server.quit()
        return True
    except:
        print("Something's gone wrong. Upload failed")
        return False


if __name__ == "__main__":

    ftp = ftplib.FTP('')
    ftp.connect('localhost',2121)
    ftp.login("user", "12345")
    #ftp.cwd('') #replace with your directory
    ftp.retrlines('LIST')
    print(ftp.login("user", "12345"))
    print(ftp.getwelcome())

    download_file(ftp, 'bf.txt', '/home/alexey2/testfold/bf.txt')
    upload_file(ftp, '/home/alexey2/testfold/bf.txt')
    uploadF(ftp, '/home/alexey2/testfold/bf.txt')



