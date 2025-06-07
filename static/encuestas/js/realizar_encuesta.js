document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-encuesta');
    const btnFinalizar = document.getElementById('btn-finalizar');
    if (!form || !btnFinalizar) return;
    form.addEventListener('submit', function(e) {
        btnFinalizar.disabled = true;
        // Obtener todos los grupos de preguntas
        const preguntas = Array.from(form.querySelectorAll('input[type="radio"]'))
            .map(input => input.name)
            .filter((v, i, a) => a.indexOf(v) === i); // nombres únicos

        let todasRespondidas = true;
        for (const name of preguntas) {
            if (!form.querySelector('input[name="' + name + '"]:checked')) {
                todasRespondidas = false;
                break;
            }
        }
        if (!todasRespondidas) {
            alert('Preguntas sin responder');
            btnFinalizar.disabled = false;
            e.preventDefault();
            return false;
        }
        // Si todas respondidas, el submit continúa
    });
});
