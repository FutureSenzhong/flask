import os

from flask import Flask, request, redirect, url_for, abort, make_response, session, g, render_template, flash, \
    get_flashed_messages

from demos.form.forms import LoginForm

app = Flask(__name__, template_folder='./templates')
app.secret_key = os.getenv('SECRET_KEY', 'dasdadadsasd')
app.config["DEBUG"] = True


# 删除Jinja2语句后的第一个空行
app.jinja_env.trim_blocks = True
# 删除Jinja2语句所在行之前的空格和制表符（tabs）
app.jinja_env.lstrip_blocks = True


@app.route('/')
def index():
    # 访问跟目录默认重定向到watchlist来显示数据
    return render_template('form.html')


@app.route('/hello')
def hello():
    # 访问跟目录默认重定向到watchlist来显示数据
    message = get_flashed_messages()
    return 'hello, 有一个消息%s' % message


# 使用Flask-WTF处理表单
# Flask-WTF默认为每个表单启用CSRF保护，它会为我们自动生成和
# 验证CSRF令牌。默认情况下，Flask-WTF使用程序密钥来对CSRF令牌
# 进行签名，所以我们需要为程序设置密钥：
# app.secret_key = 'secret string'


# 验证表单数据
# 客服端验证，可以实时提示用户
# 服务端验证，无论是否客户端是否验证，都应该进行校验，保证数据的完整性
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        print(username)
        flash('Welcome home, %s!' % username)
        return redirect(url_for('hello'))
    flash('输入有误，请重新输入！！！')
    return render_template('login.html', form=login_form, )




























if __name__ == '__main__':
    app.run()
