from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.depositos.DepositoDao import DepositoDao

depoapi = Blueprint('depoapi', __name__)

# Trae todos los depositos
@depoapi.route('/depositos', methods=['GET'])
def getDeposito():  

    depodao = DepositoDao()

    try:
        depositos = depodao.getDeposito()

        return jsonify({
            'success': True,
            'data': depositos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los depositos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@depoapi.route('/depositos/<int:id_deposito>', methods=['GET'])
def get_deposito(id_deposito):  
    depodao = DepositoDao()

    try:
        deposito = depodao.getDepositoById(id_deposito)

        if deposito:
            return jsonify({
                'success': True,
                'data': deposito,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el deposito con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener deposito: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo deposito
@depoapi.route('/depositos', methods=['POST'])
def addDeposito():
    data = request.get_json()
    depodao = DepositoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        depo_descripcion = data['descripcion'].upper()
        id_deposito = depodao.guardarDeposito(depo_descripcion)
        if id_deposito is not None:
            return jsonify({
                'success': True,
                'data': {'id_deposito': id_deposito, 'descripcion': depo_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el deposito. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar deposito: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@depoapi.route('/depositos/<int:id_deposito>', methods=['PUT'])
def updateDeposito(id_deposito):
    data = request.get_json()
    depodao = DepositoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    depo_descripcion = data['descripcion']
    try:
        if depodao.updateDeposito(id_deposito, depo_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_deposito': id_deposito, 'descripcion': depo_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el deposito con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar deposito: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@depoapi.route('/depositos/<int:id_deposito>', methods=['DELETE'])
def deleteDeposito(id_deposito):
    depodao = DepositoDao()

    try:
        # Usar el retorno de eliminarDeposito para determinar el éxito
        if depodao.deleteDeposito(id_deposito):
            return jsonify({
                'success': True,
                'mensaje': f'Deposito con ID {id_deposito} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el deposito con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar deposito: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
