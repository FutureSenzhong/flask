import os
import uuid

from flask import Flask, request, redirect, url_for, abort, make_response, session, g, render_template, flash, \
    get_flashed_messages, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError

from demos.form.forms import LoginForm, UploadForm, MultiUploadForm, RichTextForm, NewPostForm

app = Flask(__name__, template_folder='./templates')

app.secret_key = os.getenv('SECRET_KEY', 'dasdadadsasd')
app.config["DEBUG"] = True

# 配置数据连接
# SQLite的数据库URI在Linux或macOS系统下的斜线数量是4个；在
# Windows系统下的URI中的斜线数量为3个。内存型数据库的斜线固定为3
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))
# 关闭数据库警告信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 初始化数据库连接对象
db = SQLAlchemy(app)


# 定义一个数据模型
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)


# 创建数据库方法
def create_database():
    db.create_all()
    return True


























if __name__ == '__main__':
    create_database()
    app.run()

