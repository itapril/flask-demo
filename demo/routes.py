# -*- coding: utf-8 -*-
from demo import app
from flask.ext.restful import Api
from demo.controller.login_controller import Login
from demo.controller.demo_controller import Demo,DemoById


api = Api(app, default_mediatype='application/json')
api.add_resource(Login, '/login')

api.add_resource(Demo, '/demo')
api.add_resource(DemoById, '/demo/<int:demo_id>')


