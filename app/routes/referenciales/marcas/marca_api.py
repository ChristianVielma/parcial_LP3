from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.marcas.MarcaDao import MarcaDao

marcapi = Blueprint('marcapi', __name__)

# Trae todos los marcas
@marcapi.route('/marcas', methods=['GET'])
def getMarca():  

    marcdao = MarcaDao()

    try:
        marcas = marcdao.getMarca()

        return jsonify({
            'success': True,
            'data': marcas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los marcas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@marcapi.route('/marcas/<int:id_marca>', methods=['GET'])
def get_marca(id_marca):  
    marcdao = MarcaDao()

    try:
        marca = marcdao.getMarcaById(id_marca)

        if marca:
            return jsonify({
                'success': True,
                'data': marca,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el marca con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener marca: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo marca
@marcapi.route('/marcas', methods=['POST'])
def addMarca():
    data = request.get_json()
    marcdao = MarcaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['marc_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        marc_descripcion = data['marc_descripcion'].upper()
        id_marca = marcdao.guardarMarca(marc_descripcion)
        if id_marca is not None:
            return jsonify({
                'success': True,
                'data': {'id_marca': id_marca, 'marc_descripcion': marc_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el marca. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar marca: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@marcapi.route('/marcas/<int:id_marca>', methods=['PUT'])
def updateMarca(id_marca):
    data = request.get_json()
    marcdao = MarcaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['marc_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    marc_descripcion = data['marc_descripcion']
    try:
        if marcdao.updateMarca(id_marca, marc_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_marca': id_marca, 'marc_descripcion': marc_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el Marca con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar Marca: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@marcapi.route('/marcas/<int:id_marca>', methods=['DELETE'])
def deleteMarca(id_marca):
    marcdao = MarcaDao()

    try:
        # Usar el retorno de eliminarMarca para determinar el éxito
        if marcdao.deleteMarca(id_marca):
            return jsonify({
                'success': True,
                'mensaje': f'Marca con ID {id_marca} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el Marca con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar Marca: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
