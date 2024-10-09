from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.existencias.ExistenciaDao import ExistenciaDao

exisapi = Blueprint('exisapi', __name__)

# Trae todos los existencias
@exisapi.route('/existencias', methods=['GET'])
def getExistencia():  

    exisdao = ExistenciaDao()

    try:
        existencias = exisdao.getExistencia()

        return jsonify({
            'success': True,
            'data': existencias,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los existencias: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@exisapi.route('/existencias/<int:id_producto>', methods=['GET'])
def get_existencia(id_producto):  
    exisdao = ExistenciaDao()

    try:
        existencia = exisdao.getExistenciaById(id_producto)

        if existencia:
            return jsonify({
                'success': True,
                'data': existencia,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la existencias con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener existencias: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo existencia
# @exisapi.route('/existencias', methods=['POST'])
# def addExistencia():
#     data = request.get_json()
#     exisdao = ExistenciaDao()

#     # Validar que el JSON no esté vacío y tenga las propiedades necesarias
#     campos_requeridos = ['exis_cantidad']

#     # Verificar si faltan campos o son vacíos
#     for campo in campos_requeridos:
#         if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
#             return jsonify({
#                             'success': False,
#                             'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
#                             }), 400

#     try:
#         exis_cantidad = data['exis_cantidad']
#         id_producto = exisdao.guardarExistencia(exis_cantidad)
#         if id_producto is not None:
#             return jsonify({
#                 'success': True,
#                 'data': {'id_producto': id_producto, 'exis_cantidad': exis_cantidad},
#                 'error': None
#             }), 201
#         else:
#             return jsonify({ 'success': False, 'error': 'No se pudo guardar el exis_cantida. Consulte con el administrador.' }), 500
#     except Exception as e:
#         app.logger.error(f"Error al agregar exis_cantida: {str(e)}")
#         return jsonify({
#             'success': False,
#             'error': 'Ocurrió un error interno. Consulte con el administrador.'
#         }), 500

@exisapi.route('/existencias/<int:id_producto>', methods=['PUT'])
def updateExistencia(id_producto):
    data = request.get_json()
    exisdao = ExistenciaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['exis_cantidad']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    exis_cantidad = data['exis_cantidad']
    try:
        if exisdao.updateExistencia(id_producto, exis_cantidad):
            return jsonify({
                'success': True,
                'data': {'id_producto': id_producto, 'exis_cantidad': exis_cantidad},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el existencia con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar existencia: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@exisapi.route('/existencias/<int:id_producto>', methods=['DELETE'])
def deleteExistencia(id_producto):
    exisdao = ExistenciaDao()

    try:
        # Usar el retorno de eliminarExistencia para determinar el éxito
        if exisdao.deleteExistencia(id_producto):
            return jsonify({
                'success': True,
                'mensaje': f'Existencia con ID {id_producto} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el existencia con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar existencia: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
