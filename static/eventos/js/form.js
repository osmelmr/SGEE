document.addEventListener('DOMContentLoaded', function() {
  const selectProfesor = document.getElementById('profesor-cargo');
  const inputTelefono = document.getElementById('telefono-contacto');
  if (selectProfesor && inputTelefono) {
    selectProfesor.addEventListener('change', function() {
      const selected = selectProfesor.options[selectProfesor.selectedIndex];
      const telefono = selected.getAttribute('data-telefono') || '';
      inputTelefono.value = telefono;
      inputTelefono.dispatchEvent(new Event('input')); // <-- dispara validación
    });

    // Autocompletar teléfono al cargar si ya hay un profesor seleccionado
    const selected = selectProfesor.options[selectProfesor.selectedIndex];
    if (selected && selected.getAttribute('data-telefono')) {
      inputTelefono.value = selected.getAttribute('data-telefono');
      inputTelefono.dispatchEvent(new Event('input')); // <-- dispara validación
    }
  }
});