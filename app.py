import os
from logging import debug
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY") # os.urandom(64)
    load_dotenv()
    app.config.update(
        ADMIN=os.environ.get("ADMIN")
    )

    @app.route("/")
    def home():
        return render_template("home.html")

    app.register_blueprint(alert_blueprint, url_prefix="/alerts")
    app.register_blueprint(store_blueprint, url_prefix="/stores")
    app.register_blueprint(user_blueprint, url_prefix="/users")

    return app

# app = Flask(__name__)
# app.secret_key = os.environ.get("SECRET_KEY") # os.urandom(64)
# app.config.update(
#         ADMIN=os.environ.get("ADMIN")
#     )

# @app.route("/")
# def home():
#     return render_template("home.html")

# app.register_blueprint(alert_blueprint, url_prefix="/alerts")
# app.register_blueprint(store_blueprint, url_prefix="/stores")
# app.register_blueprint(user_blueprint, url_prefix="/users")

    
if __name__ == "__main__":
    app.run(debug=True)