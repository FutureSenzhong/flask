import os
import uuid

from flask import Flask, request, redirect, url_for, abort,\
    make_response, session, g, render_template, flash, \
    get_flashed_messages, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import validate_csrf
from sqlalchemy import and_, or_
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired


app = Flask(__name__, template_folder='./templates')

app.secret_key = os.getenv('SECRET_KEY', 'dasdadadsasd')
app.config["DEBUG"] = False

# 配置数据连接
# SQLite的数据库URI在Linux或macOS系统下的斜线数量是4个；在
# Windows系统下的URI中的斜线数量为3个。内存型数据库的斜线固定为3
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))
# 关闭数据库警告信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 删除Jinja2语句后的第一个空行
app.jinja_env.trim_blocks = True
# 删除Jinja2语句所在行之前的空格和制表符（tabs）
app.jinja_env.lstrip_blocks = True
# 让Flask-WTF使用WTForms内置的错误消息翻译
app.config['WTF_I18N_ENABLED'] = False
# 设置请求报文的最大长度（设置文件上传的大小限制）
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024  # 限制为3M大小的文件
# 设置上传文件路劲
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
# 设置文件类型
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']


# 初始化数据库连接对象
db = SQLAlchemy(app)


# 定义一个数据模型
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    title = db.Column(db.String)

    def __repr__(self):
        return '<Note %r>' % self.body


# 创建数据库方法
def create_database():
    db.drop_all()
    db.create_all()

    return True


# 笔记对象表单
class NewNoteForm(FlaskForm):
    title = StringField('title')
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Save')


# 更新表单
class EditNoteForm(NewNoteForm):
    submit = SubmitField('Update')


# 笔记处理视图函数
@app.route('/new', methods=['GET', 'POST'])
def new_note():
    # 实例表单对象
    form = NewNoteForm()
    # 判断表单数据已通过验证并提交
    if form.validate_on_submit():
        # 获取网页数据
        body = form.body.data
        title = form.title.data
        # 添加到数据库
        notes = Note(title=title, body=body)
        db.session.add(notes)
        db.session.commit()
        flash('标题为“{}”笔记保存成功！'.format(title))
        # 重定向到主页,会发起一个GET请求
        return redirect(url_for('index'))
    return render_template('new_note.html', form=form)


@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    form = EditNoteForm()
    note = Note.query.get(note_id)
    if form.validate_on_submit():
        note.title = form.title.data
        note.body = form.body.data
        db.session.commit()
        flash('你的笔记“{}”更新成功.'.format(note.title))
        return redirect(url_for('index'))

    # 将存在在笔记内容显示在页面上
    form.body.data = note.body
    form.title.data = note.title
    return render_template('edit_note.html', form=form)


@app.route('/')
def index():
    form = NewNoteForm()
    per_page = int(request.args.get('per_page', 3))
    curr_page = int(request.args.get('page', 1))
    order_by = request.args.get('order_by', 'id')
    # table = db.session.query(Note)
    # totals = table.count()
    # notes = table.order_by(order_by).limit(per_page).offset(curr_page)
    pagination = Note.query.order_by(order_by).paginate(curr_page, per_page=per_page, error_out=False)
    notes = pagination.items
    return render_template('index.html', notes=notes, form=form, pagination=pagination)


# 我的照片墙
@app.route('/my_photo')
def my_photo():
    path = app.config['UPLOAD_PATH']
    files = os.listdir(path)
    return render_template('my-photo.html', files=files)


# 获取上传的文件
@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


# 获取文件名
def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.jpg':
            list_name.append(file_path)
    return list_name





# 关于我
@app.route('/about_me')
def about_me():
    return render_template('about-me.html')














if __name__ == '__main__':
    # 创建数据库
    # create_database()
    # 添加数据
    # note1 = Note(body='remember Sammy Jankis')
    # note2 = Note(body='SHAVE')
    # note3 = Note(body='DONT BELIEVE HIS LIES, HE IS THE ONE, KILL HIM')
    # db.session.add(note1)
    # db.session.add(note2)
    # db.session.add(note3)
    # db.session.commit()

    # # 查询方法
    # print(Note.query.all())
    # print(Note.query.first())
    # # 指定主键查询
    # print(Note.query.get(2))
    # # 查询数量
    # print(Note.query.count())
    # # 过滤查询
    # print(Note.query.filter(Note.body == 'SHAVE').first())
    # # 打印查询语句
    # print(Note.query.filter_by(body='SHAVE'))
    #
    # # 其他查询
    # print(Note.query.filter(Note.body.like('%foo%')))
    # # in查询
    # print(Note.query.filter(Note.body.in_(['foo', 'bar', 'baz'])))
    # # not in查询
    # print(Note.query.filter(~Note.body.in_(['foo', 'bar', 'baz'])))
    # # and查询
    # print(Note.query.filter(and_(Note.body == 'foo', Note.title == 'FooBar')))
    # print(Note.query.filter(Note.body == 'foo', Note.title == 'FooBar'))
    # print(Note.query.filter(Note.body == 'foo').filter(Note.title == 'FooBar'))
    # # or查询
    # print(Note.query.filter(or_(Note.body == 'foo', Note.body == 'bar')))
    #
    # # 更新操作，删除操作
    # # 直接为属性赋值提交即可更新，直接delete即可删除
    # note = Note.query.get(2)
    # # 更新
    # note.body = 'SHAVE LEFT THIGH'
    # db.session.commit()
    #
    # # 删除
    # db.session.delete(note)
    # db.session.commit()










    app.run(host='0.0.0.0')

