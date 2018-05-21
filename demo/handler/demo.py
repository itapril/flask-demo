from demo.model.demo import DemoModel
from flask import jsonify
from demo.handler.resp import base_resp


def create_demo(name, desc):
    demo_add_data = dict(
        name=name,
        desc=desc
    )
    demo = DemoModel.add(**demo_add_data)
    print(demo)
    return demo


def list_demo(name, desc):
    result = DemoModel.list()
    demos = []
    for r in result:
        temp = DemoModel.to_json(r)
        demos.append(temp)
    return base_resp("查询成功", demos)