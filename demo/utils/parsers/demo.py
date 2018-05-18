from flask.ext.restful import reqparse

demo_post_parser = reqparse.RequestParser()
demo_post_parser.add_argument(
    'id', dest='id',
    type=int, location='form',
    required=False, help='The demo id',
)

demo_post_parser.add_argument(
    'name', dest='name',
    type=str, location='json',
    required=True, help='The demo name',
)