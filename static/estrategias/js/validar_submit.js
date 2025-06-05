// Función para validar el campo "curso"
function validarCurso(curso) {
    // Debe ser: 4 dígitos (2001-2099), un guion, 4 dígitos (2002-2100), y el segundo = primero+1
    const regex = /^(\d{4})-(\d{4})$/;
    const match = curso.match(regex);
    if (!match) return false;
    const anio1 = parseInt(match[1], 10);
    const anio2 = parseInt(match[2], 10);
    return (
        anio1 >= 2000 &&
        anio1 < 2100 &&
        anio2 === anio1 + 1 &&
        anio2 > 2000 &&
        anio2 <= 2100
    );
}

function validarNombre(nombre) {
    // Debe comenzar por mayúscula y tener al menos una letra
    return /^[A-ZÁÉÍÓÚÑ][a-záéíóúñA-ZÁÉÍÓÚÑ\s]*$/.test(nombre.trim());
}

function validarFormulario() {
    const cursoInput = document.getElementById('curso');
    const nombreInput = document.getElementById('nombre');
    const cursoVal = cursoInput.value.trim();
    const nombreVal = nombreInput.value.trim();

    let valido = true;

    // Validar curso
    if (!validarCurso(cursoVal)) {
        valido = false;
    }

    // Validar nombre
    if (!validarNombre(nombreVal)) {
        valido = false;
    }

    return valido;
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-estrategia');
    const btnRegistrar = document.querySelector('.btn-registrar');
    const cursoInput = document.getElementById('curso');
    const nombreInput = document.getElementById('titulo-estrategia');

    form.addEventListener('submit', function(e) {
        let errorMostrado = false;

        // Validación campo curso
        if (!cursoInput.value.trim() || !validarCurso(cursoInput.value.trim())) {
            e.preventDefault();
            cursoInput.classList.add('is-invalid');
            if (!document.getElementById('curso-error')) {
                const error = document.createElement('div');
                error.id = 'curso-error';
                error.className = 'invalid-feedback';
                error.innerText = 'El campo curso debe tener el formato AAAA-BBBB, donde BBBB = AAAA+1 y ambos entre 2000 y 2100.';
                cursoInput.parentNode.appendChild(error);
            }
            if (!errorMostrado) {
                cursoInput.focus();
                getStepIndexOfElement(cursoInput);
                errorMostrado = true;
            }
        } else {
            cursoInput.classList.remove('is-invalid');
            const err = document.getElementById('curso-error');
            if (err) err.remove();
        }

        // Validación campo nombre
        if (!nombreInput.value.trim() || !validarNombre(nombreInput.value.trim())) {
            e.preventDefault();
            nombreInput.classList.add('is-invalid');
            if (!document.getElementById('nombre-error')) {
                const error = document.createElement('div');
                error.id = 'nombre-error';
                error.className = 'invalid-feedback';
                error.innerText = 'El Titulo debe comenzar con mayúscula y solo permite espacio y letras.';
                nombreInput.parentNode.appendChild(error);
            }
            if (!errorMostrado) {
                nombreInput.focus();
                getStepIndexOfElement(nombreInput);
                errorMostrado = true;
            }
        } else {
            nombreInput.classList.remove('is-invalid');
            const err = document.getElementById('nombre-error');
            if (err) err.remove();
        }

        // Solo si curso y nombre son válidos, validar el resto de los campos vacíos
        if (errorMostrado) {
            const campos = form.querySelectorAll('input, select, textarea');
            for (const campo of campos) {
                if (
                    campo.type === 'button' ||
                    campo.type === 'submit' ||
                    campo.disabled 
                ) continue;
                if (!campo.value.trim()) {
                    e.preventDefault();
                    campo.classList.add('is-invalid');
                    if (!document.getElementById(campo.id + '-error')) {
                        const error = document.createElement('div');
                        error.id = campo.id + '-error';
                        error.className = 'invalid-feedback';
                        error.innerText = 'Este campo es obligatorio.';
                        campo.parentNode.appendChild(error);
                    }
                    if (!errorMostrado) {
                        getStepIndexOfElement(campo);
                        campo.focus();
                        errorMostrado = true;
                    }
                } else {
                    campo.classList.remove('is-invalid');
                    const err = document.getElementById(campo.id + '-error');
                    if (err) err.remove();
                }
            }
        }

        // Prevención de doble submit solo si es válido
        if (!errorMostrado && btnRegistrar) {
            btnRegistrar.disabled = true;
            btnRegistrar.innerHTML = '<i class="bi bi-hourglass-split"></i> Enviando...';
        }
    });
});