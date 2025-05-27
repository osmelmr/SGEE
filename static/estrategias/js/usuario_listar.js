// Selecciona todos los botones con la clase "btn-descargar-pdf"
document.querySelectorAll(".btn-descargar-pdf").forEach(button => {
    button.addEventListener("click", function () {
        const estrategiaId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        if (confirm("¿Estás seguro de que quieres descargar esta estrategia ?"+estrategiaId)) {
            // Redirige a la URL para eliminar la estrategia
            window.location.href = `/descargar/estrategia/pdf/${estrategiaId}/`;
        }
    });
});

// Selecciona todos los botones con la clase "btn-ver-detalles"
document.querySelectorAll(".btn-ver-detalles").forEach(button => {
    button.addEventListener("click", function (e) {
        //e.stopPropagation();
        const estrategiaId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        window.location.href = `/visualizar/estrategia/${estrategiaId}/`;
    });
});