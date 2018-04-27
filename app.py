#-*- coding:utf-8 -*-
import os
from flask import Flask, jsonify
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)


tasks = [
    {
        'id': 1,
        'title': u'买卖二手车',
        'description': u'Make In China',
        'done': True
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


class TaskAPI(Resource):
    def get(self):
        return jsonify({'tasks': tasks})


class ApiTest(Resource):
    def get(self):
        return jsonify({'tasks': tasks})


api.add_resource(TaskAPI,  '/todo/api/v1.0/tasks')
api.add_resource(ApiTest,  '/todo/api/v2')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
