import json

from Lib.auth_login import auth_login
from Lib.login_wechat import LoginWechat

# 消息头

token = LoginWechat().test_login_wechat()
token_admin2 = auth_login()
# headerP = {"version": "3.2.0", "mobileBrand": "IOS", "anonymousId": "6E7B9681-F967-4728-8303-DA04C16A253B"}\
headerP = {"mobileBrand": "IOS", "anonymousId": "6E7B9681-F967-4728-8303-DA04C16A253B",
           "mobileIdentity": "623B0B2878E343339836170048A537C8", "version": "3.4.0"}
heads = {
    "channel": "5",
    'headerParams': json.dumps(headerP),
    "Authorization": token,
    "Content-Type": "application/json"
}
headerP1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/68.0.3440.106 Safari/537.36 "
}
heads1 = {
    "Authorization": token_admin2,
    'headerParams': json.dumps(headerP1),
    "Content-Type": "application/json;charset=UTF-8",

}
# print(heads1)
