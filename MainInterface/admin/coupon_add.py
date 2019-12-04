import random

import requests
from requests_toolbelt import MultipartEncoder

from Conf.Oracle import Oracle
from Conf.mySql import Mysql
from Conf.url import url_coupon_add
from Lib.headers import heads2

oraDb = Mysql()
coupon_name = 'test_lp'
sql = '''SELECT * FROM sp_coupon  WHERE enabled= 1 and coupon_name =(%s)'''

coupon_id = str(oraDb.queryBy(sql, coupon_name)[0][0])

url = url_coupon_add + coupon_id + '/COUPON_001'

print(url)
'''
multipart_encoder = MultipartEncoder(
    fields={
        'save_data': ('file', open('C://Users/lp403/PycharmProjects/trgf/Conf/excel/coupon.xls', 'rb'),
                      'application/vnd.ms-excel')
    },
    boundary='----WebKitFormBoundaryv73bzO8Vxu4MIBvQ'
)
heads2['Content-Type'] = multipart_encoder.content_type
print(heads2['Content-Type'])
'''
files = {'file': ('coupon.xls', open('coupon.xls', 'rb'),
                  'application/vnd.ms-excel')}
print(heads2)
r = requests.post(url=url, files=files, headers=heads2)
print(r.json())
