document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const btnSubmit = document.getElementById('btn-submit');
    const nombreInput = document.getElementById('nombre');
    const direccionInput = document.getElementById('direccion');
    const cursoSelect = document.getElementById('curso');
    const anioEscolarSelect = document.getElementById('anio_escolar');
    const caracterizacionInput = document.getElementById('caracterizacion');
    const guiaSelect = document.getElementById('guia');
    const profesoresChecks = document.querySelectorAll('input[name="profesores"]');

    // Funciones auxiliares reutilizadas del otro script
    function getError(input) {
        return input.classList.contains('is-invalid');
    }
    function getErrorProfesores() {
        const profesoresContainer = profesoresChecks.length ? profesoresChecks[0].closest('.mb-3') || profesoresChecks[0].parentNode.parentNode : null;
        if (!profesoresContainer) return false;
        let errorElem = profesoresContainer.querySelector('.error-validacion');
        return errorElem && errorElem.style.display === 'block';
    }
    function primerError() {
        if (getError(nombreInput)) return nombreInput;
        if (getError(direccionInput)) return direccionInput;
        if (getError(cursoSelect)) return cursoSelect;
        if (getError(anioEscolarSelect)) return anioEscolarSelect;
        if (getError(caracterizacionInput)) return caracterizacionInput;
        if (getError(guiaSelect)) return guiaSelect;
        if (getErrorProfesores()) {
            // Enfoca el primer checkbox
            for (let chk of profesoresChecks) {
                if (!chk.disabled) return chk;
            }
        }
        // Si hay campos vacíos sin error visual
        if (!nombreInput.value.trim()) return nombreInput;
        if (!direccionInput.value.trim()) return direccionInput;
        if (!cursoSelect.value.trim()) return cursoSelect;
        if (!anioEscolarSelect.value.trim()) return anioEscolarSelect;
        if (!caracterizacionInput.value.trim()) return caracterizacionInput;
        if (!guiaSelect.value.trim()) return guiaSelect;
        let algunoSeleccionado = false;
        profesoresChecks.forEach(chk => { if (chk.checked) algunoSeleccionado = true; });
        if (!algunoSeleccionado && profesoresChecks.length) return profesoresChecks[0];
        return null;
    }

    function esValido() {
        // Si hay algún campo con clase is-invalid o error de profesores, no es válido
        if (
            getError(nombreInput) ||
            getError(direccionInput) ||
            getError(cursoSelect) ||
            getError(anioEscolarSelect) ||
            getError(caracterizacionInput) ||
            getError(guiaSelect) ||
            getErrorProfesores()
        ) return false;
        // Si hay algún campo vacío
        if (
            !nombreInput.value.trim() ||
            !direccionInput.value.trim() ||
            !cursoSelect.value.trim() ||
            !anioEscolarSelect.value.trim() ||
            !caracterizacionInput.value.trim() ||
            !guiaSelect.value.trim()
        ) return false;
        // Profesores
        let algunoSeleccionado = false;
        profesoresChecks.forEach(chk => { if (chk.checked) algunoSeleccionado = true; });
        if (!algunoSeleccionado) return false;
        return true;
    }

    function actualizarBoton() {
        if (esValido()) {
            btnSubmit.disabled = false;
        } else {
            btnSubmit.disabled = true;
        }
    }

    // Escuchar cambios en todos los campos relevantes
    [
        nombreInput, direccionInput, cursoSelect, anioEscolarSelect,
        caracterizacionInput, guiaSelect
    ].forEach(input => {
        if (input) {
            input.addEventListener('input', actualizarBoton);
            input.addEventListener('change', actualizarBoton);
        }
    });
    profesoresChecks.forEach(chk => {
        chk.addEventListener('change', actualizarBoton);
    });

    // Validación en submit
    form.addEventListener('submit', function (e) {
        actualizarBoton();
        if (!esValido()) {
            e.preventDefault();
            const campo = primerError();
            if (campo && typeof campo.focus === 'function') campo.focus();
        }
    });

    // Validación inicial
    actualizarBoton();
});
