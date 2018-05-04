# -*- coding: utf-8 -*-
from model.base import BaseModel

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TIMESTAMP


class DemoModel(BaseModel):
    __tablename__ = 'demo'

    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(64), nullable=False, doc=u'名称')
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now, doc=u'创建时间')
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now, doc=u'更新时间')