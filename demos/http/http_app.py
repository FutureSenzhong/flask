from flask import Flask, request


app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get('name', 'Flask')  # 获取查询参数name的值
    return '<h1>Hello, %s!<h1>' % name


if __name__ == '__main__':
    app.run()
