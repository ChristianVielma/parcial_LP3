# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class DescuentoDao:

    def getDescuento(self):

        descuentoSQL = """
        select id_descuento, desc_descripcion
          from descuentos 
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(descuentoSQL)
            # trae datos de la bd
            lista_descuentos = cur.fetchall()
            print(lista_descuentos)
            # retorno los datos
            lista_ordenada = []
            for item in lista_descuentos:
                lista_ordenada.append({
                    "id_descuento": item[0],
                    "desc_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getDescuentoById(self, id_descuento):

        descuentoSQL = """
        SELECT id_descuento, desc_descripcion
        FROM descuentos WHERE id_descuento=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(descuentoSQL, (id_descuento,))
            # trae datos de la bd
            descuentoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id_descuento": descuentoEncontrado[0],
                    "desc_descripcion": descuentoEncontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarDescuento(self, desc_descripcion):

        insertDescuentoSQL = """
        INSERT INTO descuentos(desc_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertDescuentoSQL, (desc_descripcion,))
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

    def updateDescuento(self, id_descuento, desc_descripcion):

        updateDescuentoSQL = """
        UPDATE descuentos
        SET desc_descripcion=%s
        WHERE id_descuento=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateDescuentoSQL, (desc_descripcion, id_descuento,))
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

    def deleteDescuento(self, id_descuento):

        deleteDescuentoSQL = """
        DELETE FROM descuentos
        WHERE id_descuento=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteDescuentoSQL, (id_descuento,))
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
