from flask.ext.restful import Resource
from demo.utils.parsers.demo import demo_post_parser
# from demo.model.demo import DemoModel


class Demo(Resource):
    def post(self):
        demo = demo_post_parser.parse_args()
        print(demo)
        return {"msg": "这是登录的GET方法"}, 200