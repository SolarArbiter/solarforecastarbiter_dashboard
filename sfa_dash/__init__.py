from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_24nsdagnnt2#%53moz'
    app.config.from_object('sfa_dash.config.LocalConfig')
    from blueprints.main import data_dash_blp
    from blueprints.form import forms_blp
    from blueprints.demo import demo_blp
    # TODO: remove the schema blp when it's added to the api
    app.register_blueprint(data_dash_blp)
    app.register_blueprint(forms_blp)
    app.register_blueprint(demo_blp)
    #hi
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
