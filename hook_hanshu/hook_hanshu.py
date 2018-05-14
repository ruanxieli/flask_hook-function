# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 下午4:09
# @Author  : Xieli Ruan
# @Site    : 
# @File    : hook_hanshu.py
# @Software: PyCharm

from flask import Flask, render_template, request, session,redirect,url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

@app.route('/')
def hello_world():
    return 'index'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username=='zhiliao' and password == '111111':
            session['username'] = 'zhiliao'
            return u'登陆成功'
        else:
            return u'用户名或密码错误！'
@app.route('/edit/')
def edit():
    if session.get('username'):
        return u'修改成功'
    else:
        return redirect(url_for('login'))

# before_request:在请求之前执行的
# before_request是在视图函数执行之前执行的
# before_request这个函数是一个装饰器，可以吧需要设置为钩子函数的代码放到视图函数执行之前执行

@app.before_request
def my_before_request():
    print 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
