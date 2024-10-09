from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.impuestos.ImpuestoDao import ImpuestoDao

impuapi = Blueprint('impuapi', __name__)

# Trae todos los impuestos
@impuapi.route('/impuestos', methods=['GET'])
def getImpuesto():  

    impudao = ImpuestoDao()

    try:
        impuestos = impudao.getImpuesto()

        return jsonify({
            'success': True,
            'data': impuestos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los impuestos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@impuapi.route('/impuestos/<int:id_impuesto>', methods=['GET'])
def get_impuesto(id_impuesto):  
    impudao = ImpuestoDao()

    try:
        impuesto = impudao.getImpuestoById(id_impuesto)

        if impuesto:
            return jsonify({
                'success': True,
                'data': impuesto,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el impuesto con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo impuesto
@impuapi.route('/impuestos', methods=['POST'])
def addImpuesto():
    data = request.get_json()
    impudao = ImpuestoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['impu_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        impu_descripcion = data['impu_descripcion'].upper()
        id_impuesto = impudao.guardarImpuesto(impu_descripcion)
        if id_impuesto is not None:
            return jsonify({
                'success': True,
                'data': {'id_impuesto': id_impuesto, 'impu_descripcion': impu_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el impuesto. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@impuapi.route('/impuestos/<int:id_impuesto>', methods=['PUT'])
def updateImpuesto(id_impuesto):
    data = request.get_json()
    impudao = ImpuestoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['impu_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    impu_descripcion = data['impu_descripcion']
    try:
        if impudao.updateImpuesto(id_impuesto, impu_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_impuesto': id_impuesto, 'impu_descripcion': impu_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el impuesto con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@impuapi.route('/impuestos/<int:id_impuesto>', methods=['DELETE'])
def deleteImpuesto(id_impuesto):
    impudao = ImpuestoDao()

    try:
        # Usar el retorno de eliminarImpuesto para determinar el éxito
        if impudao.deleteImpuesto(id_impuesto):
            return jsonify({
                'success': True,
                'mensaje': f'Impuesto con ID {id_impuesto} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el impuesto con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar impuesto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
