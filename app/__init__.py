from flask import Flask
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../instance/config.py')

    from . import routes
    app.register_blueprint(routes.bp)

    @app.context_processor
    def inject_year():
        return {'current_year': datetime.now().year}

    return app