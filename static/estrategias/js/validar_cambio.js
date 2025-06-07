// Puedes importar o copiar las funciones validarCurso y validarNombre aquí si no están en global

document.addEventListener('DOMContentLoaded', function() {
    const cursoInput = document.getElementById('curso');
    const nombreInput = document.getElementById('titulo-estrategia');

    if (cursoInput) {
        cursoInput.addEventListener('input', function() {
            if (!cursoInput.value.trim()) {
                cursoInput.classList.add('is-invalid');
                let err = document.getElementById('curso-error');
                if (!err) {
                    err = document.createElement('div');
                    err.id = 'curso-error';
                    err.className = 'invalid-feedback';
                    cursoInput.parentNode.appendChild(err);
                }
                err.innerText = 'Este campo es obligatorio.';
            } else if (!validarCurso(cursoInput.value.trim())) {
                cursoInput.classList.add('is-invalid');
                let err = document.getElementById('curso-error');
                if (!err) {
                    err = document.createElement('div');
                    err.id = 'curso-error';
                    err.className = 'invalid-feedback';
                    cursoInput.parentNode.appendChild(err);
                }
                err.innerText = 'El curso solo puede contener dos años consecutivos separados por - (EJ: 2014-2015)';
            } else {
                cursoInput.classList.remove('is-invalid');
                const err = document.getElementById('curso-error');
                if (err) err.remove();
            }
        });
    }

    if (nombreInput) {
        nombreInput.addEventListener('input', function() {
            if (!nombreInput.value.trim()) {
                nombreInput.classList.add('is-invalid');
                let err = document.getElementById('nombre-error');
                if (!err) {
                    err = document.createElement('div');
                    err.id = 'nombre-error';
                    err.className = 'invalid-feedback';
                    nombreInput.parentNode.appendChild(err);
                }
                err.innerText = 'Este campo es obligatorio.';
            } else if (!validarNombre(nombreInput.value.trim())) {
                nombreInput.classList.add('is-invalid');
                let err = document.getElementById('nombre-error');
                if (!err) {
                    err = document.createElement('div');
                    err.id = 'nombre-error';
                    err.className = 'invalid-feedback';
                    nombreInput.parentNode.appendChild(err);
                }
                err.innerText = 'El Titulo debe comenzar con mayúscula y solo permite espacio y letras.';
            } else {
                nombreInput.classList.remove('is-invalid');
                const err = document.getElementById('nombre-error');
                if (err) err.remove();
            }
        });
    }

    // Lista de IDs de los campos requeridos (excepto curso y nombre que ya tienen lógica especial)
    const camposObligatorios = [
        'ano-escolar',
        'grupo',
        'plan_estudios',
        'obj_estrategia',
        'direccion-grupo',
        'caracteristicas-grupo',
        'colectivo-pedagogico',
        'otros-aspectos',
        'dimension-curricular',
        'dimension-extensionista',
        'dimension-politico-ideologica',
        'conclusiones',
        'objetivo-general',
        'objetivos-especificos-curricular',
        'plan-acciones-curricular',
        'objetivos-especificos-extensionista',
        'plan-acciones-extensionista',
        'objetivos-especificos-politico-ideologica',
        'plan-acciones-politico-ideologica',
        'evaluacion-integral',
        'autor'
    ];

    camposObligatorios.forEach(function(id) {
        const campo = document.getElementById(id);
        if (campo) {
            campo.addEventListener('input', function() {
                let errId = id + '-error';
                let err = document.getElementById(errId);
                if (!campo.value.trim()) {
                    campo.classList.add('is-invalid');
                    if (!err) {
                        err = document.createElement('div');
                        err.id = errId;
                        err.className = 'invalid-feedback';
                        campo.parentNode.appendChild(err);
                    }
                    err.innerText = 'Este campo es obligatorio.';
                } else {
                    campo.classList.remove('is-invalid');
                    if (err) err.remove();
                }
            });
        }
    });
});