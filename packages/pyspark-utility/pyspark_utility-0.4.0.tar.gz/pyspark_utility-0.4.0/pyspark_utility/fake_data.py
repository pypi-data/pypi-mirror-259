from fakers.providers.person import Person
from fakers.providers.retail import Retail
from pyspark.sql import SparkSession, DataFrame


class FakeData:
    @staticmethod
    def fake_person(locale='en_US'): return Person.fake_person(locale)

    @staticmethod
    def fake_persons(spark: SparkSession, rec_cnt=5, locale='en_US') -> DataFrame:
        return Person.fake_persons(rec_cnt, locale).to_spark(spark)

    @staticmethod
    def fake_address(locale='en_US'): return Person.fake_address(locale)

    @staticmethod
    def fake_addresses(spark: SparkSession, rec_cnt=5, locale='en_US') -> DataFrame:
        return Person.fake_addresses(rec_cnt, locale).to_spark(spark)

    @staticmethod
    def fake_order(locale='en_US'): return Retail.fake_order(locale)

    @staticmethod
    def fake_orders(spark: SparkSession, rec_cnt=5, locale='en_US') -> DataFrame:
        return Retail.fake_orders(rec_cnt, locale).to_spark(spark)

    @staticmethod
    def fake_product(locale='en_US'): return Retail.fake_product(locale)

    @staticmethod
    def fake_products(spark: SparkSession, rec_cnt=5, locale='en_US') -> DataFrame:
        return Retail.fake_products(rec_cnt, locale).to_spark(spark)

    @staticmethod
    def fake_user(locale='en_US'): return Retail.fake_user(locale)

    @staticmethod
    def fake_users(spark: SparkSession, rec_cnt=5, locale='en_US') -> DataFrame:
        return Retail.fake_users(rec_cnt, locale).to_spark(spark)

    @staticmethod
    def fake_sale(locale='en_US'): return Retail.fake_sale(locale)

    @staticmethod
    def fake_sales(spark: SparkSession, rec_cnt=5, locale='en_US') -> DataFrame:
        return Retail.fake_sales(rec_cnt, locale).to_spark(spark)
