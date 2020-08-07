from app.admin import admin
from flask import render_template, redirect, url_for, request, flash
from app import login_manager
from app.admin.forms import LoginForm
from app.models import Admin


@admin.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Admin.query.filter_by(name=form.user.data).first()
        if user:
            if user.check_password(form.pwd.data):
                next_url = request.args.get('next')  # 防止重定向攻击
                print('next_url is: ', next_url)
                if next_url and next_url.startswith('/'):
                    pass
                else:
                    next_url = url_for('admin.login')
                return redirect(next_url)
            else:
                flash('密码错误', category='error')
        else:
            flash('用户不存在', category='error')

    return render_template('admin/auth/login.html', form=form)


@admin.route('/logout')
def logout():
    return redirect(url_for('admin.login'))


@admin.route('/change_password')
def change_password():
    return render_template('admin/auth/change_password.html')
