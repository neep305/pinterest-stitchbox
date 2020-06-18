from flaskmongo import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session, jsonify
from flaskmongo.models import User


@app.route('/')
def index():
    return render_template('index.html')


# @api.route('/api', '/api/')
# class GetAndPost(Resource):
#
#     # GET All
#     def get(self):
#         return jsonify(User.objects.all())
#
#     # POST
#     def post(self):
#         data = api.payload
#         print(data)
#
#         user = User(user_id=data['user_id'],
#                     email=data['email'],
#                     first_name=data['first_name'],
#                     last_name=data['last_name'])
#
#         user.set_password(data['password'])
#         user.save()
#
#         return jsonify(User.objects(user_id=data['user_id']))
#
#
# @api.route('/api/<idx>')
# class GetUpdateDelete(Resource):
#
#     # GET One
#     def get(self, idx):
#         return jsonify(User.objects(user_id=idx))
#
#     # PUT
#     def put(self, idx):
#         data = api.payload
#         User.objects(user_id=idx).update(**data)
#         return jsonify(User.objects(user_id=idx))
#
#     # DELETE
#     def delete(self, idx):
#         User.objects(user_id=idx).delete()
#         return jsonify("User is deleted!!")


@app.route('/login')
def login():
    return render_template('login.html', login=True)


@app.route('/register')
def register():
    return render_template('register.html', register=True)


@app.route('/enrollment', methods=["GET", "POST"])
def enrollment():
    id = request.args.get('courseID')
    title = request.args.get('title')
    term = request.args.get('term')
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "term": term})


courseData = [{"courseID": "1111", "title": "PHP 111", "description": "Intro to PHP", "credits": "3", "term": "Fall, Spring"}, {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": "4", "term": "Spring"}, {"courseID": "3333", "title": "Adv PHP 201",
                                                                                                                                                                                                                                                       "description": "Advanced PHP Programming", "credits": "3", "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": "3", "term": "Fall, Spring"}, {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": "4", "term": "Fall"}]


@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term="Spring 2019"):
    return render_template('courses.html', courseData=courseData, courses=True, term=term)


@app.route('/user')
def user():
    User(user_id=1, first_name="Jason", last_name="Nam",
         email="neep305@gmail.com", password="1111").save()
    User(user_id=2, first_name="Mary", last_name="Nam",
         email="neep305@naver.com", password="1111").save()
    users = User.objects.all()

    return render_template("user.html", users=users)
