document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form-grupo');
    if (!form) return;

    const submitBtn = form.querySelector('[type="submit"], button[type="submit"]');
    const nombreInput = document.getElementById('nombre');
    const direccionInput = document.getElementById('direccion');
    const cursoSelect = document.getElementById('curso');
    const caracterizacionInput = document.getElementById('caracterizacion');
    const guiaSelect = document.getElementById('guia');
    const profesoresChecks = document.querySelectorAll('input[name="profesores"]');

    function mostrarError(input, mensaje) {
        let parent = input.closest('.mb-3') || input.parentNode;
        let errorElem = parent.querySelector('.error-validacion');
        if (!errorElem) {
            errorElem = document.createElement('span');
            errorElem.className = 'error-validacion';
            parent.appendChild(errorElem);
        }
        errorElem.textContent = mensaje || '';
        errorElem.style.display = mensaje ? 'block' : 'none';
        if (mensaje) {
            input.classList.add('is-invalid');
            input.classList.remove('is-valid');
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
        }
    }

    function mostrarErrorProfesores(mensaje) {
        const profesoresContainer = profesoresChecks.length ? profesoresChecks[0].closest('.mb-3') || profesoresChecks[0].parentNode.parentNode : null;
        if (!profesoresContainer) return;
        let errorElem = profesoresContainer.querySelector('.error-validacion');
        if (!errorElem) {
            errorElem = document.createElement('span');
            errorElem.className = 'error-validacion';
            profesoresContainer.appendChild(errorElem);
        }
        errorElem.textContent = mensaje || '';
        errorElem.style.display = mensaje ? 'block' : 'none';
    }

    function validarNombre() {
        if (!nombreInput) return false;
        const valor = nombreInput.value.trim();
        if (!valor) {
            mostrarError(nombreInput, 'Este campo es obligatorio.');
            return false;
        }
        const match = valor.match(/^([A-ZÁÉÍÓÚÑ]{3,})(\d{3})$/);
        if (!match) {
            mostrarError(nombreInput, 'El nombre debe tener al menos 3 letras mayúsculas seguidas de 3 números.');
            return false;
        }
        mostrarError(nombreInput, '');
        return true;
    }

    function validarDireccion() {
        if (!direccionInput) return false;
        const valor = direccionInput.value.trim();
        if (!valor) {
            mostrarError(direccionInput, 'Este campo es obligatorio.');
            return false;
        }
        const regex = /^([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$/;
        if (!regex.test(valor)) {
            mostrarError(direccionInput, 'Debe ingresar un nombre y apellidos válidos, cada uno iniciando con mayúscula.');
            return false;
        }
        mostrarError(direccionInput, '');
        return true;
    }

    function validarCampoVacio(input, mensaje) {
        if (!input) return false;
        const valor = input.value.trim();
        if (!valor) {
            mostrarError(input, mensaje || 'Este campo es obligatorio.');
            return false;
        }
        mostrarError(input, '');
        return true;
    }

    function validarProfesores() {
        let algunoSeleccionado = false;
        profesoresChecks.forEach(chk => {
            if (chk.checked) algunoSeleccionado = true;
        });
        if (!algunoSeleccionado) {
            mostrarErrorProfesores('Debe seleccionar al menos un profesor.');
            return false;
        }
        mostrarErrorProfesores('');
        return true;
    }

    function validarFormulario() {
        let valido = true;
        let primerError = null;

        if (!validarNombre()) {
            valido = false;
            if (!primerError) primerError = nombreInput;
        }
        if (!validarDireccion()) {
            valido = false;
            if (!primerError) primerError = direccionInput;
        }
        if (!validarCampoVacio(cursoSelect)) {
            valido = false;
            if (!primerError) primerError = cursoSelect;
        }
        if (!validarCampoVacio(caracterizacionInput)) {
            valido = false;
            if (!primerError) primerError = caracterizacionInput;
        }
        if (!validarCampoVacio(guiaSelect, 'Debe seleccionar un guía.')) {
            valido = false;
            if (!primerError) primerError = guiaSelect;
        }
        if (!validarProfesores()) {
            valido = false;
            if (!primerError && profesoresChecks.length) primerError = profesoresChecks[0];
        }

        if (primerError && typeof primerError.focus === 'function') {
            primerError.focus();
        }

        return valido;
    }

    form.addEventListener('submit', function (e) {
        if (submitBtn) submitBtn.disabled = true;
        if (!validarFormulario()) {
            e.preventDefault();
            e.stopPropagation();
            if (submitBtn) submitBtn.disabled = false;
        }
    });
});

console.log('validar_submit.js cargado');