import './styles.scss';

import axios from "axios";
import { useEffect, useRef, useState } from 'react';
import { useNavigate } from "react-router-dom";

import Constantes from "../../common/constantes";
import Alertas from '../../common/alertas';


const LoginPage = () => {

    const usernameRef = useRef();

    const navigate = useNavigate()

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [redirect, setRedirect] = useState(false)


    useEffect(() => {
        usernameRef.current.focus();
    }, []);

    useEffect(() => {
        if (redirect) navigate('/dashboard');
    }, [redirect]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        axios({
            method: 'post',
            url: Constantes.API_URL + "/loginUser",
            data: {
                username: username,
                password: password
            }
        })
            .then((response) => {
                if (response && response.data) {
                    setRedirect(true);
                } else {
                    //swal.fire({
                    //    icon: 'error',
                    //    title: 'Ups...',
                    //    text: 'Usuario o contraseña incorrectos...'
                    //});
                    Alertas.error('Ups...', 'Usuario o contraseña incorrectos...');
                    setUsername('');
                    setPassword('');
                }
            })
            .catch((error) => {
                //console.log(error);
                //swal.fire({
                //    icon: 'error',
                //    title: 'Ups...',
                //    text: 'Sucedió un problema!'
                //});
                Alertas.error('Ups...', 'Sucedió un problema!');
            });
    };

    return (
        <>
            <div className="container">
                <div className="row justify-content-md-center mt-5 mb-5">

                    <div className="col-md-6 cajaLogin" id="styleLogin">
                        <div className="mb-12">
                            <a href="/inicio">
                                <img src="images/iso-fondo_gris.png" alt="Logo" className="logoLogin" />
                            </a>
                        </div>

                        <h1 className="mb-5" id="title">Login<hr /> </h1>
                        <form onSubmit={handleSubmit} autoComplete="off">
                            <div className="mb-6">
                                <label htmlFor="username" className="form-label">Escribe tu correo</label>
                                <input type="text" id="username" className="form-control" autoComplete="off" required={true}
                                    ref={usernameRef}
                                    onChange={(e) => setUsername(e.target.value)}
                                    value={username}
                                />
                            </div>
                            <div className="mb-6">
                                <label htmlFor="password" className="form-label mt-4">Escribe tu Contraseña</label>
                                <input type="password" id="password" className="form-control" autoComplete="off" required={true}
                                    onChange={(e) => setPassword(e.target.value)}
                                    value={password}
                                />
                            </div>

                            <div className="d-grid gap-2 mt-3 mb-3">
                                <button type="submit" className="btn btn-primary btn-send">Entrar Ahora!</button>
                            </div>

                            <div className="mb-12">
                                <span>
                                    No tienes Cuenta?
                                </span>
                                &nbsp;&nbsp;
                                <a href="/registro" id="link_sign_up" className="createUser">
                                    Crear cuenta
                                </a>
                            </div>
                        </form>

                    </div>

                </div>
            </div>
        </>
    );
}

export default LoginPage;