import os
import json
import random

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session
from flask_wtf.csrf import CSRFProtect
import requests

from models import db
from models import User, Problem, Solve

from forms import RegisterForm, LoginFrom, GetForm


app = Flask(__name__)

# 메인페이지


@app.route('/')
def hello():
    username = session.get('username', '')
    return render_template('index.html', user=username)

# 로그인


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(userid=form.data.get('userid')).first()
        session['username'] = user.username
        return redirect('/')
    return render_template('login.html', login=form)

# 로그아웃


@app.route('/logout/')
def logout():
    del session['username']
    # session.pop('username')
    return redirect('/')

# 회원가입


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

# 개별 문제 확인


@app.route('/problem/<int:count>/')
def problem(count: int = None):
    problem = Problem.query.filter_by(id=count).first()
    return render_template('one_problem.html', problem=problem)

# 문제들 확인


@app.route('/problem/')
def problems():
    page = request.args.get('page', type=int, default=1)  # 페이지
    problem = Problem.query.order_by(Problem.id.desc())
    problem = problem.paginate(page, per_page=15)
    return render_template('problem.html', list=problem)

# # 문제 등록
# @app.route('/problem/')
# def create_problems():
#     problem = Problem.query.all()
#     return render_template('problem.html', list=problem)

# 문제 풀기


@app.route('/start/', methods=['GET', 'POST'])
def start():
    form = GetForm()
    dicts = request.args.to_dict()
    if dicts:
        # 문제수 선택 완료
        number = int(dicts.get('number'))
        problems = Problem.query.all()
        select_problems = random.choices(problems, k=number)
        select_problems = set(select_problems)
        return render_template('start.html', form=form, pro=select_problems)
    return render_template('start.html', form=form)

# 문제 제출


@app.route('/submission/')
def subminssion():
    dicts = request.args.to_dict()
    user = session.get('username')
    user_id = User.query.filter_by(username=user).first()
    if dicts:
        for k, v in dicts.items():
            info = Solve()
            info.user_id = user_id.id
            info.problem_id = int(k)
            info.answer = v
            db.session.add(info)
            db.session.commit()
    return redirect('/')

# 풀이 확인


@app.route('/check/')
def checks():
    page = request.args.get('page', type=int, default=1)  # 페이지
    solve = Solve.query.order_by(Solve.check)
    solve = solve.paginate(page, per_page=15)
    return render_template('check.html', list=solve)
# 개별풀이 확인


@app.route('/check/<int:count>/')
def check(count: int = None):
    dicts = request.args.to_dict()
    if dicts:
        one = Solve.query.filter_by(id=count).first()
        one.check = int(dicts.get('check'))
        db.session.add(one)
        db.session.commit()
        return redirect('/check/')
    sovle = Solve.query.filter_by(id=count).first()
    return render_template('one_check.html', sovle=sovle)

# 문제등록


@app.route('/create/')
def create():
    dicts = request.args.to_dict()
    print(dicts)
    if dicts:
        problem = Problem()
        problem.title = dicts.get('title')
        problem.text = dicts.get('text')
        db.session.add(problem)
        db.session.commit()
        return redirect('/')
    return render_template('create.html')


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
