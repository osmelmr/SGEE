document.addEventListener('DOMContentLoaded', function () {
    const nombreInput = document.getElementById('nombre');
    const anioEscolarSelect = document.getElementById('anio_escolar');
    const direccionInput = document.getElementById('direccion');
    const cursoSelect = document.getElementById('curso');
    const caracterizacionInput = document.getElementById('caracterizacion');
    const guiaSelect = document.getElementById('guia');
    const profesoresChecks = document.querySelectorAll('input[name="profesores"]');
    const form = document.querySelector('form');

    const prefijos = {
        'primero': '1',
        'segundo': '2',
        'tercero': '3',
        'cuarto': '4'
    };

    const prefijoToAnio = {
        '1': 'primero',
        '2': 'segundo',
        '3': 'tercero',
        '4': 'cuarto'
    };

    function mostrarError(input, mensaje) {
        let parent = input.closest('.mb-3') || input.parentNode;
        let errorElem = parent.querySelector('.error-validacion');
        if (!errorElem) {
            errorElem = document.createElement('span');
            errorElem.className = 'error-validacion';
            parent.appendChild(errorElem);
        }
        errorElem.textContent = mensaje || '';
        if (mensaje) {
            input.classList.add('is-invalid');
            input.classList.remove('is-valid');
            errorElem.style.display = 'block';
        } else {
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
            errorElem.style.display = 'none';
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

    function validarNombreYActualizarAnio() {
        const valor = nombreInput.value.trim();
        if (!valor) {
            mostrarError(nombreInput, 'Este campo es obligatorio.');
            return false;
        }
        const match = valor.match(/^([A-ZÁÉÍÓÚÑ]{3,})(\d{3})$/);
        if (match) {
            const primerDigito = match[2].charAt(0);
            if (prefijoToAnio[primerDigito]) {
                anioEscolarSelect.value = prefijoToAnio[primerDigito];
            }
            mostrarError(nombreInput, '');
            return true;
        } else {
            mostrarError(nombreInput, 'El nombre debe tener al menos 3 letras mayúsculas seguidas de 3 números.');
            return false;
        }
    }

    function actualizarNombrePorAnio() {
        const valor = nombreInput.value.trim();
        const anio = anioEscolarSelect.value;
        if (!anio || !prefijos[anio]) return;
        const match = valor.match(/^([A-ZÁÉÍÓÚÑ]{3,})(\d)(\d{2})$/);
        if (match) {
            nombreInput.value = match[1] + prefijos[anio] + match[3];
        } else if (valor.match(/^[A-ZÁÉÍÓÚÑ]{3,}$/)) {
            nombreInput.value = valor + prefijos[anio] + '00';
        }
        validarNombreYActualizarAnio();
    }

    function validarDireccion() {
        const valor = direccionInput.value.trim();
        if (!valor) {
            mostrarError(direccionInput, 'Este campo es obligatorio.');
            return false;
        }
        const regex = /^([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$/;
        if (regex.test(valor)) {
            mostrarError(direccionInput, '');
            return true;
        } else {
            mostrarError(direccionInput, 'Debe ingresar al menos dos palabras, cada una iniciando con mayúscula.');
            return false;
        }
    }

    function validarCampoVacio(input, mensaje) {
        const valor = input.value.trim();
        if (!valor) {
            mostrarError(input, mensaje || 'Este campo es obligatorio.');
            return false;
        } else {
            mostrarError(input, '');
            return true;
        }
    }

    function validarProfesoresSeleccionados() {
        let algunoSeleccionado = false;
        profesoresChecks.forEach(chk => {
            if (chk.checked) algunoSeleccionado = true;
        });
        if (!algunoSeleccionado) {
            mostrarErrorProfesores('Debe seleccionar al menos un profesor.');
            return false;
        } else {
            mostrarErrorProfesores('');
            return true;
        }
    }

    function validarFormulario() {
        let valido = true;
        if (!validarNombreYActualizarAnio()) valido = false;
        if (!validarDireccion()) valido = false;
        if (!validarCampoVacio(cursoSelect, 'Debe seleccionar un curso.')) valido = false;
        if (!validarCampoVacio(anioEscolarSelect, 'Debe seleccionar un año escolar.')) valido = false;
        if (!validarCampoVacio(caracterizacionInput, 'Debe completar la caracterización.')) valido = false;
        if (!validarCampoVacio(guiaSelect, 'Debe seleccionar un guía.')) valido = false;
        if (!validarProfesoresSeleccionados()) valido = false;
        return valido;
    }

    if (nombreInput && anioEscolarSelect) {
        nombreInput.addEventListener('blur', validarNombreYActualizarAnio);
        anioEscolarSelect.addEventListener('change', function () {
            actualizarNombrePorAnio();
            validarCampoVacio(anioEscolarSelect);
        });
    }
    if (direccionInput) {
        direccionInput.addEventListener('blur', validarDireccion);
    }
    if (cursoSelect) {
        cursoSelect.addEventListener('change', function () {
            validarCampoVacio(cursoSelect, 'Debe seleccionar un curso.');
        });
    }
    if (caracterizacionInput) {
        caracterizacionInput.addEventListener('blur', function () {
            validarCampoVacio(caracterizacionInput, 'Debe completar la caracterización.');
        });
    }
    if (guiaSelect) {
        guiaSelect.addEventListener('change', function () {
            validarCampoVacio(guiaSelect, 'Debe seleccionar un guía.');
        });
    }
    profesoresChecks.forEach(chk => {
        chk.addEventListener('change', validarProfesoresSeleccionados);
    });

    form.addEventListener('submit', function (e) {
        if (!validarFormulario()) {
            e.preventDefault();
        }
    });
});