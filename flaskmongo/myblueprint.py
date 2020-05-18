from flask import Blueprint
from flask import render_template

example_blueprint = Blueprint('example_blueprint', __name__,
                              static_folder='simple_static', static_url_path='/simple_static', template_folder='simple_templates')


@example_blueprint.route('/example')
def index():
    # return "This is an example app"
    return render_template('index.html')
