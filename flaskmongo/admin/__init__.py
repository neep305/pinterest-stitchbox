from flask import Blueprint
from flask import Flask, render_template, request, redirect, url_for

admin = Blueprint('admin', __name__,
                  static_folder='static',
                  static_url_path='/static',
                  template_folder='templates')


@admin.route('/admin', methods=['GET', 'POST'])
def index():
    return render_template('admin/index.html')
