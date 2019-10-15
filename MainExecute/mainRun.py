# coding=utf8
import HTMLTestRunner
import unittest


class mainRun(unittest.TestCase):

    def test_01(self):
        print('test01')

    def test_02(self):
        print('test02')


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(mainRun('test_02'))
    # suite.addTest(mainRun('test_01'))
    # unittest.TextTestRunner().run(suite)
    filepath = './Report/htmlreport.html'
    fp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(mainRun('test_02'))
    suite.addTest(mainRun('test_01'))
    runer = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
    runer.run(suite)