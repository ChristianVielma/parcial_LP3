# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class EmpleadoDao:

    def getEmpleado(self):

        empleadoSQL = """
        select id_empleado, emp_descripcion
          from empleados 
        """ 
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(empleadoSQL)
            # trae datos de la bd
            lista_empleados = cur.fetchall()
            print(lista_empleados)
            # retorno los datos
            lista_ordenada = []
            for item in lista_empleados:
                lista_ordenada.append({
                    "id_empleado": item[0],
                    "emp_descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getEmpleadoById(self, id_empleado):

        empleadoSQL = """
        SELECT id_empleado, emp_descripcion
        FROM empleados WHERE id_empleado=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(empleadoSQL, (id_empleado,))
            # trae datos de la bd
            empleadoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                    "id_empleado": empleadoEncontrado[0],
                    "emp_descripcion": empleadoEncontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarEmpleado(self, emp_descripcion):

        insertEmpleadoSQL = """
        INSERT INTO empleados(emp_descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertEmpleadoSQL, (emp_descripcion,))
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

    def updateEmpleado(self, id_empleado, emp_descripcion):

        updateEmpleadoSQL = """
        UPDATE empleados
        SET emp_descripcion=%s
        WHERE id_empleado=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateEmpleadoSQL, (emp_descripcion, id_empleado,))
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

    def deleteEmpleado(self, id_empleado):

        deleteEmpleadoSQL = """
        DELETE FROM empleados
        WHERE id_empleado=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteEmpleadoSQL, (id_empleado,))
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
