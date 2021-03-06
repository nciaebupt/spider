#!/usr/bin/env python

import datetime
from sqlalchemy import Column, create_engine, Table, MetaData
from sqlalchemy.types import TIMESTAMP, Integer, String
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from config import *
class PageStore:
    def __init__(self):
        metadata = MetaData()
        engine = create_engine("mysql://%s:%s@%s/%s?charset=utf8&use_unicode=0" % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_DB))
        self.table_page = Table('page', metadata,
                          Column('id', Integer(), primary_key=True, nullable=False),
                          Column('url', String(MAX_URL_LENGTH)),
                          Column('html', MEDIUMTEXT),
                          Column('updatetime', TIMESTAMP, default=datetime.datetime.now()),
                          mysql_engine='MyISAM',
                          mysql_charset='utf8'
                          )
        self.table_failed = Table('failed', metadata,
                          Column('id', Integer(), primary_key=True, nullable=False),
                          Column('url', String(MAX_URL_LENGTH)),
                          Column('updatetime', TIMESTAMP, default=datetime.datetime.now()),
                          mysql_engine='MyISAM',
                          mysql_charset='utf8'
                          )
        metadata.create_all(engine)
        self.conn = engine.connect()
    def failed(self, url):
        self.conn.execute(self.table_failed.insert().values(url=url));
    def succeed(self, url, html):
        self.conn.execute(self.table_page.insert().values(url=url,
                                                    html=html));
        
        
