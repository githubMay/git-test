#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
print('the index.py began!!!')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        print('the index.post began!!!')
        username = self.get_argument("username")
        password = self.get_argument("password")
        print(username)
        print(password)

        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        print('get user_infos!!!')
        print(type(user_infos))
        print(user_infos)
        if user_infos:
            db_pwd = user_infos[0][1]
            print('getting db_pwd success!!!')

            if db_pwd == password:
                print('determining success!!!')
                self.write("welcome you: " + username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no this user.")