# -*- coding: utf-8 -*-
# @Time : 2022/8/24 14:38
# @Author : Zhangzixu
# @Software: PyCharm
# @Description:
import datetime

from peewee import *

database = MySQLDatabase(host="127.0.0.11", user="zf_dml", password="ArripjXAHHyM5Ah1", port=1424, database='dropship')
# cur = database.cursor()
# cur.execute("""SELECT `t1`.`id`, `t1`.`address`, `t1`.`address_created`, `t1`.`address_updated`, `t1`.`alexa_rating`, `t1`.`alexa_week_change`, `t1`.`alexa_month_change`, `t1`.`alexa_history`, `t1`.`page_id`, `t1`.`page_like`, `t1`.`recent_ads_countries`, `t1`.`recent_month_ads_count`, `t1`.`recent_ads_count`, `t1`.`ad_info`, `t1`.`available_status`, `t1`.`bk_int1`, `t1`.`category`, `t1`.`country`, `t1`.`created_at`, `t1`.`currency`, `t1`.`description`, `t1`.`email`, `t1`.`keywords`, `t1`.`last_crawl_day`, `t1`.`meta_info`, `t1`.`priority`, `t1`.`social_link`, `t1`.`title`, `t1`.`update_status`, `t1`.`is_top_shopify`, `t1`.`updated_at`, `t1`.`shop_id`, `t1`.`address_list`, `t1`.`shop_logo`, `t1`.`product_categories`, `t1`.`product_num`, `t1`.`revenue`, `t1`.`traffic`, `t1`.`advertise_count`, `t1`.`advertise_week_num`, `t1`.`advertise_month_num`, `t1`.`advertise_week_change`, `t1`.`advertise_month_change`, `t1`.`ins_account`, `t1`.`ins_followers`, `t1`.`is_login`, `t1`.`month_order_num` FROM `shopify_store` AS `t1` WHERE (`t1`.`id` = 6277392);""")
# print(cur.fetchall())

class ShopifyDropshipBaseModel(Model):

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(ShopifyDropshipBaseModel, self).save(*args, **kwargs)

    class Meta:
        database = database


class ShopifyStore(ShopifyDropshipBaseModel):
    address = CharField(null=True, unique=True)
    address_created = DateTimeField(null=True)
    address_updated = DateTimeField(null=True)
    alexa_rating = IntegerField(null=True)
    alexa_week_change = IntegerField(null=True)
    alexa_month_change = IntegerField(null=True)
    alexa_history = CharField(null=True)
    page_id = CharField(null=True)
    page_like = IntegerField(null=True)
    recent_ads_countries = CharField(null=True)
    recent_month_ads_count = IntegerField(null=True)
    recent_ads_count = CharField(null=True)
    ad_info = CharField(null=True)
    available_status = IntegerField(index=True, null=True)
    bk_int1 = IntegerField(null=True)
    category = CharField(null=True)
    country = CharField(null=True)
    created_at = DateTimeField(null=True)
    currency = CharField(null=True)
    description = CharField(null=True)
    email = CharField(null=True)
    keywords = CharField(null=True)
    last_crawl_day = IntegerField(index=True, null=True)
    meta_info = CharField(null=True)
    priority = IntegerField(null=True)
    social_link = CharField(null=True)
    title = CharField(null=True)
    update_status = IntegerField(index=True, null=True)
    is_top_shopify = IntegerField(null=True)
    updated_at = DateTimeField(null=True)
    shop_id = CharField(index=True, null=True)
    address_list = CharField(null=True)
    shop_logo = CharField(null=True)
    product_categories = CharField(null=True)
    product_num = IntegerField(null=True)
    revenue = IntegerField(null=True)
    traffic = IntegerField(null=True)
    advertise_count = IntegerField(null=True)
    advertise_week_num = IntegerField(null=True)
    advertise_month_num = IntegerField(null=True)
    advertise_week_change = IntegerField(null=True)
    advertise_month_change = IntegerField(null=True)
    ins_account = CharField(null=True)
    ins_followers = IntegerField(null=True)
    is_login = IntegerField(null=True)
    month_order_num = IntegerField(null=True)

    class Meta:
        table_name = 'shopify_store'


# print("1231231")
# print(ShopifyStore.select().where(ShopifyStore.id == 6277392))

import pymysql
conn = pymysql.connect(host="127.0.0.11", user="zf_readonly", password="2zKQy3jSRwddZVHy", port=1424, database='dropship')
print(conn.ping())
cur = conn.cursor()

cur.execute("""SELECT `t1`.`id`, `t1`.`address`, `t1`.`address_created`, `t1`.`address_updated`, `t1`.`alexa_rating`, `t1`.`alexa_week_change`, `t1`.`alexa_month_change`, `t1`.`alexa_history`, `t1`.`page_id`, `t1`.`page_like`, `t1`.`recent_ads_countries`, `t1`.`recent_month_ads_count`, `t1`.`recent_ads_count`, `t1`.`ad_info`, `t1`.`available_status`, `t1`.`bk_int1`, `t1`.`category`, `t1`.`country`, `t1`.`created_at`, `t1`.`currency`, `t1`.`description`, `t1`.`email`, `t1`.`keywords`, `t1`.`last_crawl_day`, `t1`.`meta_info`, `t1`.`priority`, `t1`.`social_link`, `t1`.`title`, `t1`.`update_status`, `t1`.`is_top_shopify`, `t1`.`updated_at`, `t1`.`shop_id`, `t1`.`address_list`, `t1`.`shop_logo`, `t1`.`product_categories`, `t1`.`product_num`, `t1`.`revenue`, `t1`.`traffic`, `t1`.`advertise_count`, `t1`.`advertise_week_num`, `t1`.`advertise_month_num`, `t1`.`advertise_week_change`, `t1`.`advertise_month_change`, `t1`.`ins_account`, `t1`.`ins_followers`, `t1`.`is_login`, `t1`.`month_order_num` FROM `shopify_store` AS `t1` WHERE (`t1`.`id` = 6277392);""")
print(cur.fetchall())
