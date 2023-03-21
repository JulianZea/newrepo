#Importando  flask y algunos paquetes
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
from datetime import datetime

from conexionBD import *  #Importando conexion BD
from funciones import *  #Importando mis Funciones
from routes import * #Vistas


import re
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/dashboard', methods=['GET', 'POST'])
def loginUser():
    conexion_MySQLdb = connectionBD()
    if 'conectado' in session:
        abogado = dataLoginSesion()
        if (abogado["tipoLogin"] == 3):
            return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion(), miData = listaCliente(abogado["idLogin"]), miLawyer = listaAbogados(), infoCliente = detallesdelCliente(abogado["idLogin"]))
        elif (abogado["tipoLogin"] == 2):
            return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion(), miData = listaCliente(), miLawyer = listaAbogados(), infoCliente = detallesdelCliente(abogado["idLogin"]))
        else:
            return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion(), miData = listaCliente(), miLawyer = listaAbogados(), infoCliente = detallesdelCliente(abogado["idLogin"]))
    else:
        msg = ''
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            email      = str(request.form['email'])
            password   = str(request.form['password'])
            
            # Comprobando si existe una cuenta
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM login_python WHERE email = %s", [email])
            account = cursor.fetchone()

            if account:
                if (check_password_hash(account['password'],password) or account['password'] == password):
                    # Crear datos de sesión, para poder acceder a estos datos en otras rutas 
                    session['conectado']        = True
                    session['id']               = account['id']
                    session['tipo_user']        = account['tipo_user']
                    session['nombre']           = account['nombre']
                    session['apellido']         = account['apellido']
                    session['email']            = account['email']
                    session['DNI']             = account['DNI']
                    session['Telefono']             = account['Telefono']
                    session['Direccion']             = account['Direccion']
                    session['sexo']             = account['sexo']
                    session['pais']             = account['pais']
                    session['create_at']        = account['create_at']
                    session['tiene_expediente']     = account['tiene_expediente']
                    session['escribe_su_caso']             = account['escribe_su_caso']

                    msg = "Ha iniciado sesión correctamente."
                    return render_template('public/dashboard/home.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion(), infoCliente = detallesdelCliente(session['id']))                    
                else:
                    msg = 'Datos incorrectos, por favor verfique!'
                    return render_template('public/modulo_login/index.html', msjAlert = msg, typeAlert=0)
            else:
                return render_template('public/modulo_login/index.html', msjAlert = msg, typeAlert=0)
    return render_template('public/modulo_login/index.html', msjAlert = 'Debe iniciar sesión.', typeAlert=0, dataPaises = listaPaises())



#Registrando una cuenta de Cliente
@app.route('/registro-usuario', methods=['GET', 'POST'])
def registerUser():
    msg = ''
    conexion_MySQLdb = connectionBD()
    if request.method == 'POST':
        tipo_user                   =2
        nombre                      = request.form['nombre']
        apellido                    = request.form['apellido']
        email                       = request.form['email']
        DNI                       = request.form['DNI']
        Telefono                       = request.form['Telefono']
        Direccion                       = request.form['Direccion']
        password                    = request.form['password']
        repite_password             = request.form['repite_password']
        sexo                        = request.form['sexo']
        tiene_expediente    = request.form['tiene_expediente']
        pais                        = request.form['pais']
        escribe_su_caso                       = request.form['escribe_su_caso']
        create_at                   = date.today()
        #current_time = datetime.datetime.now()

        # Comprobando si ya existe la cuenta de Usuario con respecto al email
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        cursor.execute('SELECT * FROM login_python WHERE email = %s', (email,))
        account = cursor.fetchone()
        cursor.close() #cerrrando conexion SQL

        if account:
            msg = 'Ya existe el Email!'
        elif password != repite_password:
            msg = 'Disculpa, las clave no coinciden!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Disculpa, formato de Email incorrecto!'
        elif not email or not password or not password or not repite_password:
            msg = 'El formulario no debe estar vacio!'
        else:
            # La cuenta no existe y los datos del formulario son válidos,
            password_encriptada = generate_password_hash(password, method='sha256')
            conexion_MySQLdb = connectionBD()
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute('INSERT INTO login_python (tipo_user, nombre, apellido, email, DNI, Telefono, Direccion, password, sexo, pais, create_at, tiene_expediente, escribe_su_caso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (tipo_user, nombre, apellido, email, DNI, Telefono, Direccion, password_encriptada, sexo, pais, create_at, tiene_expediente, escribe_su_caso))
            conexion_MySQLdb.commit()
            cursor.close()
            msg = 'Cuenta creada correctamente!'

        return render_template('public/modulo_login/index.html', msjAlert = msg, typeAlert=1, dataPaises = listaPaises())
    return render_template('public/layout.html', dataLogin = dataLoginSesion(), msjAlert = msg, typeAlert=0)




@app.route('/actualizar-mi-perfil/<id>', methods=['POST'])
def actualizarMiPerfil(id):
    if 'conectado' in session:
        msg = ''
        if request.method == 'POST':
            nombre        = request.form['nombre']
            apellido      = request.form['apellido']
            email         = request.form['email']
            sexo          = request.form['sexo']
            pais          = request.form['pais']

            if(request.form['password']):
                password         = request.form['password'] 
                repite_password  = request.form['repite_password'] 
                
                if password != repite_password:
                    msg ='Las claves no coinciden'
                    return render_template('public/dashboard/home.html', msjAlert = msg, typeAlert=0, dataLogin = dataLoginSesion())
                else:
                    nueva_password = generate_password_hash(password, method='sha256')
                    conexion_MySQLdb = connectionBD()
                    cur = conexion_MySQLdb.cursor()
                    cur.execute("""
                        UPDATE login_python 
                        SET 
                            nombre = %s, 
                            apellido = %s, 
                            email = %s, 
                            sexo = %s, 
                            pais = %s, 
                            password = %s
                        WHERE id = %s""", (nombre, apellido, email, sexo, pais, nueva_password, id))
                    conexion_MySQLdb.commit()
                    cur.close() #Cerrando conexion SQL
                    conexion_MySQLdb.close() #cerrando conexion de la BD
                    msg = 'Perfil actualizado correctamente'
                    return render_template('public/dashboard/home.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion())
            else:
                msg = 'Perfil actualizado con exito'
                conexion_MySQLdb = connectionBD()
                cur = conexion_MySQLdb.cursor()
                cur.execute("""
                    UPDATE login_python 
                    SET 
                        nombre = %s, 
                        apellido = %s, 
                        email = %s, 
                        sexo = %s, 
                        pais = %s
                    WHERE id = %s""", (nombre, apellido, email, sexo, pais, id))
                conexion_MySQLdb.commit()
                cur.close()
                return render_template('public/dashboard/home.html', msjAlert = msg, typeAlert=1, dataLogin = dataLoginSesion())
        return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion())             




#registrando cuenta de abogado
@app.route('/registro-abogado', methods=['GET', 'POST'])
def registerLawyer():
    msg = ''
    conexion_MySQLdb = connectionBD()
    if request.method == 'POST':
        tipo_user                   =3
        nombre                      = request.form['nombre']
        apellido                    = request.form['apellido']
        email                       = request.form['email']
        Telefono                       = request.form['Telefono']
        password                    = request.form['password']
        repite_password             = request.form['repite_password']
        sexo                        = request.form['sexo']
        pais                        = request.form['pais']
        create_at                   = date.today()
        #current_time = datetime.datetime.now()

        # Comprobando si ya existe la cuenta de Abogado con respecto al email
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        cursor.execute('SELECT * FROM login_python WHERE email = %s', (email,))
        account = cursor.fetchone()
        cursor.close() #cerrrando conexion SQL

        if account:
            msg = 'Ya existe el Email!'
        elif password != repite_password:
            msg = 'Disculpa, las clave no coinciden!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Disculpa, formato de Email incorrecto!'
        elif not email or not password or not password or not repite_password:
            msg = 'El formulario no debe estar vacio!'
        else:
            # La cuenta no existe y los datos del formulario son válidos,
            password_encriptada = generate_password_hash(password, method='sha256')
            conexion_MySQLdb = connectionBD()
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute('INSERT INTO login_python (tipo_user, nombre, apellido, email, Telefono, password, sexo, pais, create_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (tipo_user, nombre, apellido, email, Telefono, password_encriptada, sexo, pais, create_at))
            conexion_MySQLdb.commit()
            cursor.close()
            msg = 'Cuenta creada correctamente!'

        return render_template('public/dashboard/pages/addAbogado.html', msjAlert = msg, typeAlert=1, dataPaises = listaPaises(), dataLogin = dataLoginSesion())
    return render_template('public/dashboard/pages/addAbogado.html', dataLogin = dataLoginSesion(), msjAlert = msg, typeAlert=0, dataPaises = listaPaises())


#update de cliente
@app.route('/form-update-cliente/<string:id>', methods=['GET','POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateCliente(id)
        if resultData:
            return render_template('public/dashboard/pages/update.html',  dataInfo = resultData, dataLogin = dataLoginSesion(), miLawyer = listaAbogados(), areas = listfocusbyarea())
        else:
            return render_template('public/dashboard/pages/administrador.html', miData = listaCliente(), msg='No existe el cliente', tipo= 1, dataInfo = resultData())
    else:
        return render_template('public/dashboard/pages/administrador.html', miData = listaCliente(), msg = 'Metodo HTTP incorrecto', tipo=1, dataInfo = resultData())



#verificar la actualización cliente
@app.route('/actualizar-cliente/<string:idCliente>', methods=['POST'])
def  formActualizarCliente(idCliente):
    if request.method == 'POST':
        nombre           = request.form['nombre']
        apellido           = request.form['apellido']
        DNI          = request.form['DNI']
        Telefono          = request.form['Telefono']
        create_at            = request.form['create_at']
        tipo_caso           = request.form['tipo_caso']
        c_expediente         = request.form['c_expediente']
        # archivo_adjunto        = request.form['archivo_adjunto']
        area        = request.form['area']
        enfoque        = request.form['enfoque']
        abogado        = request.form['abogado']

        #Script para recibir el archivo (foto)
        if(request.files['archivo_adjunto']):
            file     = request.files['archivo_adjunto']
            archivo_adjunto = recibeFoto(file)
            resultData = recibeActualizarCliente(nombre, apellido, DNI, Telefono, create_at, tipo_caso, c_expediente, archivo_adjunto, area, enfoque, abogado, idCliente)
        else:
            archivo_adjunto  ='sin_foto.jpg'
            resultData = recibeActualizarCliente(nombre, apellido, DNI, Telefono, create_at, tipo_caso, c_expediente, archivo_adjunto, area, enfoque, abogado, idCliente)

        if(resultData ==1):
            return render_template('public/dashboard/pages/administrador.html', miData = listaCliente(), msg='Datos del cliente actualizados', tipo=1, dataInfo = resultData)
        else:
            msg ='No se actualizo el registro'
            return render_template('public/dashboard/pages/administrador.html', miData = listaCliente(), msg='No se pudo actualizar', tipo=1, dataInfo = resultData)

def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el expediente actual
    filename = secure_filename(file.filename) #Nombre original del expediente

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = file.filename
    #print(nuevoNombreFile)
    
    upload_path = os.path.join (basepath, 'static/assets/expedientes', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile


if __name__ == "__main__":
    app.run(debug=True, port=8000)
