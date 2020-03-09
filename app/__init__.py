from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from functools import reduce
from config import Config


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.template_filter('md')
    def markdowm_to_html(txt):
        from markdown import markdown
        return markdown(txt)

    def read_md(filename):
        with open(filename) as md_file:
            content = md_file.read()
        return content

    @app.context_processor
    def inject_methods():
        return dict(read_md=read_md)
    
    return app


from app import models