# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class MetodoEnvioDao:

    def getMetodoEnvio(self):

        metodo_envio_SQL = """
        SELECT id_metodo_envio, meen_envio, meen_descripcion
          FROM metodo_envios
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(metodo_envio_SQL)
            # trae datos de la bd
            lista_metodo_envio = cur.fetchall()
            print(lista_metodo_envio)
            # retorno los datos
            lista_ordenada = []
            for item in lista_metodo_envio:
                lista_ordenada.append({
                    "id_metodo_envio": item[0],
                    "meen_envio": item[1],
                    "meen_descripcion": item[2]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getMetodoEnvioById(self, meen_envio):

        metodo_envio_SQL = """
        SELECT meen_envio, meen_descripcion
        FROM metodo_envios WHERE id_metodo_envio=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(metodo_envio_SQL, (meen_envio,))
            # trae datos de la bd
            metodo_envio_encontrado = cur.fetchone()
            # retorno los datos
            return {
                    "meen_envio": metodo_envio_encontrado[0],
                    "meen_descripcion": metodo_envio_encontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarMetodoEnvio(self, meen_descripcion):

        insertMetodoEnvioSQL = """
        INSERT INTO metodo_envios(meen_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertMetodoEnvioSQL, (meen_descripcion,))
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

    def updateMetodoEnvio(self, meen_envio, meen_descripcion):

        updateMetodoEnvioSQL = """
        UPDATE metodo_envios
        SET meen_descripcion=%s
        WHERE id_metodo_envio=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateMetodoEnvioSQL, (meen_descripcion, meen_envio,))
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

    def deleteMetodoEnvio(self, meen_envio):

        deleteMetodoEnvioSQL = """
        DELETE FROM metodo_envios
        WHERE id_metodo_envio=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteMetodoEnvioSQL, (meen_envio,))
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
