from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


# this is a default home page
@main.route("/")
# this is a designated home page
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    # this will order posts in descending order, meaning, latest/newest posts will be displayed first,
    # oldest will be last with 5 posts per page
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title="About")
