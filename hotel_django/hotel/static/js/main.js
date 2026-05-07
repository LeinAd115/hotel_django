$(document).ready(function(){

    // HOVER EN CARDS
    $(".card").hover(
        function(){
            $(this).css("transform", "scale(1.05)");
        },
        function(){
            $(this).css("transform", "scale(1)");
        }
    );

    // MENSAJE HEADER
    $("header h1").click(function(){
        alert("Bienvenido a Hotel Quinta Dalam");
    });

    // VALIDACIÓN GENERAL
    $("form").submit(function(e){

        let valido = true;

        $(this).find("input, select, textarea").each(function(){

            if($(this).prop("required") && $(this).val() === ""){
                valido = false;
                $(this).css("border", "2px solid red");
            } else {
                $(this).css("border", "1px solid #ccc");
            }

        });

        if(!valido){
            e.preventDefault();
            alert("Completa todos los campos");
        }

    });

    // VALIDAR EMAIL
    $("#correo").on("input", function(){
        let email = $(this).val();

        if(!email.includes("@")){
            $(this).css("border", "2px solid red");
        } else {
            $(this).css("border", "2px solid green");
        }
    });

    // VALIDACIÓN FECHAS
    $("#formReservacion").submit(function(e){

        let entrada = $("#entrada").val();
        let salida = $("#salida").val();

        let fechaEntrada = new Date(entrada);
        let fechaSalida = new Date(salida);

        if(salida && entrada && fechaSalida <= fechaEntrada){
            e.preventDefault();
            $("#error-fecha").text("La fecha de salida debe ser mayor a la de entrada");
            $("#salida").css("border", "2px solid red");
        } else {
            $("#error-fecha").text("");
            $("#salida").css("border", "1px solid #ccc");
        }

    });

    $("#salida").on("change", function(){

        let entrada = $("#entrada").val();
        let salida = $(this).val();

        let fechaEntrada = new Date(entrada);
        let fechaSalida = new Date(salida);

        if(salida && entrada && fechaSalida <= fechaEntrada){
            $("#error-fecha").text("Fecha inválida");
            $(this).val("");
        } else {
            $("#error-fecha").text("");
        }

    });

    $("#entrada").on("change", function(){
        let entrada = $(this).val();
        $("#salida").attr("min", entrada);
    });

    // VALIDAR NOMBRE
    $("#nombre").on("input", function(){

        let nombre = $(this).val();
        let regex = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;

        if(!regex.test(nombre) || nombre.trim().split(" ").length < 2){
            $(this).css("border", "2px solid red");
            $("#error-nombre").text("Ingrese nombre y apellido válidos");
        } else {
            $(this).css("border", "2px solid green");
            $("#error-nombre").text("");
        }

    });

    // VALIDAR PRECIO
    $("#precio").on("input", function(){

        let precio = parseFloat($(this).val());

        if(precio <= 0 || isNaN(precio)){
            $(this).css("border", "2px solid red");
            $("#error-precio").text("Ingrese un precio válido mayor a 0");
        } else {
            $(this).css("border", "2px solid green");
            $("#error-precio").text("");
        }

    });

    if ($("body").hasClass("inicio")) {
        $(".hero").hide().fadeIn(1200);
    }

    $(".servicio").each(function(index){

        let servicio = $(this);

        setTimeout(function(){
            servicio.addClass("visible");
        }, index * 400);

    });

});

// AUTOLLENAR HABITACIÓN
document.addEventListener("DOMContentLoaded", function () {

    const params = new URLSearchParams(window.location.search);
    const habitacion = params.get("habitacion");

    if (habitacion) {
        const select = document.getElementById("tipo");
        if (select) select.value = habitacion;
    }

});

// ALTA HABITACIÓN
document.addEventListener("DOMContentLoaded", function () {

    const btnAlta = document.getElementById("btnAlta");

    if (btnAlta) {
        btnAlta.addEventListener("click", function () {

            const fileInput = document.getElementById("imagenFile");
            const urlInput = document.getElementById("imagenURL").value;

            if (fileInput.files.length > 0) {
                const reader = new FileReader();

                reader.onload = function (e) {
                    guardarHabitacion(e.target.result);
                };

                reader.readAsDataURL(fileInput.files[0]);

            } else {
                guardarHabitacion(urlInput);
            }

            function guardarHabitacion(imagen) {

                const habitacion = {
                    id: document.getElementById("id").value,
                    nombre: document.getElementById("nombre").value,
                    descripcion: document.getElementById("descripcion").value,
                    precio: document.getElementById("precio").value,
                    tipo: document.getElementById("tipo").value,
                    imagen: imagen
                };

                let habitaciones = JSON.parse(localStorage.getItem("habitaciones")) || [];

                habitaciones.push(habitacion);

                localStorage.setItem("habitaciones", JSON.stringify(habitaciones));

                alert("Habitación guardada 😎");
            }

        });
    }

});

// MOSTRAR CATÁLOGO
document.addEventListener("DOMContentLoaded", function () {

    const contenedor = document.getElementById("catalogo");

    if (contenedor) {

        let habitaciones = JSON.parse(localStorage.getItem("habitaciones")) || [];

        habitaciones.forEach(hab => {

            const card = document.createElement("a");
            card.classList.add("card");
            card.href = `reservacion.html?habitacion=${hab.nombre}`;

            card.innerHTML = `
                <img src="${hab.imagen}" alt="${hab.nombre}">
                <div class="card-content">
                    <h3>${hab.nombre}</h3>
                    <p>${hab.descripcion}</p>
                    <p class="precio">$${hab.precio} MXN / noche</p>
                </div>
            `;

            contenedor.appendChild(card);
        });
    }

});

// ELIMINAR HABITACIÓN
document.addEventListener("DOMContentLoaded", function () {

    const btnEliminar = document.getElementById("btnEliminar");

    if (btnEliminar) {
        btnEliminar.addEventListener("click", function () {

            const id = document.getElementById("id").value.trim();

            if (!id) {
                alert("Ingresa un ID para eliminar");
                return;
            }

            let habitaciones = JSON.parse(localStorage.getItem("habitaciones")) || [];

            const existe = habitaciones.some(hab => String(hab.id) === String(id));

            if (!existe) {
                alert("No existe una habitación con ese ID");
                return;
            }

            if (!confirm("¿Seguro que quieres eliminar esta habitación?")) return;

            habitaciones = habitaciones.filter(hab => String(hab.id) !== String(id));

            localStorage.setItem("habitaciones", JSON.stringify(habitaciones));

            alert("Habitación eliminada correctamente");

            document.getElementById("id").value = "";

        });
    }

});