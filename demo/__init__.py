from flask import Flask

app = Flask(__name__)

#  路由添加
from demo.routes import api