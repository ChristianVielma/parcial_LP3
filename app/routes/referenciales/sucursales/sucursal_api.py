from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.sucursales.SucursalDao import SucursalDao

sucursalapi = Blueprint('sucursalapi', __name__)

# Trae todas las sucursales
@sucursalapi.route('/sucursales', methods=['GET'])
def getSucursales():  
    sucursal_dao = SucursalDao()

    try:
        sucursales = sucursal_dao.getSucursales()

        return jsonify({
            'success': True,
            'data': sucursales,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las sucursales: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sucursalapi.route('/sucursales/<int:id_sucursal>', methods=['GET'])
def get_sucursal(id_sucursal):  
    sucursal_dao = SucursalDao()

    try:
        sucursal = sucursal_dao.getSucursalById(id_sucursal)

        if sucursal:
            return jsonify({
                'success': True,
                'data': sucursal,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la sucursal con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva sucursal
@sucursalapi.route('/sucursales', methods=['POST'])
def addSucursal():
    data = request.get_json()
    sucursal_dao = SucursalDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['suc_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_sucursal = data['suc_descripcion'].upper()
        id_sucursal = sucursal_dao.guardarSucursal(nombre_sucursal)
        if id_sucursal is not None:
            return jsonify({
                'success': True,
                'data': {'id_sucursal': id_sucursal, 'suc_descripcion': nombre_sucursal},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la sucursal. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sucursalapi.route('/sucursales/<int:id_sucursal>', methods=['PUT'])
def updateSucursal(id_sucursal):
    data = request.get_json()
    sucursal_dao = SucursalDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['suc_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    nombre_sucursal = data['suc_descripcion']
    try:
        if sucursal_dao.updateSucursal(id_sucursal, nombre_sucursal.upper()):
            return jsonify({
                'success': True,
                'data': {'id_sucursal': id_sucursal, 'suc_descripcion': nombre_sucursal},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la sucursal con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sucursalapi.route('/sucursales/<int:id_sucursal>', methods=['DELETE'])
def deleteSucursal(id_sucursal):
    sucursal_dao = SucursalDao()

    try:
        # Usar el retorno de eliminarSucursal para determinar el éxito
        if sucursal_dao.deleteSucursal(id_sucursal):
            return jsonify({
                'success': True,
                'mensaje': f'Sucursal con ID {id_sucursal} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la sucursal con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar sucursal: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
