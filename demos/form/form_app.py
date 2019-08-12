import os

from flask import Flask, request, redirect, url_for, abort, make_response, session, g, render_template, flash

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






































if __name__ == '__main__':
    app.run()
