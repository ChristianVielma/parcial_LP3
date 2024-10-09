from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.metodo_envios.MetodoEnvioDao import MetodoEnvioDao

enviapi = Blueprint('enviapi', __name__)

# Trae todos los metodo_envio
@enviapi.route('/metodo_envios', methods=['GET'])
def getMetodoEnvio():  

    envidao = MetodoEnvioDao()

    try:
        metodo_envio = envidao.getMetodoEnvio()

        return jsonify({
            'success': True,
            'data': metodo_envio,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los metodo_envio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@enviapi.route('/metodo_envios/<int:id_metodo_envio>', methods=['GET'])
def get_metodo_envio(id_metodo_envio):  
    envidao = MetodoEnvioDao()

    try:
        metodo_envio = envidao.getMetodoEnvioById(id_metodo_envio)

        if metodo_envio:
            return jsonify({
                'success': True,
                'data': metodo_envio,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el metodo_envio con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener metodo_envio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo metodo_envio
@enviapi.route('/metodo_envios', methods=['POST'])
def addMetodoEnvio():
    data = request.get_json()
    envidao = MetodoEnvioDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['meen_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        meen_descripcion = data['meen_descripcion'].upper()
        id_metodo_envio = envidao.guardarMetodoEnvio(meen_descripcion)
        if id_metodo_envio is not None:
            return jsonify({
                'success': True,
                'data': {'id_metodo_envio': id_metodo_envio, 'meen_descripcion': meen_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el metodo_envio. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar metodo_envio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@enviapi.route('/metodo_envios/<int:id_metodo_envio>', methods=['PUT'])
def updateMetodoEnvio(id_metodo_envio):
    data = request.get_json()
    envidao = MetodoEnvioDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['meen_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    meen_descripcion = data['meen_descripcion']
    try:
        if envidao.updateMetodoEnvio(id_metodo_envio, meen_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_metodo_envio': id_metodo_envio, 'meen_descripcion': meen_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el metodo_envio con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar metodo_envio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@enviapi.route('/metodo_envios/<int:id_metodo_envio>', methods=['DELETE'])
def deleteMetodoEnvio(id_metodo_envio):
    envidao = MetodoEnvioDao()

    try:
        # Usar el retorno de eliminarMetodoEnvio para determinar el éxito
        if envidao.deleteMetodoEnvio(id_metodo_envio):
            return jsonify({
                'success': True,
                'mensaje': f'metodo_envio con ID {id_metodo_envio} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el metodo_envio con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar metodo_envio: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
