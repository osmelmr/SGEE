// Utilidad para crear o actualizar el mensaje de error
function setError(input, message) {
    let error = input.parentNode.querySelector('.input-error');
    if (!error) {
        error = document.createElement('div');
        error.className = 'input-error';
        error.style.color = 'red';
        error.style.fontSize = '0.9em';
        error.style.marginTop = '2px';
        input.parentNode.appendChild(error);
    }
    error.textContent = message;
}

function clearError(input) {
    let error = input.parentNode.querySelector('.input-error');
    if (error) error.remove();
}

// Validaciones
function validarNombre(valor) {
    return /^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+$/.test(valor);
}

function validarSolapin(valor) {
    return /^[A-Z][0-9]{6}$/.test(valor);
}

function validarTelefono(valor) {
    return /^(\+?\d{8,14})$/.test(valor);
}

function validarUsuario(valor) {
    return /^[a-z0-9]+$/.test(valor);
}

// Función para aplicar o quitar blur
function aplicarBlur(input, activar) {
    if (activar) {
        input.style.filter = 'blur(0.2px)';
        input.style.opacity = '0.6';
        input.style.pointerEvents = 'none';
    } else {
        input.style.filter = '';
        input.style.opacity = '';
        input.style.pointerEvents = '';
    }
}

function mostrarMensajeGrupo(input, mensaje) {
    let msg = input.parentNode.querySelector('.mensaje-activar');
    if (!msg) {
        msg = document.createElement('div');
        msg.className = 'mensaje-activar';
        msg.style.color = '#333';
        msg.style.fontSize = '0.9em';
        msg.style.marginTop = '2px';
        input.parentNode.appendChild(msg);
    }
    msg.textContent = mensaje;
}

function ocultarMensajeGrupo(input) {
    let msg = input.parentNode.querySelector('.mensaje-activar');
    if (msg) msg.remove();
}

// Asignar eventos
window.addEventListener('DOMContentLoaded', function() {
    // Nombre
    const nombre = document.getElementById('nombre');
    nombre.addEventListener('input', function() {
        if (!validarNombre(nombre.value)) {
            setError(nombre, 'Debe comenzar con mayúscula y solo letras.');
        } else {
            clearError(nombre);
        }
    });

    // Primer Apellido
    const primerApellido = document.getElementById('primer-apellido');
    primerApellido.addEventListener('input', function() {
        if (!validarNombre(primerApellido.value)) {
            setError(primerApellido, 'Debe comenzar con mayúscula y solo letras.');
        } else {
            clearError(primerApellido);
        }
    });

    // Segundo Apellido
    const segundoApellido = document.getElementById('segundo-apellido');
    segundoApellido.addEventListener('input', function() {
        if (!validarNombre(segundoApellido.value)) {
            setError(segundoApellido, 'Debe comenzar con mayúscula y solo letras.');
        } else {
            clearError(segundoApellido);
        }
    });

    // Solapín
    const solapin = document.getElementById('solapin');
    solapin.addEventListener('input', function() {
        if (!validarSolapin(solapin.value)) {
            setError(solapin, 'Debe comenzar con una letra mayúscula seguida de 6 números.');
        } else {
            clearError(solapin);
        }
    });

    // Teléfono
    const telefono = document.getElementById('telefono');
    telefono.addEventListener('input', function() {
        if (!validarTelefono(telefono.value)) {
            setError(telefono, 'Debe tener entre 8 y 14 números, puede iniciar con +.');
        } else {
            clearError(telefono);
        }
    });

    // Usuario
    const usuario = document.getElementById('user');
    usuario.addEventListener('input', function() {
        if (!validarUsuario(usuario.value)) {
            setError(usuario, 'Solo minúsculas y números, sin espacios.');
        } else {
            clearError(usuario);
        }
    });

    const grupo = document.getElementById('grupo');
    const rol = document.getElementById('rol');

    function actualizarCampos() {
        if (rol.value === 'profesor_principal') {
            // Si el rol es profesor principal, desactivar grupo y limpiar selección
            grupo.value = '';
            grupo.disabled = true;
            aplicarBlur(grupo, true);
            mostrarMensajeGrupo(grupo, 'Para seleccionar un grupo, cambie el rol a "usuario".');
        } else {
            grupo.disabled = false;
            aplicarBlur(grupo, false);
            ocultarMensajeGrupo(grupo);
        }

        if (grupo.value) {
            // Si hay grupo seleccionado, rol es usuario (pero no se desactiva ni se aplica blur)
            rol.value = 'usuario';
            aplicarBlur(rol, false);
        } else {
            aplicarBlur(rol, false);
        }
    }

    grupo.addEventListener('change', actualizarCampos);
    rol.addEventListener('change', actualizarCampos);

    // Inicializar al cargar
    actualizarCampos();
});

