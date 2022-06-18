from flask_views import app_ctx, db
from flask_views.views import IndexView, CreateUserView, DeleteUserViews, UpdateUserView

app_ctx.add_url_rule('/', view_func=IndexView.as_view(name='index',
                                                      template_name='flask_views/index.html', info='Are you updated?'))
app_ctx.add_url_rule('/create/<string:username>/<string:email>',
                     view_func=CreateUserView.as_view(name='create', username='username', email='email'))
app_ctx.add_url_rule('/update/<string:username>',
                     view_func=UpdateUserView.as_view(name='update', username='username'))
app_ctx.add_url_rule('/delete/<string:username>', view_func=DeleteUserViews.as_view(name='delete', username='username'))
if __name__ == '__main__':
    with app_ctx.app_context():
        db.create_all()
    app_ctx.run()
