#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: login.py
@time: 2017/3/10 下午10:49
"""


from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, BooleanField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo, Email, ValidationError, IPAddress
from app_frontend.api.user_auth import get_user_auth_row
from app_frontend.forms import SelectAreaCode
from app_common.maps import area_code_list


class LoginForm(Form):
    """
    账号登陆表单
    """
    account = StringField(u'登陆账号', validators=[DataRequired()])
    password = PasswordField(u'登陆密码', validators=[DataRequired()])
    remember = BooleanField(u'记住登录状态', default=False)


class LoginPhoneForm(Form):
    """
    手机登陆表单
    """
    area_code_choices = []
    for m, n in enumerate(area_code_list):
        area_code_choices.append((m, n))

    area_id = SelectAreaCode(u'手机区号', default='0', choices=area_code_choices, validators=[DataRequired()])
    phone = StringField(u'登录手机', validators=[DataRequired()])
    password = PasswordField(u'登陆密码', validators=[DataRequired()])
    remember = BooleanField(u'记住登录状态', default=False)


class LoginEmailForm(Form):
    """
    邮箱登陆表单
    """
    email = StringField(u'登陆邮箱', validators=[DataRequired(), Email()])
    password = PasswordField(u'登陆密码', validators=[DataRequired()])
    remember = BooleanField(u'记住登录状态', default=False)
