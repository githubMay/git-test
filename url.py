#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""
from handlers.index import IndexHandler
import sys     #utf-8，兼容汉字
from imp import reload
reload(sys)


from handlers.index import IndexHandler    #假设已经有了

url = [
    (r'/', IndexHandler),
]
