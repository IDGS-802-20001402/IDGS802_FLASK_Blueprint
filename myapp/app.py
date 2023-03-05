import flask

from Alumnos.routes import alumnos_bp
from Directivos.routes import directivos_bp
from Maestros.routes import maestros_bp

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=["GET"])
def home():
    return flask.jsonify({'principal':'HOME'})

app.register_blueprint(alumnos_bp)
app.register_blueprint(directivos_bp)
app.register_blueprint(maestros_bp)

if __name__ == '__main__':
    app.run()