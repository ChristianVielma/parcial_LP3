# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProductoDao:

    def getProductos(self):

        producto_SQL = """
        SELECT id_producto, prod_descripcion
          FROM productos
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(producto_SQL)
            # trae datos de la bd
            lista_productos = cur.fetchall()
            print(lista_productos)
            # retorno los datos
            lista_ordenada = []
            for item in lista_productos:
                lista_ordenada.append({
                    "id_producto": item[0],
                    "prod_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getProductoById(self, id_producto):

        producto_SQL = """
        SELECT id_producto, prod_descripcion
        FROM productos WHERE id_producto=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(producto_SQL, (id_producto,))
            # trae datos de la bd
            producto_encontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id_producto": producto_encontrado[0],
                    "prod_descripcion": producto_encontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarProducto(self, prod_descripcion):

        insertProductoSQL = """
        INSERT INTO productos(prod_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertProductoSQL, (prod_descripcion,))
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

    def updateProducto(self, id_producto, prod_descripcion):

        updateProductoSQL = """
        UPDATE productos
        SET prod_descripcion=%s
        WHERE id_producto=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateProductoSQL, (prod_descripcion, id_producto,))
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

    def deleteProducto(self, id_producto):

        deleteProductoSQL = """
        DELETE FROM productos
        WHERE id_producto=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteProductoSQL, (id_producto,))
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
