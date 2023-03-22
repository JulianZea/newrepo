import './styles.scss';

import { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from "axios";

import Constantes from "../../common/constantes";
import Alertas from '../../common/alertas';


function RegistroPage() {
    const nombresRef = useRef();

    const navigate = useNavigate()

    const [nombres, setNombres] = useState('');
    const [apellidos, setApellidos] = useState('');
    const [correo, setCorreo] = useState('');
    const [documento, setDocumento] = useState('');
    const [password, setPassword] = useState('');
    const [telefono, setTelefono] = useState('');
    const [direccion, setDireccion] = useState('');
    const [password2, setPassword2] = useState('');
    const [sexo, setSexo] = useState('');
    const [tieneExpediente, setTieneExpediente] = useState('');
    const [paisNacimiento, setPaisNacimiento] = useState('');
    const [descripcionCaso, setDescripcionCaso] = useState('');

    const [redirect, setRedirect] = useState(false)


    useEffect(() => {
        nombresRef.current.focus();
    }, []);

    useEffect(() => {
        if (redirect) navigate('/login');
    }, [redirect]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        axios({
            method: 'post',
            url: Constantes.API_URL + "/registro",
            data: {
                nombres: nombres,
                apellidos: apellidos,
                correo: correo,
                documento: documento,
                password: password,
                telefono: telefono,
                direccion: direccion,
                password2: password2,
                sexo: sexo,
                tieneExpediente: tieneExpediente,
                paisNacimiento: paisNacimiento,
                descripcionCaso: descripcionCaso
            }
        })
            .then((response) => {
                if (response && response.data && response.data.ok == true) {
                    Alertas.success('OK!', 'Datos grabados correctamente.');
                    setRedirect(true);
                    //setTimeout(() => {
                    //    setRedirect(true);
                    //}, 2000);
                } else {
                    Alertas.error('Ups...', 'Los datos no pudieron ser grabados...');
                    //setUsername('');
                    //setPassword('');
                }
            })
            .catch((error) => {
                Alertas.error('Ups...', 'Los datos no pudieron ser grabados...');
            });
    };

    let obtenerPaises = () => {
        const paises = [
            {
                "codigo": 'pe',
                "nombre": 'Perú'
            }
        ];
        return paises.map((pais) => {
            return <option key={pais} value={pais.codigo}>{pais.nombre}</option>;
        });
    };

    return (
        <>
            <div className="container">
                <div className="row justify-content-md-center mt-5 mb-5">

                    <div className="col-md-6 formRegisterUser" id="styleLogin">
                        <a href="{{ url_for('inicio') }}">
                            <img src="/images/iso-fondo_gris.png" alt="Logo" className="logoLogin" />
                        </a>
                        <h1 className="mb-3" id="title">Crear cuenta<hr /> </h1>
                        <form id="formRegisterClient" className="mt-5" onSubmit={handleSubmit} autoComplete="off">
                            <div className="row">
                                <div className="col-md-6">
                                    <label htmlFor="nombres" className="form-label">Nombres</label>
                                    <input type="text" id="nombres" className="form-control"
                                        required={true}
                                        ref={nombresRef}
                                        onChange={(e) => setNombres(e.target.value)}
                                        value={nombres}
                                    />
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="apellido" className="form-label">Apellido</label>
                                    <input type="text" id="apellido" className="form-control"
                                        required={true}
                                        onChange={(e) => setApellidos(e.target.value)}
                                        value={apellidos}
                                    />
                                </div>
                            </div>

                            <div className="row">
                                <div className="mb-6">
                                    <label htmlFor="email" className="form-label mt-3">Email</label>
                                    <input type="email" name="email" className="form-control"
                                        required={true}
                                        onChange={(e) => setCorreo(e.target.value)}
                                        value={correo}
                                    />
                                </div>
                            </div>

                            <div className="row">
                                <div className="col-md-6">
                                    <label htmlFor="DNI" className="form-label mt-3">DNI</label>
                                    <input type="text" id="DNI" className="form-control"
                                        required={true}
                                        onChange={(e) => setDocumento(e.target.value)}
                                        value={documento}
                                    />
                                </div>
                            </div>

                            <br />
                            <div className="row">
                                <div className="col-md-6">
                                    <label htmlFor="telefono" className="form-label mt-3">Telefono</label>
                                    <input type="text" id="telefono" className="form-control" pattern="[0-9]+"
                                        required={true}
                                        onChange={(e) => setTelefono(e.target.value)}
                                        value={telefono}
                                    />
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="direccion" className="form-label mt-3">Direccion</label>
                                    <input type="text" id="direccion" className="form-control"
                                        required={true}
                                        onChange={(e) => setDireccion(e.target.value)}
                                        value={direccion}
                                    />
                                </div>
                            </div>

                            <div className="row">
                                <div className="col-md-6">
                                    <label htmlFor="password" className="form-label mt-3">Password</label>
                                    <input type="password" id="password" className="form-control"
                                        required={true}
                                        onChange={(e) => setPassword(e.target.value)}
                                        value={password}
                                    />
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="repite_password" className="form-label mt-3">Repetir Password</label>
                                    <input type="password" id="repite_password" className="form-control"
                                        required={true}
                                        onChange={(e) => setPassword2(e.target.value)}
                                        value={password2}
                                    />
                                </div>
                            </div>

                            <div className="row">
                                <div className="col-md-6">
                                    <label htmlFor="sexo" className="mt-3">Sexo</label>
                                    <select id="sexo" className="form-control"
                                        required={true}
                                        onChange={(e) => setSexo(e.target.value)}
                                        value={sexo}
                                    >
                                        <option value="" selected>--- Seleccione ---</option>
                                        <option value="Masculino">Masculino</option>
                                        <option value="Femenino">Femenino</option>
                                    </select>
                                </div>
                                <div className="col-md-6">
                                    <label htmlFor="brand" className="mt-3" >¿Tiene expediente?</label> <br />
                                    <div className="form-check form-check-inline">
                                        <input className="form-check-input" type="radio" id="tiene_expediente_si" value="Si" name="tiene_expediente"
                                            required={true}
                                            onChange={(e) => setTieneExpediente(e.target.value)}
                                        />
                                        <label className="form-check-label" htmlFor="tiene_expediente_si">Si</label>
                                    </div>
                                    <div className="form-check form-check-inline">
                                        <input className="form-check-input" type="radio" id="tiene_expediente_no" value="No" name="tiene_expediente"
                                            required={true}
                                            onChange={(e) => setTieneExpediente(e.target.value)}
                                        />
                                        <label className="form-check-label" htmlFor="tiene_expediente_no">No</label>
                                    </div>
                                </div>
                            </div>

                            <div className="row">
                                <div className="mb-6">
                                    <label htmlFor="pais" className="form-label mt-3">País de Nacimiento</label>
                                    <select id="pais" className="form-control"
                                        required={true}
                                        onChange={(e) => setPaisNacimiento(e.target.value)}
                                        value={paisNacimiento}
                                    >
                                        {obtenerPaises()}
                                    </select>
                                </div>
                            </div>

                            <div className="row">
                                <div className="mb-6">
                                    <label htmlFor="pais" className="form-label mt-3">Escribe tu caso</label>
                                    <textarea id="escribe_su_caso" placeholder="..." className="form-control"
                                        required={true}
                                        onChange={(e) => setDescripcionCaso(e.target.value)}
                                        value={descripcionCaso}
                                    />
                                </div>
                            </div>

                            <div className="row">
                                <div className="d-grid gap-2 mt-3 mb-3">
                                    <input type="submit" className="btn btn-primary btn-send" id="sendForm" value="Crear Ahora!" />
                                </div>
                            </div>

                            <div className="row">
                                <div className="mb-12">
                                    <span>
                                        Ya tengo cuenta,
                                    </span>

                                    <a href="#" className="volverViewLogin">
                                        <i className="bi bi-arrow-left-short"></i>
                                        Volver
                                    </a>
                                </div>
                            </div>
                        </form>
                    </div>

                </div>
            </div>
        </>
    );
}

export default RegistroPage;