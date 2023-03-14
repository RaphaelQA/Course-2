import logging
from flask import Flask, request, render_template, send_from_directory

from api.api import api_blueprint
from main.views import main_blueprint

app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)



if __name__ == "__main__":
    app.run(host='0.0.0.0'Debug=True)
