# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class SucursalDao:

    def getSucursales(self):

        sucursal_SQL = """
        SELECT id_sucursal, suc_descripcion
          FROM sucursales
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(sucursal_SQL)
            # trae datos de la bd
            lista_sucursales = cur.fetchall()
            print(lista_sucursales)
            # retorno los datos
            lista_ordenada = []
            for item in lista_sucursales:
                lista_ordenada.append({
                    "id_sucursal": item[0],
                    "suc_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getSucursalById(self, id_sucursal):

        sucursal_SQL = """
        SELECT id_sucursal, suc_descripcion
        FROM sucursales WHERE id_sucursal=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(sucursal_SQL, (id_sucursal,))
            # trae datos de la bd
            sucursal_encontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id_sucursal": sucursal_encontrada[0],
                    "suc_descripcion": sucursal_encontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarSucursal(self, suc_descripcion):

        insertSucursalSQL = """
        INSERT INTO sucursales(suc_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertSucursalSQL, (suc_descripcion,))
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

    def updateSucursal(self, id_sucursal, suc_descripcion):

        updateSucursalSQL = """
        UPDATE sucursales
        SET suc_descripcion=%s
        WHERE id_sucursal=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateSucursalSQL, (suc_descripcion, id_sucursal,))
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

    def deleteSucursal(self, id_sucursal):

        deleteSucursalSQL = """
        DELETE FROM sucursales
        WHERE id_sucursal=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteSucursalSQL, (id_sucursal,))
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
