document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("form-registro");

    // Función para mostrar errores
    function mostrarError(input, mensaje) {
        let parent = input.closest(".form-group") || input.parentNode;
        let errorElem = parent.querySelector(".error-validacion");
        if (!errorElem) {
            errorElem = document.createElement("span");
            errorElem.className = "error-validacion";
            parent.appendChild(errorElem);
        }
        if (mensaje) {
            errorElem.textContent = mensaje;
            errorElem.style.display = "block";
            input.classList.add("is-invalid");
            input.classList.remove("is-valid");
        } else {
            errorElem.textContent = "";
            errorElem.style.display = "none";
            input.classList.remove("is-invalid");
            input.classList.add("is-valid");
        }
    }

    // Validar campo obligatorio
    function validarCampoObligatorio(input) {
        if (!input.value.trim()) {
            mostrarError(input, "Este campo es obligatorio.");
            return false;
        } else {
            mostrarError(input, "");
            return true;
        }
    }

    // Validar campo con expresión regular
    function validarCampo(input, regex, mensajeError) {
        if (!input.value.trim()) {
            mostrarError(input, "Este campo es obligatorio.");
            return false;
        } else if (regex && !regex.test(input.value)) {
            mostrarError(input, mensajeError);
            return false;
        } else {
            mostrarError(input, "");
            return true;
        }
    }

    // Validaciones específicas para cada campo
    function validarNombre(input) {
        const regex = /^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+$/;
        return validarCampo(input, regex, "Debe comenzar con una letra mayúscula y solo contener letras.");
    }

    function validarSolapin(input) {
        const regex = /^[A-Z]\d{6}$/;
        return validarCampo(input, regex, "Debe comenzar con una letra mayúscula seguida de 6 números.");
    }

    function validarTelefono(input) {
        const regex = /^\+?\d{8,15}$/;
        return validarCampo(input, regex, "Debe contener entre 8 y 15 dígitos, y puede comenzar con '+'.");
    }

    function validarCorreo(input) {
        const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return validarCampo(input, regex, "Debe ser un correo válido (ejemplo@dominio.com).");
    }

    function validarUsuario(input) {
        const regex = /^[a-z]{1,5}$/;
        return validarCampo(input, regex, "Debe contener solo letras minúsculas y no más de 5 caracteres.");
    }

    function validarPassword(input) {
        const regex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
        return validarCampo(input, regex, "Debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial.");
    }

    function validarSelect(input) {
        if (!input.value.trim()) {
            mostrarError(input, "Este campo es obligatorio.");
            return false;
        } else {
            mostrarError(input, "");
            return true;
        }
    }

    // Asociar eventos de validación a los campos
    const nombre = document.getElementById("nombre");
    const primerApellido = document.getElementById("primer-apellido");
    const segundoApellido = document.getElementById("segundo-apellido");
    const solapin = document.getElementById("solapin");
    const telefono = document.getElementById("telefono");
    const correo = document.getElementById("correo");
    const usuario = document.getElementById("user");
    const password = document.getElementById("password");
    const selectRol = document.getElementById("rol"); // Campo select para rol
    const selectGrupo = document.getElementById("grupo"); // Campo select para grupo
    const selectSexo = document.getElementById("sexo"); // Campo select para sexo

    if (nombre) nombre.addEventListener("blur", () => validarNombre(nombre));
    if (primerApellido) primerApellido.addEventListener("blur", () => validarNombre(primerApellido));
    if (segundoApellido) segundoApellido.addEventListener("blur", () => validarNombre(segundoApellido));
    if (solapin) solapin.addEventListener("blur", () => validarSolapin(solapin));
    if (telefono) telefono.addEventListener("blur", () => validarTelefono(telefono));
    if (correo) correo.addEventListener("blur", () => validarCorreo(correo));
    if (usuario) usuario.addEventListener("blur", () => validarUsuario(usuario));
    if (password) password.addEventListener("blur", () => validarPassword(password));
    if (selectRol) selectRol.addEventListener("blur", () => validarSelect(selectRol));
    if (selectGrupo) selectGrupo.addEventListener("blur", () => validarSelect(selectGrupo));
    if (selectSexo) selectSexo.addEventListener("blur", () => validarSelect(selectSexo));

    // Validar al enviar el formulario
    form.addEventListener("submit", function (event) {
        let isValid = true;

        // Validar cada campo
        if (nombre && !validarNombre(nombre)) isValid = false;
        if (primerApellido && !validarNombre(primerApellido)) isValid = false;
        if (segundoApellido && !validarNombre(segundoApellido)) isValid = false;
        if (solapin && !validarSolapin(solapin)) isValid = false;
        if (telefono && !validarTelefono(telefono)) isValid = false;
        if (correo && !validarCorreo(correo)) isValid = false;
        if (usuario && !validarUsuario(usuario)) isValid = false;
        if (password && !validarPassword(password)) isValid = false;
        if (selectRol && !validarSelect(selectRol)) isValid = false;
        if (selectGrupo && !validarSelect(selectGrupo)) isValid = false;
        if (selectSexo && !validarSelect(selectSexo)) isValid = false;

        // Prevenir el envío si hay errores
        if (!isValid) {
            event.preventDefault();
            alert("Por favor, corrija los errores antes de enviar el formulario.");
        }
    });
});

