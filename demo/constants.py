# coding=utf-8
import os

DEBUG = (os.environ.get('ENV', 'dev') == 'dev')

# 生产环境 和 个人开发环境加载真实常量的值
# if os.environ.get('ENV', '') in ('production', 'dev'):
#     from webspider.security_constants import *