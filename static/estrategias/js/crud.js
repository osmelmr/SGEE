
// Selecciona todos los botones con la clase "btn-eliminar"
document.querySelectorAll(".btn-eliminar").forEach(button => {
    button.addEventListener("click", function () {
        const estrategiaId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        if (confirm("¿Estás seguro de que quieres eliminar esta estrategia ?"+estrategiaId)) {
            // Redirige a la URL para eliminar la estrategia
            window.location.href = `/p/eliminar/estrategia/${estrategiaId}/`;
        }
    });
});

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

// Selecciona todos los botones con la clase "btn-modificar"
document.querySelectorAll(".btn-modificar").forEach(button => {
    button.addEventListener("click", function (e) {
        //e.stopPropagation();
        const estrategiaId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        window.location.href = `/p/modificar/estrategia/${estrategiaId}/`;
    });
});

// Selecciona todos los botones con la clase "btn-ver-detalles"
document.querySelectorAll(".btn-ver-detalles").forEach(button => {
    button.addEventListener("click", function (e) {
        //e.stopPropagation();
        const estrategiaId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        window.location.href = `/p/visualizar/estrategia/${estrategiaId}/`;
    });
});

let formulario=document.getElementById("form-eliminar-estrategias");
formulario.addEventListener("submit", function(event){
  event.preventDefault();
  let estrategias=document.querySelectorAll(".seleccionar-fila:checked");
  if(estrategias.length===0){
    alert("No hay estrategias seleccionados");
    return;
  }
  if(confirm("¿Estás seguro de que quieres eliminar las estrategias seleccionadas?")){
    formulario.submit();
  }
});

document.getElementById('btn-seleccionar-todo').addEventListener('click', function (e) {
  e.preventDefault();
  const checkboxes = document.querySelectorAll('.seleccionar-fila');
  checkboxes.forEach(checkbox => checkbox.checked = !checkbox.checked);
});
