/* =====================================================
   SISTEMA DE GESTIÓN DE EQUIPOS INFORMÁTICOS
   Trabajo Práctico Ampliatorio - Web
   ===================================================== */


/* =====================================================
   1. VARIABLES PRINCIPALES
   ===================================================== */

// Array donde se almacenan todos los equipos.
let equipos = [];

// Variable que permite saber si estamos editando un equipo.
let indiceEditando = null;


/* =====================================================
   2. OBTENER ELEMENTOS DEL HTML
   ===================================================== */

// Formulario principal.
const formulario = document.getElementById("formEquipo");

// Campos del formulario.
const tipo = document.getElementById("tipo");
const titular = document.getElementById("titular");
const marca = document.getElementById("marca");
const modelo = document.getElementById("modelo");
const procesador = document.getElementById("procesador");
const ram = document.getElementById("ram");
const almacenamiento = document.getElementById("almacenamiento");
const placaVideo = document.getElementById("placaVideo");
const pantalla = document.getElementById("pantalla");
const estado = document.getElementById("estado");
const sugerencias = document.getElementById("sugerencias");

// Contenedor donde se muestran los equipos.
const listaEquipos = document.getElementById("listaEquipos");

// Mensaje que aparece cuando no hay equipos.
const mensajeVacio = document.getElementById("mensajeVacio");

// Buscador.
const buscador = document.getElementById("buscador");

// Filtro de estado.
const filtroEstado = document.getElementById("filtroEstado");

// Botón de exportar.
const btnExportar = document.getElementById("btnExportar");

// Input para importar JSON.
const inputImportar = document.getElementById("inputImportar");

// Contadores.
const contadorTotal = document.getElementById("contadorTotal");
const contadorOperativos = document.getElementById("contadorOperativos");
const contadorReparacion = document.getElementById("contadorReparacion");
const contadorDescartados = document.getElementById("contadorDescartados");


/* =====================================================
   3. CARGAR LOS DATOS DE LOCALSTORAGE
   ===================================================== */

// Cuando se abre la página, buscamos si existen
// equipos guardados anteriormente.
cargarDesdeLocalStorage();


/* =====================================================
   4. FUNCIÓN PARA GUARDAR EN LOCALSTORAGE
   ===================================================== */

function guardarEnLocalStorage() {

    // Convertimos el array de equipos a texto JSON.
    const datos = JSON.stringify(equipos);

    // Guardamos los datos en el navegador.
    localStorage.setItem("equipos", datos);
}


/* =====================================================
   5. FUNCIÓN PARA CARGAR DESDE LOCALSTORAGE
   ===================================================== */

function cargarDesdeLocalStorage() {

    // Buscamos los datos guardados.
    const datosGuardados = localStorage.getItem("equipos");

    // Si existen datos guardados...
    if (datosGuardados) {

        // Convertimos el texto JSON nuevamente
        // en un array de JavaScript.
        equipos = JSON.parse(datosGuardados);
    }

    // Mostramos los equipos en pantalla.
    mostrarEquipos();

    // Actualizamos los contadores.
    actualizarContadores();
}


/* =====================================================
   6. EVENTO DEL FORMULARIO
   ===================================================== */

formulario.addEventListener("submit", function(evento) {

    // Evita que la página se recargue al enviar el formulario.
    evento.preventDefault();


    // Creamos un objeto con todos los datos ingresados.
    const equipo = {

        tipo: tipo.value,
        titular: titular.value,
        marca: marca.value,
        modelo: modelo.value,
        procesador: procesador.value,
        ram: ram.value,
        almacenamiento: almacenamiento.value,
        placaVideo: placaVideo.value,
        pantalla: pantalla.value,
        estado: estado.value,
        sugerencias: sugerencias.value
    };


    // Si no estamos editando ningún equipo...
    if (indiceEditando === null) {

        // Agregamos el nuevo equipo al array.
        equipos.push(equipo);

    } else {

        // Reemplazamos el equipo que estamos editando.
        equipos[indiceEditando] = equipo;

        // Volvemos a dejar la variable en null.
        indiceEditando = null;

        // Cambiamos el texto del botón.
        document.getElementById("btnGuardar").textContent =
            "Guardar equipo";
    }


    // Guardamos los cambios.
    guardarEnLocalStorage();

    // Mostramos nuevamente los equipos.
    mostrarEquipos();

    // Actualizamos los contadores.
    actualizarContadores();

    // Limpiamos el formulario.
    formulario.reset();
});


/* =====================================================
   7. MOSTRAR LOS EQUIPOS
   ===================================================== */

function mostrarEquipos() {

    // Limpiamos la lista antes de volver a mostrarla.
    listaEquipos.innerHTML = "";


    // Obtenemos los equipos que cumplen con
    // la búsqueda y el filtro.
    const equiposFiltrados = obtenerEquiposFiltrados();


    // Si no hay equipos para mostrar...
    if (equiposFiltrados.length === 0) {

        // Mostramos el mensaje correspondiente.
        listaEquipos.innerHTML =
            "<p id='mensajeVacio'>No hay equipos registrados.</p>";

        return;
    }


    // Recorremos los equipos filtrados.
    equiposFiltrados.forEach(function(dato) {

        // Creamos una tarjeta para cada equipo.
        const tarjeta = document.createElement("div");

        tarjeta.classList.add("equipo");


        // Buscamos el índice original del equipo.
        const indiceOriginal = equipos.indexOf(dato);


        // Creamos el contenido de la tarjeta.
        tarjeta.innerHTML = `

            <h3>${dato.marca} ${dato.modelo}</h3>

            <p>
                <strong>Tipo:</strong>
                ${dato.tipo}
            </p>

            <p>
                <strong>Titular:</strong>
                ${dato.titular}
            </p>

            <p>
                <strong>Procesador:</strong>
                ${dato.procesador}
            </p>

            <p>
                <strong>Memoria RAM:</strong>
                ${dato.ram}
            </p>

            <p>
                <strong>Almacenamiento:</strong>
                ${dato.almacenamiento}
            </p>

            <p>
                <strong>Placa de video:</strong>
                ${dato.placaVideo || "No especificada"}
            </p>

            <p>
                <strong>Pantalla:</strong>
                ${dato.pantalla || "No especificada"}
            </p>

            <p>
                <strong>Estado:</strong>
                <span class="estado">
                    ${dato.estado}
                </span>
            </p>

            <p>
                <strong>Sugerencias:</strong>
                ${dato.sugerencias || "Sin sugerencias"}
            </p>

            <button
                class="btnEditar"
                onclick="editarEquipo(${indiceOriginal})">
                Editar
            </button>

            <button
                class="btnEliminar"
                onclick="eliminarEquipo(${indiceOriginal})">
                Eliminar
            </button>
        `;


        // Agregamos la tarjeta a la lista.
        listaEquipos.appendChild(tarjeta);
    });
}


/* =====================================================
   8. BUSCAR Y FILTRAR EQUIPOS
   ===================================================== */

function obtenerEquiposFiltrados() {

    // Obtenemos lo que escribió el usuario.
    const textoBusqueda =
        buscador.value.toLowerCase().trim();


    // Obtenemos el estado seleccionado.
    const estadoSeleccionado =
        filtroEstado.value;


    // Filtramos el array.
    return equipos.filter(function(equipo) {

        // Buscamos por titular.
        const coincideTitular =
            equipo.titular
                .toLowerCase()
                .includes(textoBusqueda);


        // Buscamos por marca.
        const coincideMarca =
            equipo.marca
                .toLowerCase()
                .includes(textoBusqueda);


        // Comprobamos si coincide el estado.
        const coincideEstado =
            estadoSeleccionado === "Todos" ||
            equipo.estado === estadoSeleccionado;


        // El equipo aparece si coincide
        // el titular o la marca y también
        // cumple con el filtro de estado.
        return (
            (coincideTitular || coincideMarca) &&
            coincideEstado
        );
    });
}


/* =====================================================
   9. EVENTO DEL BUSCADOR
   ===================================================== */

buscador.addEventListener("input", function() {

    // Cada vez que se escribe algo,
    // actualizamos la lista.
    mostrarEquipos();
});


/* =====================================================
   10. EVENTO DEL FILTRO
   ===================================================== */

filtroEstado.addEventListener("change", function() {

    // Cuando cambia el estado seleccionado,
    // actualizamos la lista.
    mostrarEquipos();
});


/* =====================================================
   11. ACTUALIZAR CONTADORES
   ===================================================== */

function actualizarContadores() {

    // Cantidad total de equipos.
    contadorTotal.textContent = equipos.length;


    // Contamos los equipos operativos.
    const operativos = equipos.filter(function(equipo) {

        return equipo.estado === "Operativo";

    }).length;


    // Contamos los equipos en reparación.
    const reparacion = equipos.filter(function(equipo) {

        return equipo.estado === "En reparación";

    }).length;


    // Contamos los equipos descartados.
    const descartados = equipos.filter(function(equipo) {

        return equipo.estado === "Descartado";

    }).length;


    // Mostramos los resultados.
    contadorOperativos.textContent = operativos;
    contadorReparacion.textContent = reparacion;
    contadorDescartados.textContent = descartados;
}


/* =====================================================
   12. EDITAR EQUIPO
   ===================================================== */

function editarEquipo(indice) {

    // Guardamos el índice del equipo que estamos editando.
    indiceEditando = indice;


    // Obtenemos el equipo seleccionado.
    const equipo = equipos[indice];


    // Colocamos sus datos nuevamente en el formulario.
    tipo.value = equipo.tipo;
    titular.value = equipo.titular;
    marca.value = equipo.marca;
    modelo.value = equipo.modelo;
    procesador.value = equipo.procesador;
    ram.value = equipo.ram;
    almacenamiento.value = equipo.almacenamiento;
    placaVideo.value = equipo.placaVideo;
    pantalla.value = equipo.pantalla;
    estado.value = equipo.estado;
    sugerencias.value = equipo.sugerencias;


    // Cambiamos el texto del botón.
    document.getElementById("btnGuardar").textContent =
        "Guardar cambios";


    // Subimos la pantalla hasta el formulario.
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


/* =====================================================
   13. ELIMINAR EQUIPO
   ===================================================== */

function eliminarEquipo(indice) {

    // Pedimos confirmación antes de eliminar.
    const confirmar = confirm(
        "¿Está seguro de que desea eliminar este equipo?"
    );


    // Si el usuario cancela, no hacemos nada.
    if (!confirmar) {
        return;
    }


    // Eliminamos el equipo del array.
    equipos.splice(indice, 1);


    // Guardamos nuevamente los datos.
    guardarEnLocalStorage();


    // Actualizamos la pantalla.
    mostrarEquipos();

    // Actualizamos los contadores.
    actualizarContadores();
}


/* =====================================================
   14. EXPORTAR A JSON
   ===================================================== */

btnExportar.addEventListener("click", function() {

    // Convertimos los equipos a formato JSON.
    const datosJSON = JSON.stringify(
        equipos,
        null,
        2
    );


    // Creamos un archivo en memoria.
    const archivo = new Blob(
        [datosJSON],
        {
            type: "application/json"
        }
    );


    // Creamos una dirección temporal para el archivo.
    const url = URL.createObjectURL(archivo);


    // Creamos un enlace para descargarlo.
    const enlace = document.createElement("a");

    enlace.href = url;

    enlace.download = "equipos.json";


    // Simulamos un clic para descargar.
    enlace.click();


    // Eliminamos la dirección temporal.
    URL.revokeObjectURL(url);
});


/* =====================================================
   15. IMPORTAR ARCHIVO JSON
   ===================================================== */

inputImportar.addEventListener("change", function(evento) {

    // Obtenemos el archivo seleccionado.
    const archivo = evento.target.files[0];


    // Si no se seleccionó ningún archivo,
    // terminamos la función.
    if (!archivo) {
        return;
    }


    // Creamos un lector de archivos.
    const lector = new FileReader();


    // Cuando termina de leer el archivo...
    lector.onload = function(e) {

        try {

            // Convertimos el contenido del archivo
            // desde JSON a JavaScript.
            const datosImportados =
                JSON.parse(e.target.result);


            // Comprobamos que realmente sea un array.
            if (!Array.isArray(datosImportados)) {

                alert(
                    "El archivo JSON no tiene un formato válido."
                );

                return;
            }


            // Reemplazamos los equipos actuales
            // por los datos importados.
            equipos = datosImportados;


            // Guardamos los nuevos datos.
            guardarEnLocalStorage();


            // Actualizamos la pantalla.
            mostrarEquipos();

            actualizarContadores();


            // Avisamos que la importación terminó.
            alert(
                "Los equipos fueron importados correctamente."
            );


        } catch (error) {

            // Mostramos un mensaje si el JSON
            // tiene algún problema.
            alert(
                "No se pudo importar el archivo JSON."
            );
        }
    };


    // Comenzamos a leer el archivo.
    lector.readAsText(archivo);
});


/* =====================================================
   16. MOSTRAR LOS EQUIPOS AL INICIAR
   ===================================================== */

// Mostramos los datos almacenados cuando
// se carga el JavaScript.
mostrarEquipos();

actualizarContadores();