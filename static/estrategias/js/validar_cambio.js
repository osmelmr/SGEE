// Puedes importar o copiar las funciones validarCurso y validarNombre aquí si no están en global

document.addEventListener('DOMContentLoaded', function() {
    const cursoInput = document.getElementById('curso');
    const nombreInput = document.getElementById('titulo-estrategia');

    if (cursoInput) {
        cursoInput.addEventListener('input', function() {
            if (!cursoInput.value.trim() || !validarCurso(cursoInput.value.trim())) {
                cursoInput.classList.add('is-invalid');
                if (!document.getElementById('curso-error')) {
                    const error = document.createElement('div');
                    error.id = 'curso-error';
                    error.className = 'invalid-feedback';
                    error.innerText = 'El curso solo puede contener dos años consecutivos separados por - (EJ: 2014-2015)';
                    cursoInput.parentNode.appendChild(error);
                }
            } else {
                cursoInput.classList.remove('is-invalid');
                const err = document.getElementById('curso-error');
                if (err) err.remove();
            }
        });
    }

    if (nombreInput) {
        nombreInput.addEventListener('input', function() {
            if (!nombreInput.value.trim() || !validarNombre(nombreInput.value.trim())) {
                nombreInput.classList.add('is-invalid');
                if (!document.getElementById('nombre-error')) {
                    const error = document.createElement('div');
                    error.id = 'nombre-error';
                    error.className = 'invalid-feedback';
                    error.innerText = 'El Titulo debe comenzar con mayúscula y solo permite espacio y letras.';
                    nombreInput.parentNode.appendChild(error);
                }
            } else {
                nombreInput.classList.remove('is-invalid');
                const err = document.getElementById('nombre-error');
                if (err) err.remove();
            }
        });
    }
});