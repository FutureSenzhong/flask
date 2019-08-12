import os
import uuid

from flask import Flask, request, redirect, url_for, abort, make_response, session, g, render_template, flash, \
    get_flashed_messages, send_from_directory

from demos.form.forms import LoginForm, UploadForm

app = Flask(__name__, template_folder='./templates')
app.secret_key = os.getenv('SECRET_KEY', 'dasdadadsasd')
app.config["DEBUG"] = True


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


# 文件上传表单应用
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        # f.filename使用原文件名
        # werkzeug模块提供的secure_filename（f.filename）过滤所有危险字符
        # 统一重命名secure_filename('头像.jpg')
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        session['filenames'] = [filename]
        return redirect(url_for('show_images'))
    return render_template('upload.html', form=form)


# 随机生成文件名接受传入的文件名，返回随机文件名
def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


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


# 显示获取的图片
@app.route('/show_images')
def show_images():
    path = app.config['UPLOAD_PATH']
    files = os.listdir(path)

    return render_template('uploaded.html', files=files)



















if __name__ == '__main__':
    app.run()
