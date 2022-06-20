

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from models import User


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[
                           DataRequired(message="값을 입력하세요")])
    userid = StringField('userid', validators=[
                         DataRequired(message="값을 입력하세요")])
    userpw = PasswordField('userpw', validators=[
                           DataRequired(), Length(min=3, message="최소 3자 이상 입력하세요.")])
    userpw_check = PasswordField('userpw_check', validators=[
                                 DataRequired(), EqualTo('userpw_check', message="비밀번호가 서로 다릅니다.")])


class LoginFrom(FlaskForm):

    class UserPassword(object):
        def __inti__(self, message=None):
            self.message = message

        def __call__(self, form, field):
            userid = form['userid'].data
            userpw = form['userpw'].data
            # userpw = field.data 왜 비번이 오는지 모르곘어

            user = User.query.filter_by(userid=userid).first()
            if user.userpw != userpw:
                raise ValidationError("비밀번호가 틀립니다.")

    userid = StringField('userid', validators=[DataRequired()])
    userpw = PasswordField('userpw', validators=[
                           DataRequired(), UserPassword()])
