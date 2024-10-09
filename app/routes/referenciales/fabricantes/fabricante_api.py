from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.fabricantes.FabricanteDao import FabricanteDao

fabrapi = Blueprint('fabrapi', __name__)

# Trae todos los fabricante
@fabrapi.route('/fabricantes', methods=['GET'])
def getFabricante():  

    fabrdao = FabricanteDao()

    try:
        fabricantes = fabrdao.getFabricante()

        return jsonify({
            'success': True,
            'data': fabricantes,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los fabricantes: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@fabrapi.route('/fabricantes/<int:id_fabricante>', methods=['GET'])
def get_fabricante(id_fabricante):  
    fabrdao = FabricanteDao()

    try:
        fabricante = fabrdao.getFabricanteById(id_fabricante)

        if fabricante:
            return jsonify({
                'success': True,
                'data': fabricante,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el fabricante con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener fabricante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo fabricante
@fabrapi.route('/fabricantes', methods=['POST'])
def addFabricante():
    data = request.get_json()
    fabrdao = FabricanteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['fabr_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        fabr_descripcion = data['fabr_descripcion'].upper()
        id_fabricante = fabrdao.guardarFabricante(fabr_descripcion)
        if id_fabricante is not None:
            return jsonify({
                'success': True,
                'data': {'id_fabricante': id_fabricante, 'fabr_descripcion': fabr_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el fabricante. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar fabricante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@fabrapi.route('/fabricantes/<int:id_fabricante>', methods=['PUT'])
def updateFabricante(id_fabricante):
    data = request.get_json()
    fabrdao = FabricanteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['fabr_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    fabr_descripcion = data['fabr_descripcion']
    try:
        if fabrdao.updateFabricante(id_fabricante, fabr_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_fabricante': id_fabricante, 'fabr_descripcion': fabr_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el fabricante con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar fabricante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@fabrapi.route('/fabricantes/<int:id_fabricante>', methods=['DELETE'])
def deleteFabricante(id_fabricante):
    fabrdao = FabricanteDao()

    try:
        # Usar el retorno de eliminarFabricante para determinar el éxito
        if fabrdao.deleteFabricante(id_fabricante):
            return jsonify({
                'success': True,
                'mensaje': f'Fabricante con ID {id_fabricante} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el fabricante con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar fabricante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
