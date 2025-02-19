from flask import Blueprint

post_bp = Blueprint('post', __name__)


@post_bp.route('/post')
def post():
    return "Hello post"
