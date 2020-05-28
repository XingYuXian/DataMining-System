import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request, jsonify, json
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr import db
from flaskr.model.User_model import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
        print(type(password))
        user = User.objects(username=username).first()
        if not user:
            return jsonify({'code': 0, 'error': '此用户不存在'})
        user.to_json()
        if user["password"] != password:
            print(user["password"])
            print(type(user["password"]))
            print(password)
            return jsonify({'code': 0, 'error': '密码错误'})
        else:
            return jsonify({'code': 1, 'username': user.username})
    return 'hh'


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
        mail = data['mail']
        user = User.objects(username=username).first()
        if not user:
            D = User(
                username=username,
                password=password,
                mail=mail
            )
            D.save()
            return jsonify({'status': 0, 'username': D.username})
        else:
            return jsonify({'error': '用户已存在'})
    return 'h'
