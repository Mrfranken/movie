from app.admin import admin
from flask import render_template, url_for, redirect


@admin.route('/')
def admin():
    return render_template('admin/admin.html')
