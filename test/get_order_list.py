import json

import jsonpath
import requests

# from MainInterface.login import get_token
from test.login import Login

sso = Login(url="https://test-admin2-api.hntrgf.com.cn/auth/login", username="trgf", password="96e79218965eb72c92a549dd5a330112")
print(dir(sso))
token = sso.get_token

# token = get_token()
url2 = "https://test-admin2-api.hntrgf.com.cn/biz/orders/orderlist"
params = {"dateType": "1", "beginDate": "2019-08-06 19:57:37", "endDate": "2019-09-05 23:59:59", "orderNo": "",
          "conNo": "", "keyword": "", "waybillNo": "", "provinceId": "", "cityId": "", "distinctId": ""}

data2 = {"params": json.dumps(params),
         "pageNum": 1,
         "pageSize": 10}
headers2 = {
    "Authorization": token
}

response2 = requests.get(url2, params=data2, headers=headers2)
print(response2.json())
real= jsonpath.jsonpath(response2.json(), '$.data.resultData[0].orderId')
print(real)
try:
    assert real[0] == '0234feda8710483aafe0e76b2d42eb691', "不相等"
except:
    print("不想扥")