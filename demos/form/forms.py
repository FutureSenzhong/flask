from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError


# 如果你想手动编写HTML表单的代码，要注意表单字段的name属性
# 值必须和表单类的字段名称相同，这样在提交表单时WTForms才能正确
# 地获取数据并进行验证
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me', default=True)
    submit = SubmitField('Log in')


# 设置内置错误消息语言为中文
class MyBaseForm(FlaskForm):
    class Meta:
        locales = ['zh']


class HelloForm(MyBaseForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField()


# 自定义验证器（行内验证器）
class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number')
    submit = SubmitField()

    @classmethod
    def validate_answer(cls, field):
        if field.data != 42:
            raise ValidationError('Must be 42.')
