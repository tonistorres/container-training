from flask import Flask
from src.routes.route import *

app = Flask(__name__)
app.add_url_rule(routes["hello"], view_func=routes["hello_world"])
