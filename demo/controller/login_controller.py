# -*- coding: utf-8 -*-
from flask.ext.restful import Resource


class Login(Resource):
    def get(self):
        return {"msg": "这是登录的GET方法"}, 200