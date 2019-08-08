from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'dasdfjikkjhkjhkj'


@app.route('/')
def hello():
    return '</h1>hello world</h1>'


# 绑定多个路由
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


if __name__ == '__main__':
    app.run()
