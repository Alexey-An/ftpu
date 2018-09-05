import ftplib
import unittest
import ftpm


class TestUM(unittest.TestCase):

    def setUp(self):
        self.ftp = ftplib.FTP('')
        self.ftp.connect('localhost', 2121)
        self.ftp.login("user", "12345")

    def test_1(self):
        self.assertTrue(ftpm.download_file(self.ftp, 'bf.txt', '/home/alexey2/testfold/bf.txt'))

    def test_2(self):
        self.assertTrue(ftpm.upload_file(self.ftp, '/home/alexey2/testfold/bf.txt'))

    def tearDown(self):
        self.ftp.quit()
        pass


if __name__ == '__main__':
    unittest.main()