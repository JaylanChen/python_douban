# -*- coding: utf-8 -*-
import sqlite3
import os

class DbHelper():
    def init_db(self):
        conn = self.get_conn('./douban/data/movie.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE MovieType
            (Id INT PRIMARY KEY NOT NULL,
            Name NVARCHAR(32) NOT NULL,
            Url NVARCHAR(64));''')

        cur.execute('''CREATE TABLE Movie
            (Id INT PRIMARY KEY NOT NULL,
            Name NVARCHAR(64) NOT NULL,
            ShowDate DATE,
            Alias NVARCHAR(256),
            LeadingRole NVARCHAR(256),
            MovieType INT,
            Language NVARCHAR(32),
            Duration INT,
            Grade FLOAT,
            Introduction NVARCHAR(1024),
            Comments INT);''')

        print('Init Db Success')
        cur.close()
        conn.close()

    '''
    @summary: 获取连接
    '''
    def get_conn(self, path):
        conn = sqlite3.connect(path)
        if os.path.exists(path) and os.path.isfile(path):
            print('success')
            return conn
        else:
            conn = None
            print('memory')
            return sqlite3.connect(':memory:')

    '''
    @summary: 获取游标
    '''
    def get_cursor(self, conn):
        if conn is not None:
            return conn.cursor()
        else:
            return self.get_conn('').cursor()

    '''
    @summary: 执行sql
    '''
    def execute(self, conn, sql):
        if sql is not None and sql != '':
            cur = self.get_cursor(conn)
            cur.execute(sql)
            conn.commit()
            print('Success!')
            self.close_all(conn, cur)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def close_all(self, conn, cur):
        try:
            if cur is not None:
                cur.close()
                conn.close()
        finally:
            if cur is not None:
                cur.close()
                conn.close()
