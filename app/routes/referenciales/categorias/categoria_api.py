from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.categorias.CategoriaDao import CategoriaDao

catapi = Blueprint('catapi', __name__)

# Trae todas las categorias
@catapi.route('/categorias', methods=['GET'])
def getCategoria():  

    catdao = CategoriaDao()

    try:
        categorias = catdao.getCategoria()

        return jsonify({
            'success': True,
            'data': categorias,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las categorias: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@catapi.route('/categorias/<int:id_categoria>', methods=['GET'])
def get_categoria(id_categoria):  
    catdao = CategoriaDao()

    try:
        categoria = catdao.getCategoriaById(id_categoria)

        if categoria:
            return jsonify({
                'success': True,
                'data': categoria,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la categoria con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener categoria: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva categoria
@catapi.route('/categorias', methods=['POST'])
def addCategoria():
    data = request.get_json()
    catdao = CategoriaDao()

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
        cat_descripcion = data['descripcion'].upper()
        id_categoria = catdao.guardarCategoria(cat_descripcion)
        if id_categoria is not None:
            return jsonify({
                'success': True,
                'data': {'id_categoria': id_categoria, 'descripcion': cat_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la categoria. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar categoria: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@catapi.route('/categorias/<int:id_categoria>', methods=['PUT'])
def updateCategoria(id_categoria):
    data = request.get_json()
    catdao = CategoriaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    cat_descripcion = data['descripcion']
    try:
        if catdao.updateCategoria(id_categoria, cat_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_categoria': id_categoria, 'descripcion': cat_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la categoria con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar categoria: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@catapi.route('/categorias/<int:id_categoria>', methods=['DELETE'])
def deleteCategoria(id_categoria):
    catdao = CategoriaDao()

    try:
        # Usar el retorno de eliminarCategoria para determinar el éxito
        if catdao.deleteCategoria(id_categoria):
            return jsonify({
                'success': True,
                'mensaje': f'Categoria con ID {id_categoria} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la categoria con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar categoria: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500


