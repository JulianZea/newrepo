function eliminarCarroJavaScript(id) {

    Swal.fire({
        title: 'Eliminar',
        text: '¿Desea eliminar el registro del cliente seleccionado?',
        icon: 'question',
        confirmButtonText: 'Si',
        showCancelButton: true,
        cancelButtonText: 'Cancelar'
    });

}

// Objeto con las mismas opciones que en Python
const derecho = {
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
};

function mostrarEnfoques() {
    // Obtener los elementos select
    const areaSelect = document.getElementById("area");
    const enfoqueSelect = document.getElementById("enfoque");
    
    // Obtener la opción seleccionada
    const areaSeleccionada = areaSelect.value;
    
    // Limpiar las opciones anteriores
    enfoqueSelect.innerHTML = "";
    
    // Agregar las nuevas opciones
    derecho[areaSeleccionada].forEach(function(enfoque) {
    const option = document.createElement("option");
    option.value = enfoque;
    option.text = enfoque;
    enfoqueSelect.add(option);
    });
}