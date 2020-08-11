from app.admin import admin
from flask import render_template, redirect, url_for, request, flash
from app import login_manager
from flask_login import login_user, logout_user
from app.admin.forms import LoginForm
from app.models import db, Admin



@admin.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # with db.auto_commit():
        #     admin = Admin()
        #     admin.name = form.user.data
        #     admin.password = form.pwd.data
        #     admin.is_super = 0
        #     db.session.add(admin)
        # return redirect(url_for('admin.login'))
        admin = Admin.query.filter_by(name=form.user.data).first()
        if admin:
            if admin.check_password(form.pwd.data):
                login_user(admin, remember=True)  # 登录

                next_url = request.args.get('next')  # 防止重定向攻击
                if next_url and next_url.startswith('/'):
                    pass
                else:
                    next_url = url_for('admin.index')
                return redirect(next_url)
            else:
                flash('密码错误', category='error')
        else:
            flash('用户不存在', category='error')

    return render_template('admin/auth/login.html', form=form)


@admin.route('/logout')
def logout():
    logout_user()  # 登出
    return redirect(url_for('admin.login'))


@admin.route('/change_password')
def change_password():
    return render_template('admin/auth/change_password.html')
