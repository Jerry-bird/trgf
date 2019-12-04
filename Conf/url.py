from MainExecute.readConfig import ReadConfig

'''前端接口'''
# 微信授权登录
url_login_wechat = ReadConfig().get_http('baseurl') + '/ms-auth/auth/app/login/wechat'
# 优惠券详情
url_active_payed_coupon = ReadConfig().get_http('baseurl') + '/ms-promotion/coupon-detail/active/payed/coupon'

# 获取默认地址
url_address_default = ReadConfig().get_http('baseurl') + '/ms-order/member-address/address/isdefault'

# 广告列表
url_advertisement_list = ReadConfig().get_http('baseurl') + '/ms-promotion/promotion/advertisement/list?adPosition=1'

# 我的邀请任务
url_assist_myList = ReadConfig().get_http('baseurl') + '/ms-promotion/assist-free/myself/index'

# 购物车列表
url_cart_list = ReadConfig().get_http('baseurl') + '/ms-goods/cart/list'

# 购物车总数
url_cart_sum = ReadConfig().get_http('baseurl') + '/ms-goods/cart/sum'

# 下单确认校验
url_confirm_check = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/confirm/check'

# 加入购物车
url_cart_insert = ReadConfig().get_http('baseurl') + '/ms-goods/cart/insert'

# 立即购买
url_query_quick = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/confirm/query/quick'

# 商品评论数
url_product_review = ReadConfig().get_http('baseurl') + '/ms-goods/reviews/countproductreview/'

# 优惠券首页列表
url_coupon_home_list = ReadConfig().get_http('baseurl') + '/ms-promotion/coupon/homepage/list'

# 商品详情优惠券列表
url_coupon_list = ReadConfig().get_http('baseurl') + '/ms-promotion/coupon/listbystatus'

# 配置列表
url_config_list = ReadConfig().get_http('baseurl') + '/ms-sys/api-config-cache/list'

# 获取用户信息
url_get_info = ReadConfig().get_http('baseurl') + '/ms-member/customer/info/get'

# 首页商品列表
url_index_list = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/all/list'

# 商品详情
url_index_detail = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/detail/new/'

# 运营位列表
url_operation_list = ReadConfig().get_http('baseurl') + '/ms-sys/operation-navigation/operation/list'

# 验证首购新增订单
url_check_add = ReadConfig().get_http('baseurl') + '/ms-order/order/cherk/add'

# 订单详情
url_order_info = ReadConfig().get_http('baseurl') + '/ms-order/order/info/'

# 用户下单
url_order_put = ReadConfig().get_http('baseurl') + '/ms-order/order-put/order/member/put'

# 下单运费
url_order_put_freight = ReadConfig().get_http('baseurl') + '/ms-order/order-put/order/put/freight'

# 线下付款
url_orders_save_pay = ReadConfig().get_http('baseurl_admin2') + '/biz/orders/savepay'

# 微信支付预下单
url_pay_to_pay = ReadConfig().get_http('baseurl') + '/ms-order/pay/topay'

# 计价接口
url_put_price = ReadConfig().get_http('baseurl') + '/ms-order/order-put/order/put/price'

# 获取sku信息
url_index_sku = ReadConfig().get_http('baseurl') + '/ms-goods/product/index/sku/'

# 获取优惠券列表
url_coupon_self_list = ReadConfig().get_http('baseurl') + '/ms-promotion/coupon-detail/self/list'

# 延长收货
url_order_delay = ReadConfig().get_http('baseurl') + '/ms-order/order/delivery/delay/'

# 确认收货
url_order_take = ReadConfig().get_http('baseurl') + '/ms-order/order/delivery/take/'

# 佣金信息-APP
url_commission_app = ReadConfig().get_http('baseurl') + '/ms-member/personal/promotion/commission/app'

# 获取账号配置信息
url_account_info = ReadConfig().get_http('baseurl') + '/ms-sys/sysaccount/info/CD100'

# 获取税率
url_get_TAX = ReadConfig().get_http('baseurl') + '/ms-sys/oracledict/get/TAXType/TAXType'

# 获取提现方式
url_config_cash = ReadConfig().get_http('baseurl') + '/ms-member/memberbankcard/config/cash'

# 微信提现
url_cash_deduction = ReadConfig().get_http('baseurl') + '/ms-member/customer-request/deduction/tax?amount='

# 银行卡对应银行
url_bank_meta = ReadConfig().get_http('baseurl') + '/ms-member/memberbankcard/bankmeta/'

# 银行卡认证
url_bank_sign = ReadConfig().get_http('baseurl') + '/ms-member/memberbankcard/sign'

# 用户的银行卡
url_use_bank = ReadConfig().get_http('baseurl') + '/ms-member/memberbankcard/usebank'

# 发送短信
url_send_sms = ReadConfig().get_http('baseurl') + '/ms-message/captcha/index/sendsms'

# 提现
url_apply_check_code = ReadConfig().get_http('baseurl') + '/ms-member/customer-request/apply/checkcode'

'''后台admin1'''

# 后台登录接口
url_login_admin = ReadConfig().get_http('baseurl_admin') + '/login'

# 申请联盟奖励前，查询会员信息
url_get_customer = ReadConfig().get_http('baseurl_admin') + '/biz/customer/getCustomer?conNo='

# 联盟奖励申请
url_award_save = ReadConfig().get_http('baseurl_admin') + '/biz/awardqtrank/save'

'''后台接口admin2'''
# 后台登录接口
url_login_admin2 = ReadConfig().get_http('baseurl_admin2') + '/auth/login'

# 新增品牌
url_brand_save = ReadConfig().get_http('baseurl_admin2') + '/biz/brand/save'

# 删除品牌
url_brand_delete = ReadConfig().get_http('baseurl_admin2') + '/biz/brand/delete/'

# 新增运费模板
url_template_insert = ReadConfig().get_http('baseurl_admin2') + '/biz/template/insert'

# 新增商品
url_product_save = ReadConfig().get_http('baseurl_admin2') + '/biz/product/save'

# 商品配置显示
url_share_update = ReadConfig().get_http('baseurl_admin2') + '/biz/sharedoc/updateconfigure/'

# 商品的删除
url_remove = ReadConfig().get_http('baseurl_admin2') + '/biz/product/remove/'

# 商品上架
url_product_shelve = ReadConfig().get_http('baseurl_admin2') + '/biz/product/shelve/'

#  新增优惠券
url_coupon_insert = ReadConfig().get_http('baseurl_admin2') + '/coupon/insert'

# 上架优惠券
url_resource_user = ReadConfig().get_http('baseurl_admin2') + '/coupon/updatestatus/'

# 导入优惠券
url_coupon_add = ReadConfig().get_http('baseurl_admin2') + '/coupon/grantcoupon/'

# 新增SKU商品
url_product_save_sku = ReadConfig().get_http('baseurl_admin2') + '/biz/product/saveproductsku'

# 打印订单
url_oder_print = ReadConfig().get_http('baseurl_admin2') + '/biz/orders/savedispa/'

# 订单发货
url_order_send = ReadConfig().get_http('baseurl_admin2') + '/biz/orders/savesend'

# 佣金重算
url_performance_recalculation = ReadConfig().get_http('baseurl_admin2') + '/biz/performance/recalculate/'
