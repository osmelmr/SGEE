
// Selecciona todos los botones con la clase "btn-eliminar"
document.querySelectorAll(".btn-eliminar").forEach(button => {
    button.addEventListener("click", function () {
        const grupoId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        if (confirm("¿Estás seguro de que quieres eliminar esta grupo ?"+grupoId)) {
            // Redirige a la URL para eliminar la grupo
            window.location.href = `/p/eliminar/grupo/${grupoId}/`;
        }
    });
});


// Selecciona todos los botones con la clase "btn-modificar"
document.querySelectorAll(".btn-modificar").forEach(button => {
    button.addEventListener("click", function (e) {
        //e.stopPropagation();
        const grupoId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        window.location.href = `/p/modificar/grupo/${grupoId}/`;
    });
});

// Selecciona todos los botones con la clase "btn-ver-detalles"
document.querySelectorAll(".btn-ver-detalles").forEach(button => {
    button.addEventListener("click", function (e) {
        //e.stopPropagation();
        const grupoId = this.getAttribute("data-id"); // Obtiene el ID desde el atributo data-id
        window.location.href = `/p/visualizar/grupo/${grupoId}/`;
    });
});

let formulario=document.getElementById("form-eliminar-grupos");
formulario.addEventListener("submit", function(event){
  event.preventDefault();
  let grupos=document.querySelectorAll(".seleccionar-fila:checked");
  if(grupos.length===0){
    alert("No hay grupos seleccionados");
    return;
  }
  if(confirm("¿Estás seguro de que quieres eliminar las grupos seleccionadas?")){
    formulario.submit();
  }
});

document.getElementById('btn-seleccionar-todo').addEventListener('click', function (e) {
  e.preventDefault();
  const checkboxes = document.querySelectorAll('.seleccionar-fila');
  checkboxes.forEach(checkbox => checkbox.checked = !checkbox.checked);
});
