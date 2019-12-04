import json
import unittest

import jsonpath
import requests

from Conf.url import url_template_insert
from Lib.headers import heads1

# 新增快递模板


class TemplateInsert(unittest.TestCase):
    def Template_insert(self):
        url = url_template_insert
        data = {"tmplName": "自动化运费模板", "tmplDesc": "自动化运费模板"}
        res = requests.post(url=url, data=json.dumps(data), headers=heads1)
        # print(res.json())
        msg = jsonpath.jsonpath(res.json(), '$.msg')[0]
        self.assertEqual(msg, '成功')


if __name__ == '__main__':
    t = TemplateInsert()
    t.test_template_insert()
