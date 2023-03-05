from flask import Blueprint

alumnos_bp = Blueprint('alumnos', __name__)

@alumnos_bp.route('/alumnos', methods=['GET'])
def alumnos():
    return {'principal':'Alumnos'}
