from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from DBManager import *


def exist_login(form, field):
    if DBUsers.query.filter_by(username=field.data).all():
        raise ValidationError("Такой пользователь уже существует")


def exist_email(form, field):
    if DBUsers.query.filter_by(email=field.data).all():
        raise ValidationError("Пользователь с такой почтой существует")


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=4, max=20,
                                                                 message="Слишком маленькая или большая строка")])
    surname = StringField('Фамилия', validators=[DataRequired(),
                                                 Length(min=4, max=50, message="Слишком маленькая или большая строка")])
    username = StringField('Логин', validators=[DataRequired(),
                                                Length(min=4, max=25, message="Слишком маленькая или большая строка"),
                                                exist_login])
    password = PasswordField('Пароль',
                             validators=[DataRequired(),
                                         Length(min=4, max=30, message="Слишком маленькая или большая строка"),
                                         EqualTo("confirm", message="Пароли не совпадают")])
    confirm = PasswordField('Повторите пароль')
    email = StringField('Почта', validators=[Email("Неправильный почтовый адрес"), Length(max=120), exist_email])
    submit = SubmitField('Зарегистрироваться')


class AddNewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
