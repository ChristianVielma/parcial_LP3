from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.productos.ProductoDao import ProductoDao

productoapi = Blueprint('productoapi', __name__)

# Trae todos los productos
@productoapi.route('/productos', methods=['GET'])
def getProductos():  
    productodao = ProductoDao()

    try:
        productos = productodao.getProductos()

        return jsonify({
            'success': True,
            'data': productos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los productos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@productoapi.route('/productos/<int:id_producto>', methods=['GET'])
def get_producto(id_producto):  
    productodao = ProductoDao()

    try:
        producto = productodao.getProductoById(id_producto)

        if producto:
            return jsonify({
                'success': True,
                'data': producto,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el producto con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo producto
@productoapi.route('/productos', methods=['POST'])
def addProducto():
    data = request.get_json()
    productodao = ProductoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['prod_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_producto = data['prod_descripcion'].upper()
        id_producto = productodao.guardarProducto(nombre_producto)
        if id_producto is not None:
            return jsonify({
                'success': True,
                'data': {'id_producto': id_producto, 'prod_descripcion': nombre_producto},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el producto. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@productoapi.route('/productos/<int:id_producto>', methods=['PUT'])
def updateProducto(id_producto):
    data = request.get_json()
    productodao = ProductoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['prod_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    nombre_producto = data['prod_descripcion']
    try:
        if productodao.updateProducto(id_producto, nombre_producto.upper()):
            return jsonify({
                'success': True,
                'data': {'id_producto': id_producto, 'prod_descripcion': nombre_producto},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el producto con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@productoapi.route('/productos/<int:id_producto>', methods=['DELETE'])
def deleteProducto(id_producto):
    productodao = ProductoDao()

    try:
        # Usar el retorno de eliminarProducto para determinar el éxito
        if productodao.deleteProducto(id_producto):
            return jsonify({
                'success': True,
                'mensaje': f'Producto con ID {id_producto} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el producto con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
