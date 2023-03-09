from flask import session
from conexionBD import * 

#https://pynative.com/python-mysql-database-connection/
#https://pynative.com/python-mysql-select-query-to-fetch-data/

#creando una funcion y dentro de la misma una data (un diccionario)
#con valores del usuario ya logueado
def dataLoginSesion():
    inforLogin = {
        "idLogin"             :session['id'],
        "tipoLogin"           :session['tipo_user'],
        "nombre"              :session['nombre'],
        "apellido"            :session['apellido'],
        "emailLogin"          :session['email'],
        "DNI"                 :session['DNI'],
        "Telefono"            :session['Telefono'],
        "Direccion"           :session['Direccion'],
        "sexo"                :session['sexo'],
        "pais"                      :session['pais'],
        "create_at"                 :session['create_at'],
        "tiene_expediente"  :session['tiene_expediente'],
        "escribe_su_caso"   :session['escribe_su_caso']
    }
    return inforLogin


def listaPaises():
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    querySQL  = ("SELECT * FROM countries")
    mycursor.execute(querySQL)
    paises = mycursor.fetchall() #fetchall () Obtener todos los registros
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    #print(Paises)
    return paises

def dataPerfilUsuario():
    conexion_MySQLdb = connectionBD() 
    mycursor       = conexion_MySQLdb.cursor(dictionary=True)
    idUser         = session['id']
    
    querySQL  = ("SELECT * FROM login_python WHERE id='%s'" % (idUser,))
    mycursor.execute(querySQL)
    datosUsuario = mycursor.fetchone() 
    mycursor.close() #cerrrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return datosUsuario


#Creando una funcion para obtener la lista de carros.
def listaCliente():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT login_python.id, CONCAT(login_python.nombre, ' ', login_python.apellido) AS nombre_completo, login_python.DNI, login_python.create_at, expediente.tipo_caso, expediente.c_expediente, expediente.archivo_adjunto, expediente.area, expediente.enfoque, (SELECT CONCAT (nombre, ' ', apellido) FROM login_python WHERE id = expediente.abogado_id) AS abogado FROM login_python INNER JOIN expediente ON expediente.cliente_id = login_python.id;"
    cur.execute(querySQL)
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda


#Creando una funcion para obtener la lista de carros.
def listaAbogados():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT CONCAT(nombre, ' ', apellido)AS ABOGADOS FROM login_python WHERE tipo_user=3;"
    cur.execute(querySQL)
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda


def detallesdelCliente(idCliente):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT login_python.id, CONCAT(login_python.nombre, ' ', login_python.apellido) AS nombre_completo, expediente.created_at, expediente.tipo_caso, login_python.Telefono  ,expediente.c_expediente, expediente.archivo_adjunto, login_python.escribe_su_caso, (SELECT CONCAT (nombre, ' ', apellido) FROM login_python WHERE id = expediente.abogado_id) AS abogado FROM login_python INNER JOIN expediente ON expediente.cliente_id = login_python.id WHERE login_python.id = '%s';" % (idCliente,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery



#update de cliente funcion
def updateCliente(id=''):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute("SELECT CONCAT(login_python.nombre, ' ', login_python.apellido) AS nombre_completo, login_python.DNI, login_python.create_at, expediente.tipo_caso, expediente.c_expediente, expediente.archivo_adjunto, expediente.area, expediente.enfoque, (SELECT CONCAT (nombre, ' ', apellido) FROM login_python WHERE id = expediente.abogado_id) AS abogado FROM login_python INNER JOIN expediente ON expediente.cliente_id = login_python.id;")
    resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
    return resultQueryData

#recibe la actualizacion del cliente
def  recibeActualizarCliente(marca, modelo, year, color, puertas, favorito, nuevoNombreFile, idCarro):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE carros
            SET 
                marca   = %s,
                modelo  = %s,
                year    = %s,
                color   = %s,
                puertas = %s,
                favorito= %s,
                foto    = %s
            WHERE id=%s
            """, (marca,modelo, year, color, puertas, favorito, nuevoNombreFile,  idCarro))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
