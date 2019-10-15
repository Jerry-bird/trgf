import json
import unittest

import requests
import jsonpath as jsonpath

from MainExecute.readConfig import ReadConfig

from DataSource.readExcel import readExcel

xls_info = readExcel().get_xls('personinfo.xls', 'Sheet1')

openid = xls_info[1][0]
# print(openid)
unionid = xls_info[1][1]
# print(unionid)

url = ReadConfig().get_http('baseurl') + '/ms-auth/auth/app/login/wechat'
# print(url)
data = {"openidApp": openid, "unionid": unionid}
headerP = {"version": "3.2.0", "mobileBrand": "IOS", "anonymousId": "6E7B9681-F967-4728-8303-DA04C16A253B"}
heads = {
    "channel": "5",
    'headerParams': json.dumps(headerP),
    "Authorization": "d2a57dc1d883fd21fb9951699df71cc7"
}


class LoginWechat(unittest.TestCase):

    # @staticmethod
    def test_login_wechat(self):
        res = requests.post(url, json=data, headers=heads)
        # print(respon.status_code)
        if res.status_code == 200:
            token = jsonpath.jsonpath(res.json(), '$.data.token')[0]
            msg1 = jsonpath.jsonpath(res.json(), '$.msg')[0]
            self.assertEqual(msg1, '成功')
            if token:
                return token
            else:
                return '无token'
        else:
            return '授权失败'


if __name__ == '__main__':
    t = LoginWechat()
    t.test_login_wechat()
