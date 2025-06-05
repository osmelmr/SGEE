document.addEventListener("DOMContentLoaded", function () {
  // Función genérica para manejar mensajes de error
  function manejarMensajeDeError(campo, regex, mensajeError, permitirVacio = false) {
    const errorMessage = document.createElement("span");
    errorMessage.style.color = "red";
    errorMessage.style.fontSize = "0.9em";
    errorMessage.style.display = "none"; // Oculto por defecto
    campo.parentNode.appendChild(errorMessage);

    campo.addEventListener("input", function () {
      if (this.value.trim() === "") {
        // Si el campo está vacío, oculta el mensaje de error
        errorMessage.style.display = "none";
      } else if (!regex.test(this.value)) {
        // Si el valor no cumple con la expresión regular, muestra el mensaje de error
        errorMessage.textContent = mensajeError;
        errorMessage.style.display = "block";
      } else {
        // Si el valor es válido, oculta el mensaje de error
        errorMessage.style.display = "none";
      }
    });

    campo.addEventListener("blur", function () {
      if (this.value.trim() === "" && !permitirVacio) {
        // Si el campo está vacío al salir y no se permite vacío, muestra el mensaje obligatorio
        errorMessage.textContent = "Este campo es obligatorio";
        errorMessage.style.display = "block";
      }
    });

    campo.addEventListener("focus", function () {
      // Oculta el mensaje de error al volver a enfocar el campo
      errorMessage.style.display = "none";
    });
  }

  // Validaciones específicas para los campos del formulario de encuesta
  manejarMensajeDeError(
    document.getElementById("titulo-encuesta"),
    /^.{10,50}$/,
    "Debe tener entre 10 y 50 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("descripcion-encuesta"),
    /^.{50,1000}$/,
    "Debe tener entre 50 y 1000 caracteres"
  );

  // Función para manejar el evento de submit
  const form = document.getElementById("form-crear-encuesta");
  form.addEventListener("submit", function (event) {
    let isValid = true;

    // Validar todos los campos
    const campos = [
      { id: "titulo-encuesta", regex: /^.{10,50}$/ },
      { id: "descripcion-encuesta", regex: /^.{50,1000}$/ }
    ];

    campos.forEach(({ id, regex }) => {
      const campo = document.getElementById(id);
      const errorMessage = campo.nextElementSibling;

      if (campo.value.trim() === "") {
        isValid = false;
        campo.focus(); // Enfocar el primer campo inválido
        errorMessage.textContent = "Este campo es obligatorio";
        errorMessage.style.display = "block";
      } else if (!regex.test(campo.value)) {
        isValid = false;
        campo.focus(); // Enfocar el primer campo inválido
        errorMessage.textContent = "Debe cumplir con el formato especificado";
        errorMessage.style.display = "block";
      }
    });

    // Si no es válido, prevenir el envío del formulario
    if (!isValid) {
      event.preventDefault();
      alert("Por favor, complete todos los campos correctamente.");
    }
  });
});