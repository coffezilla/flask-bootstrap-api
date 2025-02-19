from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def Home():
        return ("Welcome to my home!")

    with app.app_context():
        from .routes.user_routes import user_bp
        from .routes.post_routes import post_bp
        app.register_blueprint(user_bp)
        app.register_blueprint(post_bp)

    return app
