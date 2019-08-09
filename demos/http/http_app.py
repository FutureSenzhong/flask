import os

from flask import Flask, request, redirect, url_for, abort, make_response, session, g

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dasdadadsasd')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    response = '<h1>Hello, %s!</h1>' % name
    # 根据用户认证状态返回不同的内容
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response


# 钩子函数
@app.before_request
def do_something():
    pass


# 重定向
@app.route('/')
def redirects():
    return redirect(url_for('hello'))


# 错误处理
@app.route('/404')
def not_found():
    abort(404)


# 指定数据的MIME类型
@app.route('/foo')
def foo():
    response = make_response({
        "note": {

            "to": "Peter",
            "from": "Jane",
            "heading": "Remider",
            "body": "Don't forget the party!"
            }
        }
    )

    response.mimetype = 'application/json'
    return response


# 给浏览器设置cookie
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


# 使用session模拟用户的认证功能
@app.route('/login')
def login():
    session['logged_in'] = True  # 写入
    return redirect(url_for('hello'))


# 管理页面查看是否用户已经登陆
@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page.'


# 登出用户
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello'))


# 上下文全局变量
@app.before_request
def get_name():
    g.name = request.args.get('name')


if __name__ == '__main__':
    app.run()
