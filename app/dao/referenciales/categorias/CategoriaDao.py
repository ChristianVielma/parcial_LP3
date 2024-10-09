# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CategoriaDao:

    def getCategoria(self):

        categoriaSQL = """
        select id_categoria, upper(cat_descripcion) as cat_descripcion
          from categorias 
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(categoriaSQL)
            # trae datos de la bd
            lista_categorias = cur.fetchall()
            print(lista_categorias)
            # retorno los datos
            lista_ordenada = []
            for item in lista_categorias:
                lista_ordenada.append({
                    "id_categoria": item[0],
                    "cat_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getCategoriaById(self, id_categoria):

        categoriaSQL = """
        SELECT id_categoria, cat_descripcion
        FROM categorias WHERE id_categoria=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(categoriaSQL, (id_categoria,))
            # trae datos de la bd
            categoriaEncontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id_categoria": categoriaEncontrada[0],
                    "cat_descripcion": categoriaEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarCategoria(self, cat_descripcion):

        insertCategoriaSQL = """
        INSERT INTO categorias(cat_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCategoriaSQL, (cat_descripcion,))
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

    def updateCategoria(self, id_categoria, cat_descripcion):

        updateCategoriaSQL = """
        UPDATE categorias
        SET cat_descripcion=%s
        WHERE id_categoria=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateCategoriaSQL, (cat_descripcion, id_categoria,))
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

    def deleteCategoria(self, id_categoria):

        deleteCategoriaSQL = """
        DELETE FROM categorias
        WHERE id_categoria=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteCategoriaSQL, (id_categoria,))
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
    
