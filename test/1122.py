# import unittest
# #
# #
# # class test(unittest.TestCase):
# #     def test(self):
# #         a = 1
# #         b = 1
# #         if self.assertEqual(a, b):
# #             print('正确')
# #         else:
# #             print('错误')
import sys
import random


def wait_input(a, b):
    print('调用了wait_input')
    # with open('random_funcs.txt', 'a', encoding='utf8') as f:
    #     f.write('调用了wait_input' + '\n')


def batch_input(a, b):
    print('调用了batch_input')
    # with open('random_funcs.txt', 'a', encoding='utf8') as f:
    #     f.write('调用了batch_input' + '\n')


if __name__ == '__main__':
    for i in range(0, 3):
        calls = [('wait_input', [1, 2]), ('batch_input', [3, 4])]
        choice = random.choice(calls)
        this_module = sys.modules[__name__]
        getattr(this_module, choice[0])(*choice[1])