# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonaDao:

    def getPersona(self):

        persona_SQL = """
        SELECT id_persona, pers_descripcion
          FROM personas
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(persona_SQL)
            # trae datos de la bd
            lista_personas = cur.fetchall()
            print(lista_personas)
            # retorno los datos
            lista_ordenada = []
            for item in lista_personas:
                lista_ordenada.append({
                    "id_persona": item[0],
                    "pers_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getPersonaById(self, id_persona):

        persona_SQL = """
        SELECT id_persona, pers_descripcion
        FROM personas WHERE id_persona=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(persona_SQL, (id_persona,))
            # trae datos de la bd
            persona_encontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id_persona": persona_encontrada[0],
                    "pers_descripcion": persona_encontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarPersona(self, pers_descripcion):

        insertPersonaSQL = """
        INSERT INTO personas(pers_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPersonaSQL, (pers_descripcion,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def updatePersona(self, id_persona, pers_descripcion):

        updatePersonaSQL = """
        UPDATE personas
        SET pers_descripcion=%s
        WHERE id_persona=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updatePersonaSQL, (pers_descripcion, id_persona,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def deletePersona(self, id_persona):

        deletePersonaSQL = """
        DELETE FROM personas
        WHERE id_persona=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deletePersonaSQL, (id_persona,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False
