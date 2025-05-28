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

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-estrategia');
    const cursoInput = document.getElementById('curso');

    form.addEventListener('submit', function(e) {
        const cursoVal = cursoInput.value.trim();
        if (!validarCurso(cursoVal)) {
            e.preventDefault();
            cursoInput.classList.add('is-invalid');
            if (!document.getElementById('curso-error')) {
                const error = document.createElement('div');
                error.id = 'curso-error';
                error.className = 'invalid-feedback';
                error.innerText = 'El campo curso debe tener el formato AAAA-BBBB, donde BBBB = AAAA+1 y ambos entre 2000 y 2100.';
                cursoInput.parentNode.appendChild(error);
            }
            cursoInput.focus();
        } else {
            cursoInput.classList.remove('is-invalid');
            const err = document.getElementById('curso-error');
            if (err) err.remove();
        }
    });
});