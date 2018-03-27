from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField, SubmitField, DateField, IntegerField, FloatField


class ToneForm(FlaskForm):
    dic_code = IntegerField("体检项目编码")
    summary = StringField("体检项对应的健康状态描述")
    val = IntegerField("权重")
    lower_scope = FloatField("范围下限")
    upper_scope = FloatField("范围上限")
    submit = SubmitField("更新")
