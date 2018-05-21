# -*- coding: utf-8 -*-
from demo.model.base import BaseModel

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TIMESTAMP
import uuid


class DemoModel(BaseModel):
    __tablename__ = 'demo'

    # id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    id = Column(VARCHAR(64), primary_key=True, nullable=False, default=uuid.uuid4())
    name = Column(VARCHAR(64), nullable=False, doc=u'名称')
    desc = Column(VARCHAR(128), nullable=False, doc=u'备注说明')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now, doc=u'创建时间')
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, doc=u'更新时间')

    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name,
            'desc': self.desc
        }
        return json


