from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.cajas.cajaDao import CajasDao

cajapi = Blueprint('cajapi', __name__)

# Trae todas las cajas
@cajapi.route('/cajas', methods=['GET'])
def getCajas():  

    cajdao = CajasDao()

    try:
        cajas = cajdao.getCajas()

        return jsonify({
            'success': True,
            'data': cajas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las cajas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cajapi.route('/cajas/<int:id_caja>', methods=['GET'])
def get_caja(id_caja):  
    cajdao = CajasDao()

    try:
        caja = cajdao.getCajasById(id_caja)

        if caja:
            return jsonify({
                'success': True,
                'data': caja,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la caja con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva caja
@cajapi.route('/cajas', methods=['POST'])
def addCaja():
    data = request.get_json()
    cajdao = CajasDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['monto_apertura']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        monto_apertura = data['monto_apertura']
        id_caja = cajdao.guardarCaja(monto_apertura)
        if id_caja is not None:
            return jsonify({
                'success': True,
                'data': {'id_caja': id_caja, 'monto_apertura': monto_apertura},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la caja. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cajapi.route('/cajas/<int:id_caja>', methods=['PUT'])
def updateCaja(id_caja):
    data = request.get_json()
    cajdao = CajasDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['monto_apertura']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    monto_apertura = data['monto_apertura']
    try:
        if cajdao.updateCaja(id_caja, monto_apertura):
            return jsonify({
                'success': True,
                'data': {'id_caja': id_caja, 'monto_apertura': monto_apertura},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la caja con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@cajapi.route('/cajas/<int:id_caja>', methods=['DELETE'])
def deleteCaja(id_caja):
    cajdao = CajasDao()

    try:
        # Usar el retorno de eliminarCaja para determinar el éxito
        if cajdao.deleteCaja(id_caja):
            return jsonify({
                'success': True,
                'data': f'Caja con ID {id_caja} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la caja con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar caja: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500


