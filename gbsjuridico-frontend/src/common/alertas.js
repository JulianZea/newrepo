import Swal from "sweetalert2";

class Alertas {

    //const MySwal = withReactContent(Swal);

    static success = (title, message) => {
        Swal.fire({
            title: title,
            text: message,
            icon: "success",
            confirmButtonText: "OK",
        });
    };

    static error = (title, message) => {
        Swal.fire({
            title: title,
            text: message,
            icon: "error",
            confirmButtonText: "OK",
        });
    };
}

export default Alertas;