from flask import Flask, request, jsonify, make_response, session, url_for
from flask.json import JSONEncoder
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import redirect

import flaskapp.models
from flaskapp.app_decorator import login_required
from flaskapp.form_validator import RegisterForm, RegistrationForm, LoginForm
from flaskapp.models import User
from flaskapp.database import db_session


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return JSONEncoder.default(self, o)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pypostgresql://sqlalchemy:sqlalchemy@localhost/sqlalchemy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "wcsfeufhwiquehfdx"
# app.config['WTF_CSRF_SECRET_KEY'] = "testestest"

# csrf = CSRFProtect()
# csrf.init_app(app)

db = SQLAlchemy(app)


@app.route("/")
def response_test():
    return render_template('home.html') # make_response("Custom Response")


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route("/member")
@login_required
def member_page():
    return render_template("/member_page.html")


# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegisterForm(request.form)
#
#     if form.validate_on_submit():
#         # insert user start
#         userid = request.form.get('userid')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         re_password = request.form.get('re_password')
#         print(password)
#
#         if not (userid and username and password and re_password):
#             return "모두 입력해주세요"
#         elif password != re_password:
#             return "비밀번호를 확인해주세요"
#         else:
#             user = User()
#             user.password = password
#             user.id = userid
#             user.name = username
#         db_session.add(user)
#         db_session.commit()
#         # insert user end
#         return "가입 완료"
#     return render_template('register.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        user = User(form.userid.data, form.username.data, form.password.data)
        db_session.add(user)
        
        return redirect(url_for('login'))
    else:
        print(request.method)
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    
    return render_template('login-test.html', form=form)


@app.route('/main', methods=['GET', 'POST'])
def main():
    
    return render_template('main.html')
