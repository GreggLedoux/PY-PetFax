from flask import Flask 


def create_app():

    app = Flask(__name__)

    from . import pet
    app.register_blueprint(pet.bp)


    @app.route('/')
    def index():
        return 'This is the home page'


   
    

    return app
