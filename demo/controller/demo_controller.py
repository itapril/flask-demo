from flask.ext.restful import Resource, abort, marshal_with
from demo.utils.parsers.demo import demo_post_parser,demo_id_parser
from demo.handler.demo import create_demo, list_demo
# from demo.model.demo import DemoModel


class Demo(Resource):


    """
    GET : http://localhost:3001/demo?id=123&name=ishdfh
    不需要指定Headers
    """
    # @marshal_with()
    def get(self):
        demo_parser = demo_post_parser.parse_args()
        print(demo_parser)
        return list_demo(demo_parser.name, demo_parser.desc)

    """
    POST:http://localhost:3001/demo
    需要指定Headers
    Content-Type:application/json
    """
    def post(self):
        demo_parser = demo_post_parser.parse_args()
        result = create_demo(demo_parser.name, demo_parser.desc)
        print(result)
        print(demo_parser)

        return {"msg": "这是登录的GET方法"}, 200


class DemoById(Resource):

    """
    GET: http://localhost:3001/demo/123
    """
    def get(self, demo_id):

        print(demo_id)
        abort(403, messages="twest", test="test")

    def delete(self, demo_id):
        print(demo_id)

    def put(self, demo_id):
        print(demo_id)
        demo = demo_id_parser.parse_args()
        print(demo)