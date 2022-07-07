#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def buy_item_one(sku_ids):
    asst.buy_item_in_stock(sku_ids=sku_ids, 
                           area=area, 
                           wait_all=False, 
                           stock_interval=5, 
                           submit_interval=4,
                           submit_retry=1)

def buy_item_by_threads(sku_ids):
    work_count = 3
    with ThreadPoolExecutor(work_count) as executor:
        for i in range(work_count):
            executor.submit(buy_item_one, sku_ids)

def buy_all_item_by_processes(sku_id_list):
    with ProcessPoolExecutor(len(sku_id_list)) as pool:
        return pool.map(buy_item_by_threads, sku_id_list)                  

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """
    # sku_ids = '4678974:1'
    sku_id_list = ['100015253061:1', # 商品id xt30II xc35f2 黑色
                   '100015253059:1', # 商品id xt30II xc35f2 银色
                   '100018462768:1', # 商品id xe4 27套机 黑色
                   '100010368315:1', # 商品id xe4 27套机 银色
                   #'100015253079:1', # 商品id xt30II 1545 黑色
                   #'100028021978:1', # 商品id xt30II 1545 银色
                   #'10026629841380:1', # 贝诚 xt30 27黑
                #    '10026629841378:1', # 贝诚 xt30 xc35
                   #'10051827525031:1', # 卓美 xe4 27银
                   #'58821756914:1', # 卓美 xe4 27黑
                   '44347081595:1', # 爱博深 xt30
                   '63110653435:1', # 爱博深 xt30
                #    '40879688610:1', # 爱博深 xe4+xc35
                #    '40879688611:1', # 爱博深 xe4+xc35
                   # '40879688606:1', # 爱博深 xe4+27
                   '10039177703433:1', # 尼美佳 xt30
                   '10053262481020:1', # 天睿xt30
                   '10054024093233:1', # 雄冠 xt30
                #    '30029112906:1', # 御城 xt30
                   '10054024093234:1', # 雄冠 xt30
                   '10054024093233:1', # 雄冠 xt30
                #    '30029099900:1', # yucheng xt 30
                #    '30029112906:1', # yucheng xt 30
                   '10042942500249:1', # lianxiang xt30
                   '10042942500239:1', # xt30
                   ]
    area = '1_72_4211'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    buy_all_item_by_processes(sku_id_list)
    # buy_item_one(sku_id_list[0])
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
