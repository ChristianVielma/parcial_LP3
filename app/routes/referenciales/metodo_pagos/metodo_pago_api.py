from flask import Blueprint, request, jsonify, current_app as app  
from app.dao.referenciales.metodo_pagos.MetodoPagoDao import MetodoPagoDao  

pagoapi = Blueprint('pagoapi', __name__)  

# Trae todos los metodo_pago  
@pagoapi.route('/metodo_pagos', methods=['GET'])  
def getMetodoPago():  
    pagodao = MetodoPagoDao()  

    try:  
        metodo_pago = pagodao.getMetodoPago()  

        return jsonify({  
            'success': True,  
            'data': metodo_pago,  
            'error': None  
        }), 200  

    except Exception as e:  
        app.logger.error(f"Error al obtener todos los metodo_pago: {str(e)}")  
        return jsonify({  
            'success': False,  
            'error': 'Ocurrió un error interno. Consulte con el administrador.'  
        }), 500  

@pagoapi.route('/metodo_pagos/<int:id_metodo_pago>', methods=['GET'])  
def get_metodo_pago(id_metodo_pago):  
    pagodao = MetodoPagoDao()  

    try:  
        metodo_pago = pagodao.getMetodoPagoById(id_metodo_pago)  

        if metodo_pago:  
            return jsonify({  
                'success': True,  
                'data': metodo_pago,  
                'error': None  
            }), 200  
        else:  
            return jsonify({  
                'success': False,  
                'error': 'No se encontró el metodo_pago con el ID proporcionado.'  
            }), 404  

    except Exception as e:  
        app.logger.error(f"Error al obtener metodo_pago: {str(e)}")  
        return jsonify({  
            'success': False,  
            'error': 'Ocurrió un error interno. Consulte con el administrador.'  
        }), 500  

# Agrega un nuevo metodo_pago  
@pagoapi.route('/metodo_pagos', methods=['POST'])  
def addMetodoPago():  
    data = request.get_json()  
    pagodao = MetodoPagoDao()  

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias  
    campos_requeridos = ['mepa_descripcion']  

    # Verificar si faltan campos o son vacíos  
    for campo in campos_requeridos:  
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:  
            return jsonify({  
                            'success': False,  
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'  
                            }), 400  

    try:  
        mepa_descripcion = data['mepa_descripcion'].upper()  
        id_metodo_pago = pagodao.guardarMetodoPago(mepa_descripcion)  
        if id_metodo_pago is not None:  
            return jsonify({  
                'success': True,  
                'data': {'id_metodo_pago': id_metodo_pago, 'mepa_descripcion': mepa_descripcion},  
                'error': None  
            }), 201  
        else:  
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el metodo_pago. Consulte con el administrador.' }), 500  
    except Exception as e:  
        app.logger.error(f"Error al agregar metodo_pago: {str(e)}")  
        return jsonify({  
            'success': False,  
            'error': 'Ocurrió un error interno. Consulte con el administrador.'  
        }), 500  

@pagoapi.route('/metodo_pagos/<int:id_metodo_pago>', methods=['PUT'])  
def updateMetodoPago(id_metodo_pago):  
    data = request.get_json()  
    pagodao = MetodoPagoDao()  

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias  
    campos_requeridos = ['mepa_descripcion']  

    # Verificar si faltan campos o son vacíos  
    for campo in campos_requeridos:  
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:  
            return jsonify({  
                            'success': False,  
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'  
                            }), 400  
    mepa_descripcion = data['mepa_descripcion']  
    try:  
        if pagodao.updateMetodoPago(id_metodo_pago, mepa_descripcion.upper()):  
            return jsonify({  
                'success': True,  
                'data': {'id_metodo_pago': id_metodo_pago, 'mepa_descripcion': mepa_descripcion},  
                'error': None  
            }), 200  
        else:  
            return jsonify({  
                'success': False,  
                'error': 'No se encontró el metodo_pago con el ID proporcionado o no se pudo actualizar.'  
            }), 404  
    except Exception as e:  
        app.logger.error(f"Error al actualizar metodo_pago: {str(e)}")  
        return jsonify({  
            'success': False,  
            'error': 'Ocurrió un error interno. Consulte con el administrador.'  
        }), 500  

@pagoapi.route('/metodo_pagos/<int:id_metodo_pago>', methods=['DELETE'])  
def deleteMetodoPago(id_metodo_pago):  
    pagodao = MetodoPagoDao()  

    try:  
        # Usar el retorno de eliminarMetodoPago para determinar el éxito  
        if pagodao.deleteMetodoPago(id_metodo_pago):  
            return jsonify({  
                'success': True,  
                'mensaje': f'metodo_pago con ID {id_metodo_pago} eliminado correctamente.',  
                'error': None  
            }), 200  
        else:  
            return jsonify({  
                'success': False,  
                'error': 'No se encontró el metodo_pago con el ID proporcionado o no se pudo eliminar.'  
            }), 404  

    except Exception as e:  
        app.logger.error(f"Error al eliminar metodo_pago: {str(e)}")  
        return jsonify({  
            'success': False,  
            'error': 'Ocurrió un error interno. Consulte con el administrador.'  
        }), 500