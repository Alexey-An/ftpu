import ftplib
import unittest
import ftpm


class TestUM(unittest.TestCase):

    def setUp(self):
        self.ftp = ftplib.FTP('')
        self.ftp.connect('localhost', 2121)
        self.ftp.login("user", "12345")
        self.file_to_download = ""   #<--- указать имя файла, который требуется загрузить с сервера
        self.savepath = ""           #<--- указать путь, где будет записан загружаемый файл
        self.file_to_upload = ""     #<--- указать файл, который требуется выгрузить на сервер

    def test_download(self):
        self.assertTrue(ftpm.download_file(self.ftp, self.file_to_download, self.savepath))

    def test_upload(self):
        self.assertTrue(ftpm.upload_file(self.ftp, self.file_to_upload))



    ''' Данная конфигурация использовалась для запуска тестов на локальном компьютере.    
    
    def test_download(self):
        self.assertTrue(ftpm.download_file(self.ftp, 'bf.txt', '/home/alexey2/testfold/bf.txt'))

    def test_upload(self):
        self.assertTrue(ftpm.upload_file(self.ftp, '/home/alexey2/testfold/bf.txt'))
    '''

    def tearDown(self):
        self.ftp.quit()
        pass


if __name__ == '__main__':
    unittest.main()