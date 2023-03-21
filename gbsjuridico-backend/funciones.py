from flask import session
from conexionBD import * 
import os
from werkzeug.utils import secure_filename 

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

def dataexpediente():
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


#Creando una funcion para obtener la lista de cliente.
def listaCliente(idAbogado=""):
    if idAbogado == "":
        conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
        cur      = conexion_MySQLdb.cursor(dictionary=True)

        querySQL = "SELECT login_python.id, CONCAT(login_python.nombre, ' ', login_python.apellido) AS nombre_completo, login_python.DNI, login_python.create_at, expediente.tipo_caso, expediente.c_expediente, expediente.archivo_adjunto, expediente.area, expediente.enfoque, (SELECT CONCAT (nombre, ' ', apellido) FROM login_python WHERE id = expediente.abogado_id) AS abogado FROM login_python LEFT JOIN expediente ON expediente.cliente_id = login_python.id WHERE login_python.tipo_user = 2;"
        cur.execute(querySQL)
        resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
        totalBusqueda = len(resultadoBusqueda) #Total de busqueda
        
        cur.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD    
        return resultadoBusqueda
    else:
        conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
        cur      = conexion_MySQLdb.cursor(dictionary=True)

        querySQL = "SELECT login_python.id, CONCAT(login_python.nombre, ' ', login_python.apellido) AS nombre_completo, login_python.DNI, login_python.create_at, expediente.tipo_caso, expediente.c_expediente, expediente.archivo_adjunto, expediente.area, expediente.enfoque, (SELECT CONCAT (nombre, ' ', apellido) FROM login_python WHERE id = expediente.abogado_id) AS abogado FROM login_python LEFT JOIN expediente ON expediente.cliente_id = login_python.id WHERE login_python.tipo_user = 2 && expediente.abogado_id = %s;"
        cur.execute(querySQL % (idAbogado,))
        resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
        totalBusqueda = len(resultadoBusqueda) #Total de busqueda
        
        cur.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD    
        return resultadoBusqueda

    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT login_python.id, CONCAT(login_python.nombre, ' ', login_python.apellido) AS nombre_completo, login_python.DNI, login_python.create_at, expediente.tipo_caso, expediente.c_expediente, expediente.archivo_adjunto, expediente.area, expediente.enfoque, (SELECT CONCAT (nombre, ' ', apellido) FROM login_python WHERE id = expediente.abogado_id) AS abogado FROM login_python LEFT JOIN expediente ON expediente.cliente_id = login_python.id WHERE login_python.tipo_user = 2 && expediente.abogado_id = %s;"
    cur.execute(querySQL % (idAbogado,))
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda


#Creando una funcion para obtener la lista de cliente.
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


#function of area/enfoque
def listfocusbyarea():
    derecho = {
        "penal": [
            "Defensa penal general",
            "Delitos fiscales",
            "Delitos informáticos",
            "Delitos de drogas",
            "Delitos de violencia doméstica",
            "Delitos sexuales",
            "Delitos de tráfico",
            "Delitos contra la propiedad",
            "Delitos contra la persona",
            "Delitos de homicidio",
            "Delitos de fraude",
            "Delitos de blanqueo de capitales",
            "Delitos de corrupción",
            "Delitos de lesiones",
            "Delitos de secuestro",
            "Delitos de extorsión",
            "Delitos de robo"
        ],
        "civil": [
            "Derecho de familia",
            "Derecho de sucesiones",
            "Derecho laboral",
            "Derecho mercantil",
            "Derecho inmobiliario",
            "Derecho de la propiedad intelectual",
            "Derecho de la responsabilidad civil",
            "Derecho de contratos",
            "Derecho administrativo",
            "Derecho tributario"
        ],
        "laboral": [
            "Despidos y terminaciones laborales",
            "Contratación de empleados y asesoramiento en contratos laborales",
            "Acoso y discriminación en el lugar de trabajo",
            "Lesiones y enfermedades relacionadas con el trabajo",
            "Seguridad laboral y cumplimiento de las normativas",
            "Salarios y beneficios laborales",
            "Arbitraje y litigios laborales",
            "Negociación colectiva y relaciones con los sindicatos",
            "Asesoramiento en casos de huelgas y conflictos laborales"
        ]
        
    }
    return derecho


#update de cliente funcion
def updateCliente(id=''):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute("SELECT login_python.id, login_python.nombre, login_python.apellido, login_python.DNI, login_python.create_at, expediente.tipo_caso, expediente.c_expediente, login_python.Telefono, expediente.archivo_adjunto, expediente.area, expediente.enfoque, (SELECT CONCAT (nombre, ' ', apellido) FROM login_python WHERE id = expediente.abogado_id) AS abogado FROM login_python LEFT JOIN expediente ON expediente.cliente_id = login_python.id WHERE login_python.id ='%s';" % (id,))
    resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
    return resultQueryData


#recibe la actualizacion del cliente
def  recibeActualizarCliente(nombre, apellido, DNI, Telefono, create_at, tipo_caso, c_expediente,archivo_adjunto, area, enfoque, abogado, idCliente):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE login_python
            SET nombre = %s,
                apellido = %s,
                DNI = %s,
                Telefono = %s,
                create_at = %s
            WHERE id=%s;""",(nombre, apellido, DNI,Telefono, create_at, idCliente))
        if archivo_adjunto == "sin_foto.jpg":
            cur.execute("""
                UPDATE expediente
                SET tipo_caso = %s,
                    c_expediente = %s,
                    area = %s,
                    enfoque = %s,
                    abogado_id = (
                        SELECT id FROM login_python
                        WHERE CONCAT(nombre, ' ', apellido) = %s
                        )
                WHERE cliente_id=%s;""",
                (tipo_caso, c_expediente, area, enfoque, abogado, idCliente))
        else:
            cur.execute("""
                UPDATE expediente
                SET tipo_caso = %s,
                    c_expediente = %s,
                    archivo_adjunto = %s,
                    area = %s,
                    enfoque = %s,
                    abogado_id = (
                        SELECT id FROM login_python
                        WHERE CONCAT(nombre, ' ', apellido) = %s
                        )
                WHERE cliente_id=%s;""",
                (tipo_caso, c_expediente, archivo_adjunto, area, enfoque, abogado, idCliente))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update


#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio