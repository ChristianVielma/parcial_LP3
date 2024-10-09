# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ExistenciaDao:

    def getExistencia(self):

        existenciaSQL = """
                select id_producto
                      ,prod_descripcion 
                      ,exis_cantidad 
                  from existencias e 
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(existenciaSQL)
            # trae datos de la bd
            lista_existencias = cur.fetchall()
            print(lista_existencias)
            # retorno los datos
            lista_ordenada = []
            for item in lista_existencias:
                lista_ordenada.append({
                    "id_producto": item[0],
                    "prod_descripcion": item[1],
                    "exis_cantidad": item[2]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getExistenciaById(self, id_producto):

        existenciaSQL = """
                select prod_descripcion 
                      ,exis_cantidad 
                  from existencias
                WHERE id_producto=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(existenciaSQL, (id_producto,))
            # trae datos de la bd
            existenciaEncontrada = cur.fetchone()
            # retorno los datos
            return {
                    "prod_descripcion": existenciaEncontrada[0],
                    "exis_cantidad": existenciaEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    # def guardarExistencia(self, exis_descripcion):

    #     insertExistenciaSQL = """
    #     INSERT INTO existencias(exis_descripcion) VALUES(%s)
    #     """

    #     conexion = Conexion()
    #     con = conexion.getConexion()
    #     cur = con.cursor()

    #     # Ejecucion exitosa
    #     try:
    #         cur.execute(insertExistenciaSQL, (exis_descripcion,))
    #         # se confirma la insercion
    #         con.commit()

    #         return True

    #     # Si algo fallo entra aqui
    #     except con.Error as e:
    #         app.logger.info(e)

    #     # Siempre se va ejecutar
    #     finally:
    #         cur.close()
    #         con.close()

    #     return False

    def updateExistencia(self, id_producto, exis_cantidad):

        updateExistenciaSQL = """
        UPDATE existencias
        SET exis_cantidad=%s
        WHERE id_producto=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateExistenciaSQL, (exis_cantidad, id_producto,))
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

    def deleteExistencia(self, id_producto):

        deleteExistenciaSQL = """
        DELETE FROM existencias
        WHERE id_producto=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteExistenciaSQL, (id_producto,))
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
