# coding:utf-8
import redis

class Config(object):
    """工程的配置信息"""
    SECRET_KEY = "qwertyuiopasdfghjklzxcvbnm"

    #数据库的配置信息　mysql
    SQLALCHEMY_DATABASE_URI ="mysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    #flask_session的配置信息
    SESSION_TYPE = "redis" #指明保存到redis中
    SESSION_USE_SIGNER = True #让cookie中的sesssion_id被加密处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)#使用redisde的实例
    PERMANENT_SESSION_LIFETIME =86400 #session的过期时间秒


class DevelopmentConfig(Config):
    """开发模式使用的配置信息"""
    DEBUG = True
    # 支付宝
    ALIPAY_APPID = "2016091900546337"
    ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"


class ProductionConfig(Config):
    """生产模式的配置信息，线上模式"""
    pass



config_dict ={
    "develop":DevelopmentConfig,
    "product":ProductionConfig


}
