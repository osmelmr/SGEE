document.addEventListener('DOMContentLoaded', function() {
    // Elementos del formulario
    const nombreEvento = document.getElementById('nombre-evento');
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    const horaInicio = document.getElementById('hora-inicio');
    const horaFin = document.getElementById('hora-fin');
    const telefonoContacto = document.getElementById('telefono-contacto');
    const ubicacionEvento = document.getElementById('ubicacion-evento');
    const tipoEvento = document.getElementById('tipo-evento');
    const descripcionEvento = document.getElementById('descripcion-evento');
    const profesorCargo = document.getElementById('profesor-cargo');
    const form = document.getElementById('form-evento');

    // Helper para mostrar mensajes de error debajo del input
    function showErrorBelow(input, message) {
        let errorDiv = input.parentNode.querySelector('.invalid-feedback');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.className = 'invalid-feedback';
            input.parentNode.appendChild(errorDiv);
        }
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
        input.classList.add('is-invalid');
    }
    function hideErrorBelow(input) {
        let errorDiv = input.parentNode.querySelector('.invalid-feedback');
        if (errorDiv) {
            errorDiv.textContent = '';
            errorDiv.style.display = 'none';
        }
        input.classList.remove('is-invalid');
    }
    function setError(input, message) {
        input.setCustomValidity(message);
        showErrorBelow(input, message);
        input.reportValidity();
    }
    function clearError(input) {
        input.setCustomValidity('');
        hideErrorBelow(input);
    }

    // Validar nombre del evento
    nombreEvento.addEventListener('input', function() {
        const value = nombreEvento.value.trim();
        if (value.length === 0) {
            setError(nombreEvento, 'Este campo es obligatorio.');
        } else if (value.length < 4) {
            setError(nombreEvento, 'El nombre debe tener más de 3 caracteres.');
        } else if (!/^[A-ZÁÉÍÓÚÑ]/.test(value)) {
            setError(nombreEvento, 'El nombre debe comenzar con mayúscula.');
        } else {
            clearError(nombreEvento);
        }
    });

    // Validar fecha de inicio
    fechaInicio.addEventListener('input', function() {
        if (!fechaInicio.value) {
            setError(fechaInicio, 'Este campo es obligatorio.');
            fechaFin.dispatchEvent(new Event('input'));
            return;
        }
        const hoy = new Date();
        hoy.setHours(0,0,0,0);
        const inicio = fechaInicio.value ? new Date(fechaInicio.value + 'T00:00:00') : null;
        if (inicio < hoy) {
            setError(fechaInicio, 'La fecha de inicio no puede ser menor que la fecha actual.');
        } else {
            clearError(fechaInicio);
        }
        fechaFin.dispatchEvent(new Event('input'));
    });

    // Validar fecha de fin
    fechaFin.addEventListener('input', function() {
        if (!fechaFin.value) {
            setError(fechaFin, 'Este campo es obligatorio.');
            return;
        }
        if (!fechaInicio.value) {
            clearError(fechaFin);
            return;
        }
        const inicio = new Date(fechaInicio.value + 'T00:00:00');
        const fin = new Date(fechaFin.value + 'T00:00:00');
        if (fin < inicio) {
            setError(fechaFin, 'La fecha de fin no puede ser menor que la fecha de inicio.');
        } else {
            clearError(fechaFin);
        }
        if (fechaInicio.value === fechaFin.value) {
            horaInicio.dispatchEvent(new Event('input'));
            horaFin.dispatchEvent(new Event('input'));
        }
    });

    // Validar horas si las fechas son iguales
    function validarHoras() {
        if (!horaInicio.value) {
            setError(horaInicio, 'Este campo es obligatorio.');
        } else {
            clearError(horaInicio);
        }
        if (!horaFin.value) {
            setError(horaFin, 'Este campo es obligatorio.');
            return;
        }
        if (fechaInicio.value && fechaFin.value && fechaInicio.value === fechaFin.value) {
            if (horaInicio.value && horaFin.value) {
                const [h1, m1] = horaInicio.value.split(':').map(Number);
                const [h2, m2] = horaFin.value.split(':').map(Number);
                const minutos1 = h1 * 60 + m1;
                const minutos2 = h2 * 60 + m2;
                if (minutos2 - minutos1 < 60) {
                    setError(horaFin, 'La hora de fin debe ser al menos 1 hora después de la hora de inicio.');
                } else {
                    clearError(horaFin);
                }
            }
        } else {
            if (horaFin.value) clearError(horaFin);
        }
    }
    horaInicio.addEventListener('input', validarHoras);
    horaFin.addEventListener('input', validarHoras);

    // Validar teléfono
    telefonoContacto.addEventListener('input', function() {
        const value = telefonoContacto.value;
        if (value.length === 0) {
            setError(telefonoContacto, 'Este campo es obligatorio.');
        } else if (!/^(\+?\d*)$/.test(value)) {
            setError(telefonoContacto, 'Solo se permite el símbolo + al inicio seguido de números o solo números.');
        } else if (value.replace(/^\+/, '').length < 8) {
            setError(telefonoContacto, 'El número debe tener al menos 8 dígitos.');
        } else {
            clearError(telefonoContacto);
        }
    });

    // Validar ubicación
    ubicacionEvento.addEventListener('input', function() {
        const value = ubicacionEvento.value.trim();
        if (value.length === 0) {
            setError(ubicacionEvento, 'Este campo es obligatorio.');
        } else {
            clearError(ubicacionEvento);
        }
    });

    // Validar tipo de evento
    tipoEvento.addEventListener('change', function() {
        if (!tipoEvento.value) {
            setError(tipoEvento, 'Este campo es obligatorio.');
        } else {
            clearError(tipoEvento);
        }
    });

    // Validar descripción
    descripcionEvento.addEventListener('input', function() {
        const value = descripcionEvento.value.trim();
        if (value.length === 0) {
            setError(descripcionEvento, 'Este campo es obligatorio.');
        } else {
            clearError(descripcionEvento);
        }
    });

    // Validar profesor a cargo
    profesorCargo.addEventListener('change', function() {
        if (!profesorCargo.value) {
            setError(profesorCargo, 'Este campo es obligatorio.');
        } else {
            clearError(profesorCargo);
        }
    });

    // Validación final al enviar
    form.addEventListener('submit', function(e) {
        // Forzar validaciones input
        nombreEvento.dispatchEvent(new Event('input'));
        fechaInicio.dispatchEvent(new Event('input'));
        fechaFin.dispatchEvent(new Event('input'));
        horaInicio.dispatchEvent(new Event('input'));
        horaFin.dispatchEvent(new Event('input'));
        telefonoContacto.dispatchEvent(new Event('input'));
        ubicacionEvento.dispatchEvent(new Event('input'));
        tipoEvento.dispatchEvent(new Event('change'));
        descripcionEvento.dispatchEvent(new Event('input'));
        profesorCargo.dispatchEvent(new Event('change'));
        // Si algún campo es inválido, prevenir envío
        if (!form.checkValidity()) {
            e.preventDefault();
        }
    });
});