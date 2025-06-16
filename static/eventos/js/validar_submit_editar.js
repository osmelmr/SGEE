document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-evento');
    if (!form) return;

    const nombreEvento = document.getElementById('nombre-evento');
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    const horaInicio = document.getElementById('hora-inicio');
    const horaFin = document.getElementById('hora-fin');
    const ubicacionEvento = document.getElementById('ubicacion-evento');
    const tipoEvento = document.getElementById('tipo-evento');
    const descripcionEvento = document.getElementById('descripcion-evento');
    const profesorCargo = document.getElementById('profesor-cargo');
    const telefonoContacto = document.getElementById('telefono-contacto');

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

    form.addEventListener('submit', function(e) {
        let firstInvalid = null;

        // 1. Validaciones específicas
        // Nombre del evento
        const nombreVal = nombreEvento.value.trim();
        if (nombreVal.length < 4) {
            setError(nombreEvento, 'El nombre debe tener más de 3 caracteres.');
            if (!firstInvalid) firstInvalid = nombreEvento;
        } else if (!/^[A-ZÁÉÍÓÚÑ]/.test(nombreVal)) {
            setError(nombreEvento, 'El nombre debe comenzar con mayúscula.');
            if (!firstInvalid) firstInvalid = nombreEvento;
        } else {
            clearError(nombreEvento);
        }

        // Fechas
        const hoy = new Date();
        hoy.setHours(0,0,0,0);
        // Corregido: asegura que la fecha sea la seleccionada en el input
        const inicio = fechaInicio.value ? new Date(fechaInicio.value + 'T00:00:00') : null;
        const fin = fechaFin.value ? new Date(fechaFin.value + 'T00:00:00') : null;
        if (inicio && inicio < hoy) {
            setError(fechaInicio, 'La fecha de inicio no puede ser menor que la fecha actual.');
            if (!firstInvalid) firstInvalid = fechaInicio;
        } else {
            clearError(fechaInicio);
        }
        if (inicio && fin && fin < inicio) {
            setError(fechaFin, 'La fecha de fin no puede ser menor que la fecha de inicio.');
            if (!firstInvalid) firstInvalid = fechaFin;
        } else {
            clearError(fechaFin);
        }

        // Horas si fechas iguales
        if (fechaInicio.value && fechaFin.value && fechaInicio.value === fechaFin.value) {
            if (horaInicio.value && horaFin.value) {
                const [h1, m1] = horaInicio.value.split(':').map(Number);
                const [h2, m2] = horaFin.value.split(':').map(Number);
                const minutos1 = h1 * 60 + m1;
                const minutos2 = h2 * 60 + m2;
                if (minutos2 - minutos1 < 60) {
                    setError(horaFin, 'La hora de fin debe ser al menos 1 hora después de la hora de inicio.');
                    if (!firstInvalid) firstInvalid = horaFin;
                } else {
                    clearError(horaFin);
                }
            }
        } else {
            clearError(horaFin);
        }

        // Teléfono
        const telVal = telefonoContacto.value;
        if (!/^(\+?\d*)$/.test(telVal)) {
            setError(telefonoContacto, 'Solo se permite el símbolo + al inicio seguido de números o solo números.');
            if (!firstInvalid) firstInvalid = telefonoContacto;
        } else if (telVal.replace(/^\+/, '').length < 8) {
            setError(telefonoContacto, 'El número debe tener al menos 8 dígitos.');
            if (!firstInvalid) firstInvalid = telefonoContacto;
        } else {
            clearError(telefonoContacto);
        }

        // 2. Validar campos vacíos (solo si no hay error específico)
        const campos = [
            {input: nombreEvento, msg: 'Este campo es obligatorio.'},
            {input: fechaInicio, msg: 'Este campo es obligatorio.'},
            {input: fechaFin, msg: 'Este campo es obligatorio.'},
            {input: horaInicio, msg: 'Este campo es obligatorio.'},
            {input: horaFin, msg: 'Este campo es obligatorio.'},
            {input: ubicacionEvento, msg: 'Este campo es obligatorio.'},
            {input: tipoEvento, msg: 'Seleccione un tipo de evento.'},
            {input: descripcionEvento, msg: 'Este campo es obligatorio.'},
            {input: profesorCargo, msg: 'Seleccione un profesor.'},
            {input: telefonoContacto, msg: 'Este campo es obligatorio.'}
        ];
        for (const campo of campos) {
            if (!campo.input.value || (campo.input.tagName === 'SELECT' && campo.input.value === '')) {
                setError(campo.input, campo.msg);
                if (!firstInvalid) firstInvalid = campo.input;
            } else if (!campo.input.validationMessage) {
                clearError(campo.input);
            }
        }

        // Si hay algún error, prevenir envío y enfocar
        if (!form.checkValidity()) {
            e.preventDefault();
            if (firstInvalid) firstInvalid.focus();
        } else {
            // No hay errores: deshabilitar botón y cambiar texto
            const btnRegistrar = form.querySelector('[type="submit"], button[name="registrar"]');
            if (btnRegistrar) {
                btnRegistrar.disabled = true;
                btnRegistrar.textContent = 'Enviando...';
            }
        }
    });
});
