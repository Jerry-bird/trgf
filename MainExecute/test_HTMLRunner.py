# import HTMLTestRunner
# import unittest
#
#
# class MyTest(unittest.TestCase):  # 继承unittest.TestCase
#     def tearDown(self):
#         # 每个测试用例执行之后做操作
#         print('111')
#
#     def setUp(self):
#         # 每个测试用例执行之前做操作
#         print(22222)
#
#     def test_run(self):
#         # self.assertEqual(1,1)
#         self.assertIs(1, 2)
#         # 测试用例
#
#     def test_run2(self):
#         # self.assertEqual(1,1)
#         self.assertIs(1, 1)
#         # 测试用例
#
#     def test_run3(self):
#         # self.assertEqual(1,1)
#         self.assertIs(1, 1)
#         # 测试用例
#
#     def test_run1(self):
#         # self.assertEqual(1,1)
#         self.assertIs(1, 1)
#         # 测试用例
#
#
# if __name__ == '__main__':
#     test_suite = unittest.TestSuite()  # 创建一个测试集合
#     test_suite.addTest(MyTest('test_run1'))  # 测试套件中添加测试用例
#     test_suite.addTest(MyTest('test_run2'))
#     test_suite.addTest(MyTest('test_run3'))
#     # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
#     fp = open('../Lib/res.html', 'wb')  # 打开一个保存结果的html文件
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='天然工坊自动化测试报告', description='测试详情')
#     # 生成执行用例的对象
#     runner.run(test_suite)
#     # 执行测试套件
# coding=utf-8
# import HTMLTestRunner
from HTMLTestRunner_PY3 import HTMLTestRunner_PY3
import os
import unittest
import time
from unittest import defaultTestLoader

# 测试用例存放路径
case_path = "../MainInterface"


# case_path = os.path.join(os.path.abspath('..'), 'MainInterface')


# 获取所有测试用例
def get_allcase():
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="*.py")
    # print(discover)
    suite = unittest.TestSuite()
    # [suite.addTests(case) for case in discover]
    suite.addTest(discover)
    return discover


def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new


if __name__ == '__main__':
    # fp = open('../Report/res.html', 'wb')  # 打开一个保存结果的html文件
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='天然工坊自动化测试报告', description='测试详情')
    # # 运行测试用例
    # # runner = unittest.TextTestRunner()
    # runner.run(get_allcase())
    # fp.close()
    # 取当前时间
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    print(now)
    # 保存生成报告的路径
    report_path = "C:\\Users\\lp403\\PycharmProjects\\trgf\\Report\\" + now + "_result.html"
    print(report_path)
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp,
                                               title=u"自动化测试用例",
                                               description=u"用例执行情况",
                                               verbosity=2
                                               )
    # run 所有用例
    runner.run(get_allcase())
    # 关闭文件，记住用open()打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。
    fp.close()
