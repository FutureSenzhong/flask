import os


from flask_mail import Message, Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

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


# SSL/TLS加密：
# MAIL_USE_SSL = True
# MAIL_PORT = 465


# STARTTLS加密
# MAIL_USE_TLS = True
# MAIL_PORT = 587

# 邮件配置
app.config.update(
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=('SZ', os.getenv('MAIL_USERNAME')),
    )
# 初始化数据库连接对象
db = SQLAlchemy(app)
# 初始化邮件对象
mail = Mail(app)

# 实例化数据库迁移
migrate = Migrate(app, db)  # 在db对象创建后调用


@app.route('/')
def send_mail():
    message = Message(subject='Hello, World!',
                      recipients=['1019217919@qq.com>'],
                      body='Across the Great Wall we can reach every corner in the world.')

    mail.send(message)
    return '发送成功', True


# 异步发送邮件
# 因为Flask-Mail的send（）方法内部的调用逻辑中使用了current_app
# 变量，而这个变量只在激活的程序上下文中才存在，这里在后台线程调
# 用发信函数，但是后台线程并没有程序上下文存在。为了正常实现发信
# 功能，我们传入程序实例app作为参数，并调用app.app_context（）手动
# 激活程序上下文

# say hello flask over ！






















if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)


