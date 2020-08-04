from app.home import home
from flask import render_template, redirect, url_for


@home.route('/login')
def login():
    return render_template('home/user/login.html')


@home.route('/logout')
def logout():
    return redirect(url_for('home.index'))


@home.route('/register')
def register():
    return render_template('home/user/register.html')


@home.route('/user')
def user():
    return render_template('home/user/user.html')


@home.route('/user/change/password')
def change_password():
    return render_template('home/user/change_password.html')


@home.route('/user/comments')
def comments():
    return render_template('home/user/comments.html')


@home.route('/user/loginlog')
def loginlog():
    return render_template('home/user/loginlog.html')


@home.route('/user/moviecol')
def moviecol():
    return render_template('home/user/moviecol.html')
