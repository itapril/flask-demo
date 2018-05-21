# -*- coding: utf-8 -*-
from flask.ext.restful import fields

demo_simple_fislds = {
    'id': fields.String,
    'created_at': fields.DateTime,
    'updateed_at': fields.DateTime
}