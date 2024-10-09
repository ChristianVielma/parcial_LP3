from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.empleados.EmpleadosDao import EmpleadoDao

empapi = Blueprint('empapi', __name__)

# Trae todos los empleados
@empapi.route('/empleados', methods=['GET'])
def getEmpleado():  

    empdao = EmpleadoDao()

    try:
        empleados = empdao.getEmpleado()

        return jsonify({
            'success': True,
            'data': empleados,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los empleados: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@empapi.route('/empleados/<int:id_empleado>', methods=['GET'])
def get_empleado(id_empleado):  
    empdao = EmpleadoDao()

    try:
        empleado = empdao.getEmpleadoById(id_empleado)

        if empleado:
            return jsonify({
                'success': True,
                'data': empleado,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el empleado con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo empleado
@empapi.route('/empleados', methods=['POST'])
def addEmpleado():
    data = request.get_json()
    empdao = EmpleadoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['emp_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        emp_descripcion = data['emp_descripcion'].upper()
        id_empleado = empdao.guardarEmpleado(emp_descripcion)
        if id_empleado is not None:
            return jsonify({
                'success': True,
                'data': {'id_empleado': id_empleado, 'emp_descripcion': emp_descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el empleado. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@empapi.route('/empleados/<int:id_empleado>', methods=['PUT'])
def updateEmpleado(id_empleado):
    data = request.get_json()
    empdao = EmpleadoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['emp_descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    emp_descripcion = data['emp_descripcion']
    try:
        if empdao.updateEmpleado(id_empleado, emp_descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id_empleado': id_empleado, 'emp_descripcion': emp_descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el empleado con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@empapi.route('/empleados/<int:id_empleado>', methods=['DELETE'])
def deleteEmpleado(id_empleado):
    empdao = EmpleadoDao()

    try:
        # Usar el retorno de eliminarEmpleado para determinar el éxito
        if empdao.deleteEmpleado(id_empleado):
            return jsonify({
                'success': True,
                'mensaje': f'Empleado con ID {id_empleado} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el empleado con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar empleado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
