document.addEventListener('DOMContentLoaded', function() {
    const boton = document.getElementById('boton-descargar-estrategia');
    if (boton) {
        boton.addEventListener('click', function(event) {
            const nombre = this.getAttribute('data-nombre');
            if (!confirm(`¿Está seguro de que desea descargar la estrategia "${nombre}"?`)) {
                event.preventDefault();
            }
        });
    }
});