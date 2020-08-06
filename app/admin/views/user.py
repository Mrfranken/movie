from app.admin import admin
from flask import render_template, redirect, url_for


@admin.route("/login")
def login():
    return render_template('admin/auth/login.html')


@admin.route('/logout')
def logout():
    return redirect(url_for('admin.login'))


@admin.route('/change_password')
def change_password():
    return render_template('admin/auth/change_password.html')
