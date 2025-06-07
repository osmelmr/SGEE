document.addEventListener('DOMContentLoaded', function () {
    // Elementos del formulario
    const nombreEvento = document.getElementById('nombre-evento');
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    const horaInicio = document.getElementById('hora-inicio');
    const horaFin = document.getElementById('hora-fin');
    const telefonoContacto = document.getElementById('telefono-contacto');
    const ubicacionEvento = document.getElementById('ubicacion-evento');
    const descripcionEvento = document.getElementById('descripcion-evento');
    const form = document.getElementById('form-evento');

    // Función genérica para manejar mensajes de error
    function manejarMensajeDeError(campo, regex, mensajeError, permitirVacio = false) {
        let errorMessage = campo.parentNode.querySelector('.error-message');
        if (!errorMessage) {
            errorMessage = document.createElement('span');
            errorMessage.className = 'error-message';
            errorMessage.style.color = 'red';
            errorMessage.style.fontSize = '0.9em';
            errorMessage.style.display = 'none'; // Oculto por defecto
            campo.parentNode.appendChild(errorMessage);
        }

        campo.addEventListener('input', function () {
            if (this.value.trim() === '') {
                if (!permitirVacio) {
                    errorMessage.textContent = 'Este campo es obligatorio';
                    errorMessage.style.display = 'block';
                    campo.classList.add('is-invalid');
                } else {
                    errorMessage.style.display = 'none';
                    campo.classList.remove('is-invalid');
                }
            } else if (!regex.test(this.value)) {
                errorMessage.textContent = mensajeError;
                errorMessage.style.display = 'block';
                campo.classList.add('is-invalid');
            } else {
                errorMessage.style.display = 'none';
                campo.classList.remove('is-invalid');
            }
        });

        campo.addEventListener('blur', function () {
            if (this.value.trim() === '' && !permitirVacio) {
                errorMessage.textContent = 'Este campo es obligatorio';
                errorMessage.style.display = 'block';
                campo.classList.add('is-invalid');
            }
        });

        campo.addEventListener('focus', function () {
            errorMessage.style.display = 'none';
            campo.classList.remove('is-invalid');
        });
    }

    // Validaciones específicas para los campos
    manejarMensajeDeError(
        nombreEvento,
        /^[A-ZÁÉÍÓÚÑ][a-zA-ZÁÉÍÓÚÑáéíóúñ\s]{3,100}$/,
        'El nombre debe comenzar con mayúscula y tener entre 4 y 100 caracteres'
    );

    manejarMensajeDeError(
        telefonoContacto,
        /^\+?\d{8,15}$/,
        'El número debe tener entre 8 y 15 dígitos y puede comenzar con +'
    );

    manejarMensajeDeError(
        ubicacionEvento,
        /^.{5,100}$/,
        'Debe tener entre 5 y 100 caracteres'
    );

    manejarMensajeDeError(
        descripcionEvento,
        /^.{10,1000}$/,
        'Debe tener entre 10 y 1000 caracteres'
    );

    // Validación específica para fechas
    function validarFechaCampo(campo, mensajeError) {
        let errorMessage = campo.parentNode.querySelector('.error-message');
        if (!errorMessage) {
            errorMessage = document.createElement('span');
            errorMessage.className = 'error-message';
            errorMessage.style.color = 'red';
            errorMessage.style.fontSize = '0.9em';
            errorMessage.style.display = 'none';
            campo.parentNode.appendChild(errorMessage);
        }

        if (campo.value.trim() === '') {
            errorMessage.textContent = 'Este campo es obligatorio';
            errorMessage.style.display = 'block';
            campo.classList.add('is-invalid');
            return false; // Detenemos aquí si el campo está vacío
        } else {
            errorMessage.style.display = 'none';
            campo.classList.remove('is-invalid');
            return true; // Continuamos si el campo no está vacío
        }
    }

    function validarLogicaFechas() {
        if (!validarFechaCampo(fechaInicio, 'Este campo es obligatorio') ||
            !validarFechaCampo(fechaFin, 'Este campo es obligatorio')) {
            return;
        }

        const inicio = new Date(fechaInicio.value + 'T00:00:00');
        const fin = new Date(fechaFin.value + 'T00:00:00');

        if (fin < inicio) {
            setError(fechaFin, 'La fecha de fin no puede ser menor que la fecha de inicio.');
        } else {
            clearError(fechaFin);
        }

        // Si las fechas son diferentes, limpiar errores de horas
        if (inicio.getTime() !== fin.getTime()) {
            clearError(horaInicio);
            clearError(horaFin);
        }
    }

    function validarLogicaHoras() {
        if (!validarFechaCampo(horaInicio, 'Este campo es obligatorio') ||
            !validarFechaCampo(horaFin, 'Este campo es obligatorio')) {
            return;
        }

        const [h1, m1] = horaInicio.value.split(':').map(Number);
        const [h2, m2] = horaFin.value.split(':').map(Number);
        const minutos1 = h1 * 60 + m1;
        const minutos2 = h2 * 60 + m2;

        // Validar solo si las fechas son iguales
        if (fechaInicio.value === fechaFin.value) {
            if (minutos2 - minutos1 < 60) {
                setError(horaFin, 'La hora de fin debe ser al menos 1 hora después de la hora de inicio.');
            } else {
                clearError(horaFin);
            }
        } else {
            clearError(horaFin); // Limpiar errores si las fechas son diferentes
        }
    }

    fechaInicio.addEventListener('input', function () {
        validarLogicaFechas();
        validarLogicaHoras(); // Forzar validación de horas al cambiar la fecha
    });

    fechaFin.addEventListener('input', function () {
        validarLogicaFechas();
        validarLogicaHoras(); // Forzar validación de horas al cambiar la fecha
    });

    horaInicio.addEventListener('blur', validarLogicaHoras);
    horaFin.addEventListener('blur', validarLogicaHoras);

    // Validación final al enviar
    form.addEventListener('submit', function (e) {
        validarLogicaFechas();
        validarLogicaHoras();
        if (!form.checkValidity()) {
            e.preventDefault();
        }
    });

    // Funciones auxiliares para manejar errores
    function setError(input, message) {
        let errorMessage = input.parentNode.querySelector('.error-message');
        if (!errorMessage) {
            errorMessage = document.createElement('span');
            errorMessage.className = 'error-message';
            errorMessage.style.color = 'red';
            errorMessage.style.fontSize = '0.9em';
            input.parentNode.appendChild(errorMessage);
        }
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        input.classList.add('is-invalid');
    }

    function clearError(input) {
        let errorMessage = input.parentNode.querySelector('.error-message');
        if (errorMessage) {
            errorMessage.textContent = '';
            errorMessage.style.display = 'none';
        }
        input.classList.remove('is-invalid');
    }
});