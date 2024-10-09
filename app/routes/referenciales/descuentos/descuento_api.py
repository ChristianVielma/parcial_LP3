from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.descuentos.DescuentoDao import DescuentoDao

descapi = Blueprint('descapi', __name__)

# Trae todos los descuentos
@descapi.route('/descuentos', methods=['GET'])
def getDescuento():  

    descdao = DescuentoDao()

    try:
        descuentos = descdao.getDescuento()

        return jsonify({
            'success': True,
            'data': descuentos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los descuentos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@descapi.route('/descuentos/<int:id_descuento>', methods=['GET'])
def get_descuento(id_descuento):  
    descdao = DescuentoDao()

    try:
        descuento = descdao.getDescuentoById(id_descuento)

        if descuento:
            return jsonify({
                'success': True,
                'data': descuento,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el descuento con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo descuento
@descapi.route('/descuentos', methods=['POST'])
def addDescuento():
    data = request.get_json()
    descdao = DescuentoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['desc_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        desc_descripcion = data['desc_descripcion'].upper()
        id_descuento = descdao.guardarDescuento(desc_descripcion)
        if id_descuento is not None:
            return jsonify({
                'success': True,
                'data': {'id_descuento': id_descuento, 'desc_descripcion': desc_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el descuento. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@descapi.route('/descuentos/<int:id_descuento>', methods=['PUT'])
def updateDescuento(id_descuento):
    data = request.get_json()
    descdao = DescuentoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['desc_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    desc_descripcion = data['desc_descripcion']
    try:
        if descdao.updateDescuento(id_descuento, desc_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_descuento': id_descuento, 'desc_descripcion': desc_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el descuento con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@descapi.route('/descuentos/<int:id_descuento>', methods=['DELETE'])
def deleteDescuento(id_descuento):
    descdao = DescuentoDao()

    try:
        # Usar el retorno de eliminardescuento para determinar el éxito
        if descdao.deleteDescuento(id_descuento):
            return jsonify({
                'success': True,
                'mensaje': f'descuento con ID {id_descuento} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el descuento con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar descuento: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
