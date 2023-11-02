import mysql.connector

def ConectarDB():
    # Código para establecer una conexión a la base de datos
    try:
        # Configura la conexión a la base de datos, cambiar los datos segun la base de datos que estes usando
        config = {
            'user': 'root',
            'password': '123456',
            'host': 'localhost',
            'database': 'datos'
        }

        # Establece la conexión
        conn = mysql.connector.connect(**config)

        # Si la conexión es exitosa, devuelve la conexión
        return conn

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def insert(dia,motivo,monto):
    # Código para insertar datos en la base de datos
    try:
        conn = ConectarDB()
        cursor = conn.cursor()

        # Sentencia SQL para insertar datos en la tabla
        sql = "INSERT INTO registros_contables (dia, motivo, monto) VALUES (%s, %s, %s)"
        values = (dia,monto,motivo)
        # Ejecuta la sentencia SQL
        cursor.execute(sql, values)

        # Confirma la transacción
        conn.commit()

        print("Datos insertados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")

    finally:
        cursor.close()
        conn.close()

def insertar(motivo):
    # Código para insertar datos en la base de datos
    try:
        conn = ConectarDB()
        cursor = conn.cursor()

        # Sentencia SQL para insertar datos en la tabla
        sql = "INSERT INTO motivos (motivo) VALUES (%s)"
        values = (motivo,)
        # Ejecuta la sentencia SQL
        cursor.execute(sql, values)

        # Confirma la transacción
        conn.commit()

        print("Datos insertados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")

    finally:
        cursor.close()
        conn.close()

    
def EliminarDatos(dia, motivo, monto):
    # Código para eliminar datos de la base de datos
    try:
        conn = ConectarDB()
        cursor = conn.cursor()

        # Sentencia SQL para eliminar datos de la tabla
        sql = "DELETE FROM registros_contables WHERE dia = %s AND motivo = %s AND monto = %s"
        values = (dia, monto, motivo)

        # Ejecuta la sentencia SQL
        cursor.execute(sql, values)

        # Confirma la transacción
        conn.commit()

        print("Datos eliminados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al eliminar datos: {err}")

    finally:
        cursor.close()
        conn.close()

def InsertarTabla(treeview, mes_seleccionado, year_seleccionado):
    conn = ConectarDB()
    cursor = conn.cursor()

    # Realizar una consulta SQL para obtener los datos de la tabla
    #cursor.execute("SELECT dia, motivo, monto FROM registros_contables")

    # Realizar una consulta SQL para obtener los datos del mes seleccionado
    sql = "SELECT id, dia, motivo, monto FROM registros_contables WHERE YEAR(dia) = %s AND MONTH(dia) = %s"
    cursor.execute(sql, (year_seleccionado, mes_seleccionado))

     # Iterar sobre los resultados y agregarlos al Treeview
    for row in cursor.fetchall():
        treeview.insert("", "end", values=row)

    # Cerrar la conexión a la base de datos
    conn.close()

def InsertarTablaCompleta(tree, year):
    conn = ConectarDB()
    cursor = conn.cursor()

    sql = "SELECT id, dia, motivo, monto FROM registros_contables WHERE YEAR(dia) = %s"
    cursor.execute(sql,(year,))

    for row in cursor.fetchall():
        tree.insert("", "end", values = row)
    
    conn.close()

def ObtenerValoresDesdeDB():
    conn = ConectarDB()
    cursor = conn.cursor()

    cursor.execute("SELECT motivo FROM motivos;")  # Reemplaza con tu consulta SQL

    valores = [row[0] for row in cursor.fetchall()]

    conn.close()
    return valores

def EliminarDato(id):
    conn = ConectarDB()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM registros_contables WHERE id = %s"
        cursor.execute(sql,(id,))

        conn.commit()
        print(f"Registro con ID {id} eliminado correctamente.")
    
    except mysql.connector.Error as e:
        print(f"Error al eliminar el registro: {e}")

    finally:
        cursor.close()
        conn.close()
    
def SumarMontos(mes,year):
    conn = ConectarDB()
    cursor = conn.cursor()

    if mes == "0":
        sql = "SELECT SUM(monto) from registros_contables WHERE YEAR(dia) = %s"
        cursor.execute(sql,(year,))
    else:
        sql = "SELECT SUM(monto) FROM registros_contables WHERE MONTH(dia) = %s AND YEAR(dia) = %s"
        cursor.execute(sql, (mes,year,))

    #Obtener el resultado de la suma
    suma = cursor.fetchone()
    
    if suma is not None:
        suma = suma[0]
    else:
        suma = 0

    #Mostrar la suma en la interfaz grafica
    conn.close()
    return suma


def ModificarDatos(id, dia, motivo, monto, nuevo_monto, nuevo_id, nuevo_dia, nuevo_motivo):
    # Código para modificar datos en la base de datos
    try:
        conn = ConectarDB()
        cursor = conn.cursor()

        # Sentencia SQL para actualizar datos en la tabla
        sql = "UPDATE registros_contables SET id = %s, dia = %s, monto = %s, motivo = %s WHERE id = %s AND dia = %s AND monto = %s AND motivo = %s"
        values = (nuevo_id, nuevo_dia, nuevo_monto, nuevo_motivo, id, dia, monto, motivo)

        # Ejecuta la sentencia SQL
        cursor.execute(sql, values)

        # Confirma la transacción
        conn.commit()

        print("Datos modificados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al modificar datos: {err}")

    finally:
        cursor.close()
        conn.close()

def insertaringresos(monto,mes,year):
    # Código para insertar datos en la base de datos
    try:
        conn = ConectarDB()
        cursor = conn.cursor()

        # Sentencia SQL para insertar datos en la tabla
        sql = "INSERT INTO ingresos (mes, año, monto) VALUES (%s, %s, %s)"
        values = (mes,year,monto)
        # Ejecuta la sentencia SQL
        cursor.execute(sql, values)

        # Confirma la transacción
        conn.commit()

        print("Datos insertados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")

    finally:
        cursor.close()
        conn.close()

def MostrarTablaIngresosDb(treeview):
    # Realizar una consulta SQL para obtener los datos de la tabla "ingresos"
    conn = ConectarDB()
    cursor = conn.cursor()
    cursor.execute("SELECT id, mes, año, monto FROM ingresos")


    # Obtener los datos y ordenarlos por mes y año
    datos = sorted(cursor.fetchall(), key=lambda x: (x[1], x[0]))

    # Insertar los datos en el TreeView
    for row in datos:
        treeview.insert("", "end", values=row)

    conn.close()

def BorrarDatos():
    conn = ConectarDB()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM saldos")

    conn.commit()

    cursor.close()
    conn.close

    
def SumarMontosGastos(mes,year):
    conn = ConectarDB()
    cursor = conn.cursor()

    sql = "SELECT SUM(monto) FROM registros_contables WHERE MONTH(dia) = %s AND YEAR(dia) = %s"
    cursor.execute(sql, (mes,year,))

    #Obtener el resultado de la suma
    suma = cursor.fetchone()
    
    if suma is not None:
        suma = suma[0]
    else:
        suma = 0

    #Mostrar la suma en la interfaz grafica
    conn.close()
    return suma
    
def SumarMontosIngresos(mes,year):
    conn = ConectarDB()
    cursor = conn.cursor()

    sql = "SELECT SUM(monto) FROM ingresos WHERE mes = %s AND año = %s"
    cursor.execute(sql, (mes, year,))

    #Obtener el resultado de la suma
    suma = cursor.fetchone()
    
    if suma is not None:
        suma = suma[0]
    else:
        suma = 0

    #Mostrar la suma en la interfaz grafica
    conn.close()
    return suma

def IngresarDatosSaldo(mes,year,ingresos,gastos, saldo):
    # Código para insertar datos en la base de datos
    try:
        conn = ConectarDB()
        cursor = conn.cursor()

        # Sentencia SQL para insertar datos en la tabla
        sql = "INSERT INTO saldos (mes, año, ingresos, gastos, saldo) VALUES (%s, %s, %s,%s,%s)"
        values = (mes,year,ingresos,gastos,saldo)
        # Ejecuta la sentencia SQL
        cursor.execute(sql, values)

        # Confirma la transacción
        conn.commit()

        print("Datos insertados correctamente.")

    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")

    finally:
        cursor.close()
        conn.close()

def ActualizarDatos(mes,year,ingresos,gastos,saldo):
    conn = ConectarDB()
    cursor = conn.cursor()

    sql = "UPDATE saldos SET mes = %s, año = %s, ingresos = %s, gastos = %s, saldo = %s WHERE mes = %s AND año = %s"
    cursor.execute(sql,(mes,year,ingresos,gastos,saldo,mes,year,))

    conn.commit()
    print("Datos actualizados correctamente")

    cursor.close()
    conn.close()

    
def VerificarSiExiste(mes,year):
    conn = ConectarDB()
    cursor = conn.cursor()

    sql = "SELECT COUNT(*) FROM saldos WHERE mes = %s AND año = %s"
    cursor.execute(sql,(mes,year,))
    cantidad = cursor.fetchone()[0]
    print(int(cantidad))
    if int(cantidad) > 0:
        rta = True
        print()
    else:
        rta = False
    print(rta)
    return rta

def MostrarTablaSaldosDb(treeview):
    # Realizar una consulta SQL para obtener los datos de la tabla "ingresos"
    conn = ConectarDB()
    cursor = conn.cursor()
    cursor.execute("SELECT id, mes, año, ingresos, gastos, saldo FROM saldos")


    # Obtener los datos y ordenarlos por mes y año
    datos = sorted(cursor.fetchall(), key=lambda x: (x[1], x[0]))

    # Insertar los datos en el TreeView
    for row in datos:
        treeview.insert("", "end", values=row)

    conn.close()

    
def SumarSaldos():
    conn = ConectarDB()
    cursor = conn.cursor()

    sql = "SELECT SUM(saldo) FROM saldos"
    cursor.execute(sql)

    #Obtener el resultado de la suma
    suma = cursor.fetchone()
    
    if suma is not None:
        suma = suma[0]
    else:
        suma = 0

    #Mostrar la suma en la interfaz grafica
    conn.close()
    return suma

def EliminarIngreso(id):
    conn = ConectarDB()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM ingresos WHERE id = %s"
        cursor.execute(sql,(id,))

        conn.commit()
        print(f"Registro con ID {id} eliminado correctamente.")
    
    except mysql.connector.Error as e:
        print(f"Error al eliminar el registro: {e}")

    finally:
        cursor.close()
        conn.close()

def EliminarSaldo(id):
    conn = ConectarDB()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM saldos WHERE id = %s"
        cursor.execute(sql,(id,))

        conn.commit()
        print(f"Registro con ID {id} eliminado correctamente.")
    
    except mysql.connector.Error as e:
        print(f"Error al eliminar el registro: {e}")

    finally:
        cursor.close()
        conn.close()

def Borrar(data_id):
    # Código para eliminar datos de la base de datos
    pass

def retrieve_data():
    # Código para recuperar datos de la base de datos
    pass

