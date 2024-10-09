# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProveedorDao:

    def getProveedores(self):

        proveedor_SQL = """
        SELECT id_proveedor, prov_descripcion
          FROM proveedores
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(proveedor_SQL)
            # trae datos de la bd
            lista_proveedores = cur.fetchall()
            print(lista_proveedores)
            # retorno los datos
            lista_ordenada = []
            for item in lista_proveedores:
                lista_ordenada.append({
                    "id_proveedor": item[0],
                    "prov_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getProveedorById(self, id_proveedor):

        proveedor_SQL = """
        SELECT id_proveedor, prov_descripcion
        FROM proveedores WHERE id_proveedor=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(proveedor_SQL, (id_proveedor,))
            # trae datos de la bd
            proveedor_encontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id_proveedor": proveedor_encontrado[0],
                    "prov_descripcion": proveedor_encontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarProveedor(self, prov_descripcion):

        insertProveedorSQL = """
        INSERT INTO proveedores(prov_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertProveedorSQL, (prov_descripcion,))
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

    def updateProveedor(self, id_proveedor, prov_descripcion):

        updateProveedorSQL = """
        UPDATE proveedores
        SET prov_descripcion=%s
        WHERE id_proveedor=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateProveedorSQL, (prov_descripcion, id_proveedor,))
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

    def deleteProveedor(self, id_proveedor):

        deleteProveedorSQL = """
        DELETE FROM proveedores
        WHERE id_proveedor=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteProveedorSQL, (id_proveedor,))
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
