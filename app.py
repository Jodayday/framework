import os

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask_wtf.csrf import CSRFProtect

from models import db
from models import User

from forms import RegisterForm, LoginFrom


app = Flask(__name__)


@app.route('/')
def hello():
    username = session.get('username', '')
    return render_template('index.html', user=username)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(userid=form.data.get('userid')).first()
        session['username'] = user.username
        return redirect('/')
    return render_template('login.html', login=form)


@app.route('/logout/')
def logout():
    del session['username']
    # session.pop('username')
    return redirect('/')


@app.route('/register/', methods=['GET', 'POST'])
def join():
    form = RegisterForm()

    if form.validate_on_submit():
        # 회원정보 생성
        user_info = User()
        user_info.userid = form.data.get('userid')
        user_info.userpw = form.data.get('userpw')
        user_info.username = form.data.get('username')
        db.session.add(user_info)
        db.session.commit()

        return redirect('/')

    return render_template('register.html', Register=form)


# db 설정
basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dlatltlzmfltzltkdyd'

# csrf 설정
csrf = CSRFProtect()
csrf.init_app(app)

# db 초기화
db.init_app(app)
db.app = app
db.create_all()
# 실행

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


# 실행
# flask run
# FLASK_APP=app.py flask run
