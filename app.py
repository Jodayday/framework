import os
import json

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask_wtf.csrf import CSRFProtect

from models import db
from models import User, Problem, Solve

from forms import RegisterForm, LoginFrom, GetForm


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


@app.route('/problem/<int:count>/')
def problem(count: int = None):
    problem = Problem.query.filter_by(id=count).first()
    return render_template('one_problem.html', problem=problem)


@app.route('/problem/')
def problems():
    problem = Problem.query.all()
    return render_template('problem.html', list=problem)

# # 문제 등록
# @app.route('/problem/')
# def create_problems():
#     problem = Problem.query.all()
#     return render_template('problem.html', list=problem)


@app.route('/start/', methods=['GET', 'POST'])
def start():
    form = GetForm()
    dicts = request.args.to_dict()
    if dicts != None:
        tn = dicts.get('tn')
        print(tn)
    return render_template('start.html', form=form)

# db 설정


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets = json.loads(open(SECRET_FILE).read())
DB = secrets["DB"]
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}"
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
