from flask import Flask, request, redirect, url_for, abort

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name', 'Flask')  # 获取查询参数name的值
    return '<h1>Hello, %s!<h1>' % name


# 钩子函数
@app.before_request
def do_something():
    pass


# 重定向
@app.route('/')
def redirect():
    return redirect(url_for('hello'))


# 错误处理
@app.route('/404')
def not_found():
    abort(404)


if __name__ == '__main__':
    app.run()
