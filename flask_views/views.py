from flask import render_template, flash, url_for
from flask.views import View, MethodView
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from werkzeug.utils import redirect

from flask_views import app_ctx
from flask_views.forms import UpdateForm
from flask_views.models import User, db


@app_ctx.errorhandler(404)
def page_not_found(e):
    return render_template('flask_views/404.html')


class IndexView(View):
    def __init__(self, template_name, info):
        self.template_name = template_name
        self.info = info

    def dispatch_request(self):
        users = User.query.all()
        form = UpdateForm()
        return render_template(self.template_name, info=self.info, users=users, form=form)


class CreateUserView(MethodView):

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def get(cls, username, email):
        user = User(username=username, email=email)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'Пользователь {user} создан!', 'success')
        except IntegrityError:
            flash(f'Пользователь {user} уже существует!', 'primary')
        return redirect(url_for('index'))


class UpdateUserView(MethodView):

    def __init__(self, username):
        self.username = username

    @staticmethod
    def get():
        return redirect(url_for('index'))

    @classmethod
    def post(cls, username):
        form = UpdateForm()
        user = User.query.filter_by(username=username).first()
        if form.validate_on_submit():
            try:
                user.username = form.username.data
                db.session.commit()
                flash(f'Пользователь {user} обновлен!', 'warning')
            except (IntegrityError, PendingRollbackError):
                db.session.rollback()
                flash(f'Пользователь {user} уже существует!', 'primary')
            return redirect(url_for('index'))
        else:
            flash(form.errors, 'success')
            return redirect(url_for('index'))


class DeleteUserViews(MethodView):
    def __init__(self, username):
        self.username = username

    @classmethod
    def get(cls, username):
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        flash(f'Пользователь {user} удалён!', 'danger')
        return redirect(url_for('index'))
