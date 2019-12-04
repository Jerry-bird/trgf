import json
import random
import time
import unittest
import warnings

import jsonpath
import requests

from Conf.Oracle import Oracle
from Conf.url import url_award_save, url_login_admin, url_get_customer, url_performance_recalculation
from Lib.headers import heads2, token_admin, heads1


class AwardSave(unittest.TestCase):
    def test_award_save(self):
        # 忽略线程协助警告
        warnings.simplefilter("ignore", ResourceWarning)
        # 登录admin后台登录，使session有效
        url = url_login_admin
        data = {
            "username": "trgf",
            "password": "96e79218965eb72c92a549dd5a330112",
            "code": ""
        }
        res = requests.session().post(url, data=data, headers=heads2)
        print(res.json())

        url_award = url_award_save
        award = random.randint(1, 10)
        con_no = '260053555'
        data = {
            "conId": "7edd26fe79bc4944a4c991fa218d7f4d",
            "postName": "月度合伙人",
            "conNo": "260053555",
            "conName": "鸟呀'",
            "mobile": "15074814525",
            "postNo": "1",
            "award": award,
            "remark": "测试奖励"
        }
        res = requests.post(url_award, data=data, headers=heads2)
        # 审核通过
        oraDb = Oracle()
        sql_award = "Update TLD_AWARD_QTRANK Set is_dist = '1',FINANCE_CHECKRESULT = '1',status = '1' Where con_no =%s" % con_no
        ora_award = oraDb.query(sql_award)


if __name__ == '__main__':
    t = AwardSave()
    t.test_award_save()
