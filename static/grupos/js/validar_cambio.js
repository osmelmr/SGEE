let validarFormulario = null; // Declarar la función para que sea accesible globalmente
document.addEventListener('DOMContentLoaded', function () {
    const nombreInput = document.getElementById('nombre');
    const anioEscolarSelect = document.getElementById('anio_escolar');
    const direccionInput = document.getElementById('direccion');
    const cursoSelect = document.getElementById('curso');
    const caracterizacionInput = document.getElementById('caracterizacion');
    const guiaSelect = document.getElementById('guia');
    // Profesores checkboxes
    const profesoresChecks = document.querySelectorAll('input[name="profesores"]');

    // Prefijos por año escolar (solo el primer dígito)
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
        // Busca el contenedor de los checkboxes
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
            nombreInput.setCustomValidity('Este campo es obligatorio.');
            nombreInput.reportValidity();
            return false;
        }
        // Regex: 3+ mayúsculas seguidas de 3 dígitos
        const match = valor.match(/^([A-ZÁÉÍÓÚÑ]{3,})(\d{3})$/);
        if (match) {
            const letras = match[1];
            const numeros = match[2];
            const primerDigito = numeros.charAt(0);
            if (prefijoToAnio[primerDigito]) {
                anioEscolarSelect.value = prefijoToAnio[primerDigito];
            }
            mostrarError(nombreInput, '');
            nombreInput.setCustomValidity('');
            return true;
        } else {
            const msg = 'El nombre debe tener al menos 3 letras mayúsculas seguidas de 3 números. El primer dígito indica el año escolar.';
            mostrarError(nombreInput, msg);
            nombreInput.setCustomValidity(msg);
            nombreInput.reportValidity();
            return false;
        }
    }

    function actualizarNombrePorAnio() {
        const valor = nombreInput.value.trim();
        const anio = anioEscolarSelect.value;
        if (!anio || !prefijos[anio]) return;
        // Si el nombre ya tiene letras y 3 números, reemplaza solo el primer dígito
        const match = valor.match(/^([A-ZÁÉÍÓÚÑ]{3,})(\d)(\d{2})$/);
        if (match) {
            nombreInput.value = match[1] + prefijos[anio] + match[3];
        } else if (valor.match(/^[A-ZÁÉÍÓÚÑ]{3,}$/)) {
            // Si solo hay letras, añade el prefijo y dos ceros
            nombreInput.value = valor + prefijos[anio] + '00';
        }
        validarNombreYActualizarAnio();
    }

    function validarDireccion() {
        if (!direccionInput) return false;
        const valor = direccionInput.value.trim();
        if (!valor) {
            mostrarError(direccionInput, 'Este campo es obligatorio.');
            direccionInput.setCustomValidity('Este campo es obligatorio.');
            direccionInput.reportValidity();
            return false;
        }
        // Debe ser al menos dos palabras, cada una con mayúscula inicial y minúsculas después
        const regex = /^([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)(\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+$/;
        if (regex.test(valor)) {
            mostrarError(direccionInput, '');
            direccionInput.setCustomValidity('');
            return true;
        } else {
            const msg = 'Debe ingresar un nombre y apellidos válidos, cada uno iniciando con mayúscula.';
            mostrarError(direccionInput, msg);
            direccionInput.setCustomValidity(msg);
            direccionInput.reportValidity();
            return false;
        }
    }

    function validarCampoVacio(input, mensaje) {
        if (!input) return false;
        const valor = input.value.trim();
        if (!valor) {
            mostrarError(input, mensaje || 'Este campo es obligatorio.');
            input.setCustomValidity(mensaje || 'Este campo es obligatorio.');
            input.reportValidity();
            return false;
        } else {
            mostrarError(input, '');
            input.setCustomValidity('');
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

    validarFormulario=()=> {
        let valido = true;
        if (!validarNombreYActualizarAnio()) valido = false;
        if (!validarDireccion()) valido = false;
        if (!validarCampoVacio(cursoSelect)) valido = false;
        if (!validarCampoVacio(anioEscolarSelect)) valido = false;
        if (!validarCampoVacio(caracterizacionInput)) valido = false;
        if (!validarCampoVacio(guiaSelect, 'Debe seleccionar un guía.')) valido = false;
        if (!validarProfesoresSeleccionados()) valido = false;
        return valido;
    }

    if (nombreInput && anioEscolarSelect) {
        nombreInput.addEventListener('input', function() {
            validarNombreYActualizarAnio();
        });
        anioEscolarSelect.addEventListener('change', function() {
            actualizarNombrePorAnio();
            validarCampoVacio(anioEscolarSelect);
        });
    }
    if (direccionInput) {
        direccionInput.addEventListener('input', validarDireccion);
    }
    if (cursoSelect) {
        cursoSelect.addEventListener('change', function() {
            validarCampoVacio(cursoSelect);
        });
    }
    if (caracterizacionInput) {
        caracterizacionInput.addEventListener('input', function() {
            validarCampoVacio(caracterizacionInput);
        });
    }
    if (guiaSelect) {
        guiaSelect.addEventListener('change', function() {
            validarCampoVacio(guiaSelect, 'Debe seleccionar un guía.');
        });
    }
    profesoresChecks.forEach(chk => {
        chk.addEventListener('change', validarProfesoresSeleccionados);
    });
});