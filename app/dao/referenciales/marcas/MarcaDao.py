# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class MarcaDao:

    def getMarca(self):

        marcaSQL = """
        SELECT id_marca, marc_descripcion
          FROM marcas
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(marcaSQL)
            # trae datos de la bd
            lista_marcas = cur.fetchall()
            print(lista_marcas)
            # retorno los datos
            lista_ordenada = []
            for item in lista_marcas:
                lista_ordenada.append({
                    "id_marca": item[0],
                    "marc_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getMarcaById(self, id_marca):

        marcaSQL = """
        SELECT id_marca, marc_descripcion
        FROM marcas WHERE id_marca=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(marcaSQL, (id_marca,))
            # trae datos de la bd
            marcaEncontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id_marca": marcaEncontrada[0],
                    "marc_descripcion": marcaEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarMarca(self, marc_descripcion):

        insertMarcaSQL = """
        INSERT INTO marcas(marc_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertMarcaSQL, (marc_descripcion,))
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

    def updateMarca(self, id_marca, marc_descripcion):

        updateMarcaSQL = """
        UPDATE marcas
        SET marc_descripcion=%s
        WHERE id_marca=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateMarcaSQL, (marc_descripcion, id_marca,))
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

    def deleteMarca(self, id_marca):

        deleteMarcaSQL = """
        DELETE FROM marcas
        WHERE id_marca=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteMarcaSQL, (id_marca,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se
