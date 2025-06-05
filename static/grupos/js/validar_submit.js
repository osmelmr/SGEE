document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const btnSubmit = document.getElementById('btn-submit');
    if (!form || !btnSubmit) return;

    form.addEventListener('submit', function(e) {
        btnSubmit.disabled = true;
        if (typeof validarFormulario === 'function' && !validarFormulario()) {
            e.preventDefault();
            btnSubmit.disabled = false;
        }
    });
});

