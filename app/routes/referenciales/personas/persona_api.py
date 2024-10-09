from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.personas.PersonaDao import PersonaDao

personaapi = Blueprint('personaapi', __name__)

# Trae todas las personas
@personaapi.route('/personas', methods=['GET'])
def getPersona():  

    personadao = PersonaDao()

    try:
        personas = personadao.getPersona()

        return jsonify({
            'success': True,
            'data': personas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las personas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@personaapi.route('/personas/<int:id_persona>', methods=['GET'])
def get_persona(id_persona):  
    personadao = PersonaDao()

    try:
        persona = personadao.getPersonaById(id_persona)

        if persona:
            return jsonify({
                'success': True,
                'data': persona,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva persona
@personaapi.route('/personas', methods=['POST'])
def addPersona():
    data = request.get_json()
    personadao = PersonaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_persona = data['nombre'].upper()
        id_persona = personadao.guardarPersona(nombre_persona)
        if id_persona is not None:
            return jsonify({
                'success': True,
                'data': {'id_persona': id_persona, 'nombre': nombre_persona},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la persona. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@personaapi.route('/personas/<int:id_persona>', methods=['PUT'])
def updatePersona(id_persona):
    data = request.get_json()
    personadao = PersonaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    nombre_persona = data['nombre']
    try:
        if personadao.updatePersona(id_persona, nombre_persona.upper()):
            return jsonify({
                'success': True,
                'data': {'id_persona': id_persona, 'nombre': nombre_persona},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@personaapi.route('/personas/<int:id_persona>', methods=['DELETE'])
def deletePersona(id_persona):
    personadao = PersonaDao()

    try:
        # Usar el retorno de eliminarPersona para determinar el éxito
        if personadao.deletePersona(id_persona):
            return jsonify({
                'success': True,
                'mensaje': f'Persona con ID {id_persona} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
