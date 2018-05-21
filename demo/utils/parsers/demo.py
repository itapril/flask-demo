# -*- coding: utf-8 -*-
from flask.ext.restful import reqparse

demo_post_parser = reqparse.RequestParser()
# demo_post_parser.add_argument(
#     'id', dest='id',
#     type=int, location=['json', 'args'],
#     required=False, help='The demo id',
# )

demo_post_parser.add_argument(
    'name', dest='name',
    type=str, location=['json', 'args'],
    required=False, help='The demo name',
)

demo_post_parser.add_argument(
    'desc', dest='desc',
    type=str, location=['json', 'args'],
    required=False, help='The demo desc',
)

demo_id_parser = reqparse.RequestParser()
demo_id_parser.add_argument(
    'name', dest='name',
    type=str, location=['json', 'args'],
    required=False, help='The demo name',
)