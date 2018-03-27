from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField, SubmitField, DateField, IntegerField, FloatField, SelectField
from ..models import TblDictTone


class DictCmpConductForm(FlaskForm):
    dic_code = IntegerField("体检项目编码")
    tone_id = SelectField("针对的体检项目及其级别", coerce=int)
    suggest = StringField("建议")
    risk = StringField("风险分析")
    submit = SubmitField("更新")

    def __init__(self, *args, **kwargs):
        super(DictCmpConductForm, self).__init__(*args, **kwargs)
        self.tone_id.choices = [(tone.tone_id, tone.summary)
                                for tone in
                                TblDictTone.query.order_by(TblDictTone.tone_id).all()]
