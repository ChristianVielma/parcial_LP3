# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class MetodoPagoDao:

    def getMetodoPago(self):

        metodo_pago_SQL = """
        SELECT id_metodo_pago, mepa_descripcion
          FROM metodo_pagos
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(metodo_pago_SQL)
            # trae datos de la bd
            lista_metodo_pago = cur.fetchall()
            print(lista_metodo_pago)
            # retorno los datos
            lista_ordenada = []
            for item in lista_metodo_pago:
                lista_ordenada.append({
                    "id_metodo_pago": item[0],
                    "mepa_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getMetodoPagoById(self, id_metodo_pago):

        metodo_pago_SQL = """
        SELECT mepa_descripcion
        FROM metodo_pagos WHERE id_metodo_pago=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(metodo_pago_SQL, (id_metodo_pago,))
            # trae datos de la bd
            metodo_pago_encontrado = cur.fetchone()
            # retorno los datos
            return {
                    "mepa_descripcion": metodo_pago_encontrado[0]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarMetodoPago(self, mepa_descripcion):

        insertMetodoPagoSQL = """
        INSERT INTO metodo_pagos(mepa_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertMetodoPagoSQL, (mepa_descripcion,))
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

    def updateMetodoPago(self, id_metodo_pago, mepa_descripcion):

        updateMetodoPagoSQL = """
        UPDATE metodo_pagos
        SET mepa_descripcion=%s
        WHERE id_metodo_pago=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateMetodoPagoSQL, (mepa_descripcion, id_metodo_pago,))
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

    def deleteMetodoPago(self, id_metodo_pago):

        deleteMetodoPagoSQL = """
        DELETE FROM metodo_pagos
        WHERE id_metodo_pago=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteMetodoPagoSQL, (id_metodo_pago,))
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
