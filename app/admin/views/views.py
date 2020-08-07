from app.admin import admin
from flask import render_template, url_for, redirect


@admin.route('/')
def index():
    return render_template('admin/admin.html')


@admin.route('/tag/add')
def tag_add():
    return render_template('admin/tag_add.html')


@admin.route('/tag/list')
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route('/movie/add')
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route('/movie/list')
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route('/preview/add')
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route('/preview/list')
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route('/user/view')
def user_view():
    return render_template('admin/user_view.html')


@admin.route('/user/list')
def user_list():
    return render_template('admin/user_list.html')


@admin.route('/comment/list')
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route('/moviecol/list')
def movie_col_list():
    return render_template('admin/moviecol_list.html')


@admin.route('/operatelog/list')
def operate_log_list():
    return render_template('admin/operatelog_list.html')


@admin.route('/adminloginlog/list')
def admin_login_log_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route('/userloginlog/list')
def user_login_log_list():
    return render_template('admin/userloginlog_list.html')


@admin.route('/auth/add')
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route('/auth/list')
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route('/role/add')
def role_add():
    return render_template('admin/role_add.html')


@admin.route('/role/list')
def role_list():
    return render_template('admin/role_list.html')


@admin.route('/admin/add')
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route('/admin/list')
def admin_list():
    return render_template('admin/admin_list.html')
