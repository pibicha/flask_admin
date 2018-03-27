from flask import render_template, redirect, url_for
from . import dict_cmp_conduct
from ..models import TblDictCmpConduct, TblCity, TblDictTone, db
from sqlalchemy import alias
from .forms import DictCmpConductForm


@dict_cmp_conduct.route("/conduct/list")
def list():
    data = db.session.query(TblDictCmpConduct).all()
    tones = db.session.query(TblDictTone).all()
    # tone_map = [(tone.tone_id, str(tone.dic_code) + " :" + tone.summary)
    #             for tone in
    #             TblDictTone.query.order_by(TblDictTone.tone_id).all()]
    tone_map = {tone.tone_id: tone.summary
                for tone in tones
                }
    return render_template("dic_cmp_conduct/dict_cmp_conduct_list.html", data=data, tone_map=tone_map)


@dict_cmp_conduct.route("/conduct/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    dict_cmp_accord = TblDictCmpConduct.query.get(id)
    form = DictCmpConductForm()
    if form.validate_on_submit():
        dict_cmp_accord.dic_code = form.dic_code.data
        dict_cmp_accord.tone_id = form.tone_id.data
        dict_cmp_accord.suggest = form.suggest.data
        dict_cmp_accord.risk = form.risk.data
        db.session.add(dict_cmp_accord)
        db.session.commit()
        return redirect(url_for("dict_cmp_conduct.list"))
    form.dic_code.data = dict_cmp_accord.dic_code
    form.tone_id.data = dict_cmp_accord.tone_id
    form.suggest.data = dict_cmp_accord.suggest
    form.risk.data = dict_cmp_accord.risk

    return render_template("dic_cmp_conduct/dict_cmp_conduct_update.html", form=form)


@dict_cmp_conduct.route("/conduct/create", methods=['GET', 'POST'])
def create():
    form = DictCmpConductForm()
    if form.validate_on_submit():
        dict_cmp_conduct = TblDictCmpConduct()
        dict_cmp_conduct.dic_code = form.dic_code.data
        dict_cmp_conduct.tone_id = form.tone_id.data

        dict_cmp_conduct.suggest = form.suggest.data
        dict_cmp_conduct.risk = form.risk.data
        db.session.add(dict_cmp_conduct)
        db.session.commit()
        return redirect(url_for("dict_cmp_conduct.list"))
    return render_template("dic_cmp_conduct/dict_cmp_conduct_update.html", form=form)


@dict_cmp_conduct.route("/conduct/delete/<int:id>", methods=['POST', 'GET'])
def delete(id):
    dict_cmp_conduct = TblDictCmpConduct.query.get(id)
    db.session.delete(dict_cmp_conduct)
    db.session.commit()
    return redirect(url_for("dict_cmp_conduct.list"))
