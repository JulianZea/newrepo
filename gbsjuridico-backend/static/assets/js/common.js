function eliminarCarroJavaScript(id) {

    Swal.fire({
        title: 'Eliminar',
        text: '¿Desea eliminar el registro seleccionado?',
        icon: 'question',
        confirmButtonText: 'Si',
        showCancelButton: true,
        cancelButtonText: 'Cancelar'
    });

}