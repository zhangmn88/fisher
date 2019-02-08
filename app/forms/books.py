#!/usr/bin/python
# coding: utf8


from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, DataRequired, NumberRange


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=20)], default=1)

