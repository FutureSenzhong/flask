from flask import Flask, request


app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name', 'Flask')  # 获取查询参数name的值
    return '<h1>Hello, %s!<h1>' % name


# 钩子函数
@app.before_request
def do_something():
    pass


if __name__ == '__main__':
    app.run()
