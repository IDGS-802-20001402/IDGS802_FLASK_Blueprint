from flask import Blueprint

directivos_bp = Blueprint('directivos', __name__)

@directivos_bp.route('/directivos', methods=['GET'])
def alumnos():
    return {'principal':'Directivos'}