# coding=utf-8
import HTMLTestRunner
import unittest
from unittest import defaultTestLoader

# 测试用例存放路径
case_path = '../MainInterface'


# 获取所有测试用例
def get_allCase():
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


if __name__ == '__main__':
    filepath = '../Lib/res.html'
    fp = open(filepath, 'wb')  # 打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='天然工坊自动化测试报告', description='测试详情')
    # 运行测试用例
    #runner = unittest.TextTestRunner()
    runner.run(get_allCase())
