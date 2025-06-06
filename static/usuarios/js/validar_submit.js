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
function validarContrasena(valor) {
    return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(valor);
}
function validarCorreo(valor) {
    return /^[a-zA-Z0-9._%+-]+@uci\.cu$/.test(valor);
}

window.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-registro');
    const submitBtn = document.getElementById('boton-registrar-usuario');

    form.addEventListener('submit', function(e) {
        let valido = true;
        let primerError = null;

        // Campos
        const nombre = document.getElementById('nombre');
        const primerApellido = document.getElementById('primer-apellido');
        const segundoApellido = document.getElementById('segundo-apellido');
        const solapin = document.getElementById('solapin');
        const telefono = document.getElementById('telefono');
        const usuario = document.getElementById('user');
        const password = document.getElementById('password');
        const correo = document.getElementById('correo');
        const grupo = document.getElementById('grupo');
        const rol = document.getElementById('rol');

        // Limpiar errores previos
        [nombre, primerApellido, segundoApellido, solapin, telefono, usuario, password, correo, grupo, rol].forEach(clearError);

        // Validar campos vacíos y reglas
        if (!nombre.value.trim() || !validarNombre(nombre.value)) {
            setError(nombre, 'Debe comenzar con mayúscula y solo letras.');
            valido = false;
            primerError = primerError || nombre;
        }
        if (!primerApellido.value.trim() || !validarNombre(primerApellido.value)) {
            setError(primerApellido, 'Debe comenzar con mayúscula y solo letras.');
            valido = false;
            primerError = primerError || primerApellido;
        }
        if (!segundoApellido.value.trim() || !validarNombre(segundoApellido.value)) {
            setError(segundoApellido, 'Debe comenzar con mayúscula y solo letras.');
            valido = false;
            primerError = primerError || segundoApellido;
        }
        if (!solapin.value.trim() || !validarSolapin(solapin.value)) {
            setError(solapin, 'Debe comenzar con una letra mayúscula seguida de 6 números.');
            valido = false;
            primerError = primerError || solapin;
        }
        if (!telefono.value.trim() || !validarTelefono(telefono.value)) {
            setError(telefono, 'Debe tener entre 8 y 14 números, puede iniciar con +.');
            valido = false;
            primerError = primerError || telefono;
        }
        if (!usuario.value.trim() || !validarUsuario(usuario.value)) {
            setError(usuario, 'Solo minúsculas y números, sin espacios.');
            valido = false;
            primerError = primerError || usuario;
        }
        if (!password.value.trim() || !validarContrasena(password.value)) {
            setError(password, 'Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.');
            valido = false;
            primerError = primerError || password;
        }
        if (!correo.value.trim() || !validarCorreo(correo.value)) {
            setError(correo, 'El correo debe terminar en @uci.cu');
            valido = false;
            primerError = primerError || correo;
        }
        // Validación de grupo según rol
        if (rol.value === 'profesor_principal') {
            if (grupo.value) {
                setError(grupo, 'El grupo debe quedar vacío si el rol es Profesor Principal.');
                valido = false;
                primerError = primerError || grupo;
            }
        } else if (rol.value === 'usuario') {
            if (!grupo.value) {
                setError(grupo, 'Debe seleccionar un grupo si el rol es Estudiante.');
                valido = false;
                primerError = primerError || grupo;
            }
        } else {
            setError(rol, 'Debe seleccionar un rol.');
            valido = false;
            primerError = primerError || rol;
        }

        if (!valido) {
            e.preventDefault();
            if (primerError) primerError.focus();
            submitBtn.disabled = false;
        } else {
            submitBtn.disabled = true;
        }
    });
});

