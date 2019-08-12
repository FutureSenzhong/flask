from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


# 如果你想手动编写HTML表单的代码，要注意表单字段的name属性
# 值必须和表单类的字段名称相同，这样在提交表单时WTForms才能正确
# 地获取数据并进行验证
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me', default=True)
    submit = SubmitField('Log in')