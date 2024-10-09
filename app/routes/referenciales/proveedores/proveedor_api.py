from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.proveedores.ProveedorDao import ProveedorDao

proveedorapi = Blueprint('proveedorapi', __name__)

# Trae todos los proveedores
@proveedorapi.route('/proveedores', methods=['GET'])
def getProveedores():  
    proveedor_dao = ProveedorDao()

    try:
        proveedores = proveedor_dao.getProveedores()

        return jsonify({
            'success': True,
            'data': proveedores,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los proveedores: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@proveedorapi.route('/proveedores/<int:id_proveedor>', methods=['GET'])
def get_proveedor(id_proveedor):  
    proveedor_dao = ProveedorDao()

    try:
        proveedor = proveedor_dao.getProveedorById(id_proveedor)

        if proveedor:
            return jsonify({
                'success': True,
                'data': proveedor,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el proveedor con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener proveedor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo proveedor
@proveedorapi.route('/proveedores', methods=['POST'])
def addProveedor():
    data = request.get_json()
    proveedor_dao = ProveedorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['prov_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_proveedor = data['prov_descripcion'].upper()
        id_proveedor = proveedor_dao.guardarProveedor(nombre_proveedor)
        if id_proveedor is not None:
            return jsonify({
                'success': True,
                'data': {'id_proveedor': id_proveedor, 'prov_descripcion': nombre_proveedor},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el proveedor. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar proveedor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@proveedorapi.route('/proveedores/<int:id_proveedor>', methods=['PUT'])
def updateProveedor(id_proveedor):
    data = request.get_json()
    proveedor_dao = ProveedorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['prov_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    nombre_proveedor = data['prov_descripcion']
    try:
        if proveedor_dao.updateProveedor(id_proveedor, nombre_proveedor.upper()):
            return jsonify({
                'success': True,
                'data': {'id_proveedor': id_proveedor, 'prov_descripcion': nombre_proveedor},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el proveedor con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar proveedor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@proveedorapi.route('/proveedores/<int:id_proveedor>', methods=['DELETE'])
def deleteProveedor(id_proveedor):
    proveedor_dao = ProveedorDao()

    try:
        # Usar el retorno de eliminarProveedor para determinar el éxito
        if proveedor_dao.deleteProveedor(id_proveedor):
            return jsonify({
                'success': True,
                'mensaje': f'Proveedor con ID {id_proveedor} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el proveedor con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar proveedor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
