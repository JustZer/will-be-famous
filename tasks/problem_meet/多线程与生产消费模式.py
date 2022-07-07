# -*- coding: utf-8 -*-
# @Time : 2022/6/7 15:41
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:
import json
import queue
import threading
import time
import traceback

from elasticsearch import Elasticsearch
from peewee import *

from ecomm_uniprocess_center.db.fn.conn.mysql_db import ShopifyDropshipBaseModel
from ecomm_uniprocess_center.db.fn.conn.redis_db import RedisPool

red_conn = RedisPool().get_redis_conn()


class ShopifyProductInfo(ShopifyDropshipBaseModel):
    aliexpress_relation_list = CharField(constraints=[SQL("DEFAULT ''")])
    competition = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = IntegerField()
    images = CharField(constraints=[SQL("DEFAULT ''")])
    inventory_detail = CharField(constraints=[SQL("DEFAULT ''")])
    two_week_inventory_change = IntegerField(constraints=[SQL("DEFAULT 0")])
    two_week_inventory_growth = IntegerField(constraints=[SQL("DEFAULT 0")])
    have_inventory_flag = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    max_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    max_profit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    min_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    min_profit = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    product_img_hash = CharField(constraints=[SQL("DEFAULT ''")])
    product_url = CharField(constraints=[SQL("DEFAULT ''")])
    product_url_md5 = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    published_time = DateTimeField(constraints=[SQL("DEFAULT 1970-01-01 08:00:01")])
    review_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    store_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    store_rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    tags = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    categories = CharField(null=True)
    two_week_growth = IntegerField(null=True)
    two_week_order_count = IntegerField(null=True)
    ad_count = IntegerField(null=True)
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    like_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    comment_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    week_order_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    week_revenue = IntegerField(constraints=[SQL("DEFAULT 0")])
    week_revenue_growth = IntegerField(constraints=[SQL("DEFAULT 0")])
    month_order_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    month_revenue = IntegerField(constraints=[SQL("DEFAULT 0")])
    shopify_compete_list = CharField(constraints=[SQL("DEFAULT ''")])
    order_detail = CharField(constraints=[SQL("DEFAULT ''")])
    revenue_detail = CharField(constraints=[SQL("DEFAULT ''")])
    price_detail = CharField(constraints=[SQL("DEFAULT ''")])
    week_avg_price_detail = CharField(constraints=[SQL("DEFAULT ''")])
    week_order_detail = CharField(constraints=[SQL("DEFAULT ''")])
    week_revenue_detail = CharField(constraints=[SQL("DEFAULT ''")])
    original_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    original_price_detail = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'shopify_product_info'
        indexes = (
            (('id', 'product_url_md5'), True),
        )
        primary_key = CompositeKey('id', 'product_url_md5')


def query_body(search_after):
    body = {
        "_source": ["_id"],
        "sort": [
            {
                "seven_days_revenue": {
                    "order": "desc"
                }
            }
        ],
        "size": 500,
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "seven_days_order": {
                                "gte": 1
                            }
                        }
                    },
                    {
                        "term": {
                            "is_deleted": {
                                "value": "0"
                            }
                        }
                    }
                ]
            }
        }
    }
    if search_after:
        body.update({"search_after": search_after, })
    return body


FN_USERNAME = 'elastic'
FN_PASSWORD = 'ES@common_us0619'
FN_INNER_DOMAIN = 'es-cn-6ja1pcr6x000nzc15.elasticsearch.aliyuncs.com:9200'


def fn_elastic():
    return Elasticsearch('{}:{}@{}'.format(FN_USERNAME, FN_PASSWORD, FN_INNER_DOMAIN))


def fix_detail(detail):
    detail = json.loads(detail)
    avg_value = round(sum(detail.values()) / len(detail.items()))
    last_a = None
    for p in detail.keys():
        if detail[p] > avg_value and last_a:
            detail[p] = last_a
        if detail[p] == 0 or last_a == 0:
            detail[p] = list(detail.values())[0]
        last_a = detail[p]
    return json.dumps(detail)


class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue
        self.fn_elastic = fn_elastic()
        self.index_name = "fn_shopify_product_info"

    def run(self):
        search_after = None
        while True:
            body = query_body(search_after)
            try:
                res = self.fn_elastic.search(body=body, index=self.index_name)
            except Exception:
                print("ES 查询失败,休息5秒吧")
                # print(traceback.print_exc())
                time.sleep(5)
                continue
            hits = res['hits']['hits']
            if not hits:
                self.queue.put("__break__")
                print(f"生产者 {self.name} 已完成使命,拜拜")
                break
            search_after = hits[-1]['sort']
            for hit in hits:
                _id = hit["_id"]
                self.queue.put(_id)


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue
        self.count = 0

    def run(self) -> None:
        while True:
            if not self.queue.empty():
                print("队列消费完毕,休息一秒吧")
                time.sleep(1)
                continue
            value = self.queue.get()
            if value == '__break__':
                self.queue.put("__break__")
                print(f"消费者 {self.name} 已完成使命,拜拜")
                break
            try:
                row = ShopifyProductInfo.select(ShopifyProductInfo.id,
                                                ShopifyProductInfo.product_url_md5,
                                                ShopifyProductInfo.price_detail,
                                                ShopifyProductInfo.original_price_detail
                                                ).where(ShopifyProductInfo.id == value).get()
                if row.price_detail and row.original_price_detail:
                    row.price_detail = fix_detail(row.price_detail)
                    row.original_price_detail = fix_detail(row.original_price_detail)
                    row.save()
                red_conn.lpush('shopify_order_recount_solo', row.id)
                self.count += 1
                print(f"消费者 {self.name} 已处理 {self.count} 条数据")
            except Exception:
                print("查询数据库报错,保存原因如下...")
                print(traceback.print_exc())
                time.sleep(1)


if __name__ == '__main__':
    q = queue.Queue(maxsize=1000)
    p = Producer("1号", q)
    p.start()
    p.join()
    tt = []
    for i in range(3):
        c = Consumer(str(i), q)
        tt.append(c)
        c.start()
    for t in tt:
        t.join()
