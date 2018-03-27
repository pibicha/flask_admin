from flask import render_template, redirect, url_for
from . import tone
from ..models import TblDictTone, TblCity, db
from sqlalchemy import alias
from .forms import ToneForm


@tone.route("/dict_list")
def dict_list():
    data = db.session.query(TblDictTone).all()
    return render_template("tone/dict_list.html", data=data)


@tone.route("/tone/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    tone = TblDictTone.query.get(id)
    form = ToneForm()
    if form.validate_on_submit():
        tone.dict_code = form.dic_code.data
        tone.summary = form.summary.data
        tone.val = form.val.data
        tone.lower_scope = form.lower_scope.data
        tone.upper_scope = form.upper_scope.data
        db.session.add(tone)
        db.session.commit()
        return redirect(url_for("tone.dict_list"))
    form.dic_code.data = tone.dic_code
    form.summary.data = tone.summary
    form.val.data = tone.val
    form.lower_scope.data = tone.lower_scope
    form.upper_scope.data = tone.lower_scope
    return render_template("tone/tone_update.html", form=form)


@tone.route("/tone/create", methods=['GET', 'POST'])
def create():
    form = ToneForm()
    if form.validate_on_submit():
        tone = TblDictTone()
        tone.dic_code = form.dic_code.data
        tone.summary = form.summary.data
        tone.val = form.val.data
        tone.lower_scope = form.lower_scope.data
        tone.upper_scope = form.upper_scope.data
        db.session.add(tone)
        db.session.commit()
        return redirect(url_for("tone.dict_list"))
    return render_template("tone/tone_update.html", form=form)


@tone.route("/tone/delete/<int:id>", methods=['POST', 'GET'])
def delete(id):
    tone = TblDictTone.query.get(id)
    db.session.delete(tone)
    db.session.commit()
    return redirect(url_for("tone.dict_list"))
