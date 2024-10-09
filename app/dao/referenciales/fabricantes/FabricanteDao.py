# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class FabricanteDao:

    def getFabricante(self):

        fabricanteSQL = """
        select id_fabricante, fabr_descripcion
          from fabricantes 
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(fabricanteSQL)
            # trae datos de la bd
            lista_fabricantes = cur.fetchall()
            print(lista_fabricantes)
            # retorno los datos
            lista_ordenada = []
            for item in lista_fabricantes:
                lista_ordenada.append({
                    "id_fabricante": item[0],
                    "fabr_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getFabricanteById(self, id_fabricante):

        fabricanteSQL = """
        SELECT id_fabricante, fabr_descripcion
        FROM fabricantes WHERE id_fabricante=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(fabricanteSQL, (id_fabricante,))
            # trae datos de la bd
            fabricanteEncontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id_fabricante": fabricanteEncontrado[0],
                    "fabr_descripcion": fabricanteEncontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarFabricante(self, fabr_descripcion):

        insertFabricanteSQL = """
        INSERT INTO fabricantes(fabr_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertFabricanteSQL, (fabr_descripcion,))
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

    def updateFabricante(self, id_fabricante, fabr_descripcion):

        updateFabricanteSQL = """
        UPDATE fabricantes
        SET fabr_descripcion=%s
        WHERE id_fabricante=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateFabricanteSQL, (fabr_descripcion, id_fabricante,))
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

    def deleteFabricante(self, id_fabricante):

        deleteFabricanteSQL = """
        DELETE FROM fabricantes
        WHERE id_fabricante=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteFabricanteSQL, (id_fabricante,))
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
