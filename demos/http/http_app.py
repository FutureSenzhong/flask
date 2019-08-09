from flask import Flask, request, redirect, url_for, abort, make_response

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




































if __name__ == '__main__':
    app.run()
