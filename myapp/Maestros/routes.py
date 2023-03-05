from flask import Blueprint

maestros_bp = Blueprint('maestros', __name__)

@maestros_bp.route('/maestros', methods=['GET'])
def maestros():
    return {'principal':'Maestros'}