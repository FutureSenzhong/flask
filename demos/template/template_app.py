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
    return redirect(url_for('watchlist'))


@app.route('/watchlist')
def watchlist():
    user = {
        'username': 'Grey Li',
        'bio': 'A boy who loves movies and music.',
    }
    movies = [
        {'name': 'My Neighbor Totoro', 'year': '1988'},
        {'name': 'Three Colours trilogy', 'year': '1993'},
        {'name': 'Forrest Gump', 'year': '1994'},
        {'name': 'Perfect Blue', 'year': '1997'},
        {'name': 'The Matrix', 'year': '1999'},
        {'name': 'Memento', 'year': '2000'},
        {'name': 'The Bucket list', 'year': '2007'},
        {'name': 'Black Swan', 'year': '2010'},
        {'name': 'Gone Girl', 'year': '2014'},
        {'name': 'CoCo', 'year': '2017'},
    ]
    return render_template('watchlist.html', user=user, movies=movies)


@app.template_global()
def bar():
    return 'I am global bar.'


# 在页面中加载网址静态资源
# 1.使用静态url
# 2.使用cdn加速连接引用
# 3.使用宏定义
# {% macro static_file(type, filename_or_url, local=True) %}
#     {% if local %}
#         {% set filename_or_url = url_for('static', filename=filename_or_url)
# %}
#     {% endif %}
#     {% if type == 'css' %}
#         <link rel="stylesheet" href="{{ filename_or_url }}" type="text/css">
#     {% elif type == 'js' %}
#         <script type="text/javascript" src="{{ filename_or_url }}"></script>
#     {% elif type == 'icon' %}
#         <link rel="icon" href="{{ filename_or_url }}">
#     {% endif %}
# {% endmacro %}

# 调用方式
# static_file('css', 'css/bootstrap.min.css')


# 页面消息闪现（出现后删除）
@app.route('/flash')
def just_flash():
    flash('通知！有一个消息请注意查看！！！')
    return redirect(url_for('index'))








































if __name__ == '__main__':
    app.run()
