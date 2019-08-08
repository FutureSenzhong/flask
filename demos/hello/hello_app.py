from flask import Flask

import config

app = Flask(__name__)

# 配置文件引入的几种方式
# app.config.from_object(config.config['development'])  # 获取相应的配置类


@app.route('/')
def hello():
    return '</h1>hello world</h1>'


# 绑定多个路由
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# 动态URl给视图函数传递参数
# 设置默认参数
@app.route('/greet', defaults={'name': 'Flask'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
