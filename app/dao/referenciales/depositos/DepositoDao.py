# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class DepositoDao:

    def getDeposito(self):

        depositoSQL = """
        select id_deposito, depo_descripcion
          from depositos 
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(depositoSQL)
            # trae datos de la bd
            lista_depositos = cur.fetchall()
            print(lista_depositos)
            # retorno los datos
            lista_ordenada = []
            for item in lista_depositos:
                lista_ordenada.append({
                    "id_deposito": item[0],
                    "depo_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getDepositoById(self, id_deposito):

        depositoSQL = """
        SELECT id_deposito, depo_descripcion
        FROM depositos WHERE id_deposito=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(depositoSQL, (id_deposito,))
            # trae datos de la bd
            depositoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id_deposito": depositoEncontrado[0],
                    "depo_descripcion": depositoEncontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarDeposito(self, depo_descripcion):

        insertDepositoSQL = """
        INSERT INTO depositos(depo_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertDepositoSQL, (depo_descripcion,))
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

    def updateDeposito(self, id_deposito, depo_descripcion):

        updateDepositoSQL = """
        UPDATE depositos
        SET depo_descripcion=%s
        WHERE id_deposito=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateDepositoSQL, (depo_descripcion, id_deposito,))
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

    def deleteDeposito(self, id_deposito):

        deleteDepositoSQL = """
        DELETE FROM depositos
        WHERE id_deposito=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteDepositoSQL, (id_deposito,))
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
