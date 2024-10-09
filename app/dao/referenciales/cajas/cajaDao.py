# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CajasDao:

    def getCajas(self):

        cajaSQL = """
        select id_caja, monto_apertura
          from cajas 
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cajaSQL)
            # trae datos de la bd
            lista_cajas = cur.fetchall()
            print(lista_cajas)
            # retorno los datos
            lista_ordenada = []
            for item in lista_cajas:
                lista_ordenada.append({
                    "id_caja": item[0],
                    "monto_apertura": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getCajasById(self, id_caja):

        cajaSQL = """
        SELECT id_caja, monto_apertura
        FROM cajas WHERE id_caja=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cajaSQL, (id_caja,))
            # trae datos de la bd
            cajaEncontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id_caja": cajaEncontrada[0],
                    "monto_apertura": cajaEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarCaja(self, monto_apertura):

        insertCajaSQL = """
        INSERT INTO cajas(monto_apertura) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCajaSQL, (monto_apertura,))
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

    def updateCaja(self,id_caja, monto_apertura):

        updateCajaSQL = """
        UPDATE cajas
        SET monto_apertura=%s
        WHERE id_caja=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateCajaSQL, (monto_apertura, id_caja,))
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

    def deleteCaja(self, id_caja):

        deleteCajaSQL = """
        DELETE FROM cajas
        WHERE id_caja=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteCajaSQL, (id_caja,))
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
    
