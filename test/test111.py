import HTMLTestRunner
import os
import unittest


class runMain(unittest.TestCase):

    def test_01(self):
        self.assertEqual(1, 1)

    def test_02(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    filepath = '../Lib/res.html'
    fp = os.open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(runMain('test_02'))
    suite.addTest(runMain('test_01'))
    runer = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
    runer.run(suite)
