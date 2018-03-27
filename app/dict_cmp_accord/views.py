from flask import render_template, redirect, url_for
from . import dict_cmp_accord
from ..models import TblDictCmpAccord, TblCity, db
from sqlalchemy import alias
from .forms import DictCmpAccordForm

from .. import photos
from config import Config
import os


@dict_cmp_accord.route("/list")
def list():
    data = db.session.query(TblDictCmpAccord).all()
    return render_template("dict_cmp_accord/dict_cmp_accord_list.html", data=data)


@dict_cmp_accord.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    dict_cmp_accord = TblDictCmpAccord.query.get(id)
    form = DictCmpAccordForm()
    if form.validate_on_submit():
        dict_cmp_accord.dic_code = form.dic_code.data
        dict_cmp_accord.ahead_tone = form.ahead_tone.data
        dict_cmp_accord.behead_tone = form.behead_tone.data

        filename = form.img.data.filename
        print('上传图片：', filename)
        print('本地图片', os.listdir(Config.UPLOADED_PHOTOS_DEST))
        if form.img.data.filename in os.listdir(Config.UPLOADED_PHOTOS_DEST):
            dict_cmp_accord.img = form.img.data.filename
            db.session.add(dict_cmp_accord)
            db.session.commit()
            return redirect(url_for("dict_cmp_accord.list"))
        filename = photos.save(form.img.data, name=filename)
        dict_cmp_accord.trend_advise = form.trend_advise.data

        dict_cmp_accord.img = filename
        db.session.add(dict_cmp_accord)
        db.session.commit()
        return redirect(url_for("dict_cmp_accord.list"))
    form.dic_code.data = dict_cmp_accord.dic_code
    form.ahead_tone.data = dict_cmp_accord.ahead_tone
    form.behead_tone.data = dict_cmp_accord.behead_tone
    form.trend_advise.data = dict_cmp_accord.trend_advise
    form.img.data = photos.url(dict_cmp_accord.img)
    return render_template("dict_cmp_accord/dict_cmp_accord_update.html", form=form)


@dict_cmp_accord.route("/create", methods=['GET', 'POST'])
def create():
    form = DictCmpAccordForm()
    if form.validate_on_submit():
        dict_cmp_accord = TblDictCmpAccord()
        dict_cmp_accord.dic_code = form.dic_code.data
        dict_cmp_accord.ahead_tone = form.ahead_tone.data
        dict_cmp_accord.behead_tone = form.behead_tone.data
        dict_cmp_accord.trend_advise = form.trend_advise.data
        db.session.add(dict_cmp_accord)
        db.session.commit()
        return redirect(url_for("dict_cmp_accord.list"))
    return render_template("dict_cmp_accord/dict_cmp_accord_update.html", form=form)


@dict_cmp_accord.route("/delete/<int:id>", methods=['POST', 'GET'])
def delete(id):
    dict_cmp_accord = TblDictCmpAccord.query.get(id)
    db.session.delete(dict_cmp_accord)
    db.session.commit()
    return redirect(url_for("dict_cmp_accord.list"))
