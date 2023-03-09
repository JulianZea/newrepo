from flask import Flask, render_template, request, redirect, url_for, session
from funciones import *  #Importando mis Funciones


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app


app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'


#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    if 'conectado' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template('public/modulo_login/index.html', dataPaises = listaPaises())

#mostrar la lista de clientes
''' @app.route('/listClient', methods=['GET','POST'])
def listClient():
    return render_template('public/dashboard/pages/administrador.html', miData = listaCliente())'''

#Creando mi Decorador para el Home
@app.route('/')
def inicio():
    if 'conectado' in session:
        return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion(), miData = listaCliente(), miLawyer = listaAbogados())
    else:
        return render_template('public/modulo_login/index.html', dataPaises = listaPaises())

@app.route('/login')
def login():
    if 'conectado' in session:
        return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion())
    else:
        return render_template('public/modulo_login/index.html', dataPaises = listaPaises())


#Ruta para editar el perfil del cliente
@app.route('/edit-profile', methods=['GET', 'POST'])
def editProfile():
    if 'conectado' in session:
        return render_template('public/dashboard/pages/Profile.html', dataUser = dataPerfilUsuario(), dataLogin = dataLoginSesion(), dataPaises = listaPaises())
    return redirect(url_for('inicio'))


@app.route('/ver-detalles-del-cliente/<int:idCliente>', methods=['GET', 'POST'])
def viewDetalleCliente(idCliente):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelCliente(idCliente) #Funcion que almacena los detalles del cliente
        
        if resultData:
            return render_template('public/dashboard/pages/view.html', infoCliente = resultData, msg='Detalles del Cliente', tipo=1, dataLogin = dataLoginSesion())
        else:
            return render_template('public/dashboard/pages/view.html', msg='No existe el Cliente', tipo=1, dataLogin = dataLoginSesion())
    return redirect(url_for('inicio'))

#RUTAS
#@app.route('/registrar-abogado', methods=['GET','POST'])
#def addAbogado():
#    return render_template('public/dashboard/pages/addAbogado.html', dataLogin = dataLoginSesion(), dataPaises = listaPaises())




#Registrando nuevo Abogado
"""@app.route('/carro', methods=['POST'])
def formAddCarro():
    if request.method == 'POST':
        marca               = request.form['marca']
        modelo              = request.form['modelo']
        year                = request.form['year']
        color               = request.form['color']
        puertas             = request.form['puertas']
        favorito            = request.form['favorito']
        
        
        if(request.files['foto'] !=''):
            file     = request.files['foto'] #recibiendo el archivo
            nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
            resultData = registrarCarro(marca, modelo, year, color, puertas, favorito, nuevoNombreFile)
            if(resultData ==1):
                return render_template('public/dashboard/pages/Dashboard.html', miData = listaCliente(), msg='El Registro fue un éxito', tipo=1, dataLogin = dataLoginSesion())
            else:
                return render_template('public/dashboard/pages/Dashboard.html', msg = 'Metodo HTTP incorrecto', tipo=1, dataLogin = dataLoginSesion())   
        else:
            return render_template('public/dashboard/pages/Dashboard.html', msg = 'Debe cargar una foto', tipo=1, dataLogin = dataLoginSesion())"""




# Cerrar session del usuario
@app.route('/logout')
def logout():
    msgClose = ''
    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    session.pop('id', None)
    session.pop('email', None)
    msgClose ="La sesión fue cerrada correctamente"
    return render_template('public/modulo_login/index.html', msjAlert = msgClose, typeAlert=1)