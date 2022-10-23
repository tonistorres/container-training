from flask.views import MethodView


class HelloWorld(MethodView):
    def get(self):
        return "Olá todos do Canal"
