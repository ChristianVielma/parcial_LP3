# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ImpuestoDao:

    def getImpuesto(self):

        impuestoSQL = """
        SELECT id_impuesto, impu_descripcion
          FROM impuestos
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(impuestoSQL)
            # trae datos de la bd
            lista_impuestos = cur.fetchall()
            print(lista_impuestos)
            # retorno los datos
            lista_ordenada = []
            for item in lista_impuestos:
                lista_ordenada.append({
                    "id_impuesto": item[0],
                    "impu_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getImpuestoById(self, id_impuesto):

        impuestoSQL = """
        SELECT id_impuesto, impu_descripcion
        FROM impuestos WHERE id_impuesto=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(impuestoSQL, (id_impuesto,))
            # trae datos de la bd
            impuestoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id_impuesto": impuestoEncontrado[0],
                    "impu_descripcion": impuestoEncontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarImpuesto(self, impu_descripcion):

        insertImpuestoSQL = """
        INSERT INTO impuestos(impu_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertImpuestoSQL, (impu_descripcion,))
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

    def updateImpuesto(self, id_impuesto, impu_descripcion):

        updateImpuestoSQL = """
        UPDATE impuestos
        SET impu_descripcion=%s
        WHERE id_impuesto=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateImpuestoSQL, (impu_descripcion, id_impuesto,))
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

    def deleteImpuesto(self, id_impuesto):

        deleteImpuestoSQL = """
        DELETE FROM impuestos
        WHERE id_impuesto=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteImpuestoSQL, (id_impuesto,))
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
