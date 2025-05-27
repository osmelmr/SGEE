/**
 * Inicializa la funcionalidad dinámica para agregar y eliminar preguntas en un formulario de encuesta.
 * @param {string} btnAgregarSelector - Selector del botón para agregar preguntas.
 * @param {string} contenedorSelector - Selector del contenedor donde se agregan las preguntas.
 */
function initPreguntasEncuesta(btnAgregarSelector, contenedorSelector) {
  const agregarPreguntaBtn = document.querySelector(btnAgregarSelector);
  const preguntasContainer = document.querySelector(contenedorSelector);

  if (!agregarPreguntaBtn || !preguntasContainer) return;

  let contadorPreguntas = preguntasContainer.querySelectorAll('.pregunta').length || 1;

  agregarPreguntaBtn.addEventListener('click', function() {
    contadorPreguntas++;
    const nuevaPregunta = document.createElement('div');
    nuevaPregunta.classList.add('pregunta', 'mb-3', 'p-3', 'border', 'rounded');
    nuevaPregunta.innerHTML = `
      <div class="form-group">
        <label for="pregunta${contadorPreguntas}">Pregunta ${contadorPreguntas}</label>
        <input type="text" id="pregunta${contadorPreguntas}" name="preguntas[]" class="form-control" required>
      </div>
      <div class="text-right">
        <button type="button" class="btn btn-danger btn-sm btn-eliminar">
          <i class="bi bi-trash"></i> Eliminar
        </button>
      </div>
    `;
    preguntasContainer.appendChild(nuevaPregunta);

    nuevaPregunta.querySelector('.btn-eliminar').addEventListener('click', function() {
      eliminarPregunta(this);
    });
  });

  preguntasContainer.querySelectorAll('.btn-eliminar').forEach(btn => {
    btn.addEventListener('click', function() {
      eliminarPregunta(this);
    });
  });

  function eliminarPregunta(boton) {
    const pregunta = boton.closest('.pregunta');
    if (confirm('¿Estás seguro de que deseas eliminar esta pregunta?')) {
      pregunta.remove();
      reorganizarPreguntas();
    }
  }

  function reorganizarPreguntas() {
    const preguntas = preguntasContainer.querySelectorAll('.pregunta');
    preguntas.forEach((pregunta, index) => {
      const numeroPregunta = index + 1;
      pregunta.querySelector('label').textContent = `Pregunta ${numeroPregunta}`;
      const input = pregunta.querySelector('input');
      input.id = `pregunta${numeroPregunta}`;
      input.name = `preguntas[]`;
    });
    contadorPreguntas = preguntas.length;
  }
}

// Auto-inicialización al cargar el DOM
document.addEventListener('DOMContentLoaded', function() {
  initPreguntasEncuesta('#agregar-pregunta', '#preguntas-encuesta');
});