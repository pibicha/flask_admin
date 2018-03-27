from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField, SubmitField, DateField, IntegerField, FloatField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..models import TblDictTone
from .. import photos


class DictCmpAccordForm(FlaskForm):
    dic_code = IntegerField("体检项目编码")
    ahead_tone = SelectField("相对过去的健康状态", coerce=int)
    behead_tone = SelectField("相对现在的健康状态", coerce=int)
    trend_advise = StringField("对比过去和现在的健康趋势，对应的建议")
    img = FileField('图片上传', validators=[
        FileAllowed(photos, '只能上传图片！'),
        FileRequired('文件未选择！')
    ])

    def __init__(self, *args, **kwargs):
        super(DictCmpAccordForm, self).__init__(*args, **kwargs)
        self.ahead_tone.choices = [(tone.val, str(tone.dic_code) + " :" + tone.summary)
                                   for tone in
                                   TblDictTone.query.order_by(TblDictTone.tone_id).all()]
        self.behead_tone.choices = [(tone.val, str(tone.dic_code) + " :" + tone.summary)
                                    for tone in
                                    TblDictTone.query.order_by(TblDictTone.tone_id).all()]

    submit = SubmitField("更新")
