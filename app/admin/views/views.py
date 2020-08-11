from app.admin import admin
from app.admin.forms import TageForm
from app.models import db, Tag
from flask import render_template, url_for, redirect, request, flash
from flask_login import login_required


@admin.route('/')
@login_required
def index():
    return render_template('admin/admin.html')


@admin.route('/tag/add', methods=['POST', 'GET'])
@login_required
def tag_add():
    form = TageForm(request.form)
    if request.method == 'POST' and form.validate():
        tag = Tag.query.filter_by(name=form.name.data).first()
        if not tag:
            with db.auto_commit():
                tag = Tag()
                tag.set_value_for_table(form.data)
                db.session.add(tag)
            flash(message='标签添加成功', category='message')
        else:
            flash(message='标签已存在', category='error')
    return render_template('admin/tag_add.html', form=form)


@admin.route('/tag/list/<int:page>', methods=["GET"])
@login_required
def tag_list(page=None):
    tag_data = Tag.get_tags_by_page(page)
    return render_template('admin/tag_list.html', tag_data=tag_data)


@admin.route('/movie/add')
@login_required
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route('/movie/list')
@login_required
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route('/preview/add')
@login_required
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route('/preview/list')
@login_required
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route('/user/view')
@login_required
def user_view():
    return render_template('admin/user_view.html')


@admin.route('/user/list')
@login_required
def user_list():
    return render_template('admin/user_list.html')


@admin.route('/comment/list')
@login_required
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route('/moviecol/list')
@login_required
def movie_col_list():
    return render_template('admin/moviecol_list.html')


@admin.route('/operatelog/list')
@login_required
def operate_log_list():
    return render_template('admin/operatelog_list.html')


@admin.route('/adminloginlog/list')
@login_required
def admin_login_log_list():
    return render_template('admin/adminloginlog_list.html')


@admin.route('/userloginlog/list')
@login_required
def user_login_log_list():
    return render_template('admin/userloginlog_list.html')


@admin.route('/auth/add')
@login_required
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route('/auth/list')
@login_required
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route('/role/add')
@login_required
def role_add():
    return render_template('admin/role_add.html')


@admin.route('/role/list')
@login_required
def role_list():
    return render_template('admin/role_list.html')


@admin.route('/admin/add')
@login_required
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route('/admin/list')
@login_required
def admin_list():
    return render_template('admin/admin_list.html')
