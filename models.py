from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(10), unique=True)
    userpw = db.Column(db.String(20))
    username = db.Column(db.String(10))


class Problem(db.Model):
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    # choice = db.Column(db.String(255))
    # img = db.Column(db.LargeBinary)
    text = db.Column(db.String(255), nullable=False)


class Solve(db.Model):
    __tablename__ = "solves"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id", ondelete='CASCADE'))
    problem_id = db.Column(db.Integer, db.ForeignKey(
        "problems.id", ondelete='CASCADE'))
    answer = db.Column(db.String(255))
    check = db.Column(db.Boolean)
    user = db.relationship("User", backref=db.backref('user_set'))
    problem = db.relationship("Problem", backref=db.backref('problem_set'))
