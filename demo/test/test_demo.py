# -*- coding: utf-8 -*-

from demo.model.demo import DemoModel


def get_demo_list():
    demos = DemoModel.list()
    return {city.name: city.id for city in demos}


def test_add():
    add_data_dict = dict(
        name='laoA'
    )
    print(add_data_dict)
    demo_id = DemoModel.add(**add_data_dict)
    demo = DemoModel.get_by_pk(demo_id)
    print(demo)



print(get_demo_list())
# print(test_add())
print(get_demo_list())
print(get_demo_list())
