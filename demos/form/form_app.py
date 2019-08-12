import os

from flask import Flask, request, redirect, url_for, abort, make_response, session, g, render_template, flash

from demos.form.forms import LoginForm

app = Flask(__name__, template_folder='./templates')
app.secret_key = os.getenv('SECRET_KEY', 'dasdadadsasd')


# 删除Jinja2语句后的第一个空行
app.jinja_env.trim_blocks = True
# 删除Jinja2语句所在行之前的空格和制表符（tabs）
app.jinja_env.lstrip_blocks = True


@app.route('/')
def index():
    # 访问跟目录默认重定向到watchlist来显示数据
    return render_template('form.html')


# 使用Flask-WTF处理表单
# Flask-WTF默认为每个表单启用CSRF保护，它会为我们自动生成和
# 验证CSRF令牌。默认情况下，Flask-WTF使用程序密钥来对CSRF令牌
# 进行签名，所以我们需要为程序设置密钥：
# app.secret_key = 'secret string'

@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', login_form=login_form)



































if __name__ == '__main__':
    app.run()
