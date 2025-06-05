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

  // Validaciones específicas
  manejarMensajeDeError(
    document.getElementById("solapin"),
    /^[A-Z][0-9]{6}$/,
    "El formato debe ser: Una letra mayúscula seguida de 6 números (ejemplo: A123456)"
  );

  manejarMensajeDeError(
    document.getElementById("telefono"),
    /^[0-9]{8,15}$/,
    "Solo números (8-15 dígitos)"
  );

  manejarMensajeDeError(
    document.getElementById("correo"),
    /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
    "Debe ser un correo válido (ejemplo: usuario@dominio.com)"
  );

  manejarMensajeDeError(
    document.getElementById("descripcion-profesor"),
    /^.{10,500}$/,
    "Debe tener entre 10 y 500 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("nombre-profesor"),
    /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/,
    "Solo letras y espacios (2-50 caracteres)"
  );

  manejarMensajeDeError(
    document.getElementById("primer-apellido"),
    /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/,
    "Solo letras y espacios (2-50 caracteres)"
  );

  manejarMensajeDeError(
    document.getElementById("segundo-apellido"),
    /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{0,50}$/,
    "Solo letras y espacios (máx. 50 caracteres)",
    false // Cambiar a false para que sea obligatorio
  );

  manejarMensajeDeError(
    document.getElementById("asignatura"),
    /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]{5,50}$/,
    "Solo letras, números y espacios (5-50 caracteres)"
  );

  // Función para manejar el evento de submit
  const form = document.getElementById("formulario-profesor");
  form.addEventListener("submit", function (event) {
    let isValid = true;

    // Validar todos los campos
    const campos = [
      { id: "solapin", regex: /^[A-Z][0-9]{6}$/ },
      { id: "telefono", regex: /^[0-9]{8,15}$/ },
      { id: "correo", regex: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/ },
      { id: "descripcion-profesor", regex: /^.{10,500}$/ },
      { id: "nombre-profesor", regex: /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/ },
      { id: "primer-apellido", regex: /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/ },
      { id: "segundo-apellido", regex: /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{0,50}$/ },
      { id: "asignatura", regex: /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]{5,50}$/ }
    ];

    campos.forEach(({ id, regex }) => {
      const campo = document.getElementById(id);
      if (campo.value.trim() === "" || !regex.test(campo.value)) {
        isValid = false;
        campo.focus(); // Enfocar el primer campo inválido
      }
    });

    // Si no es válido, prevenir el envío del formulario
    if (!isValid) {
      event.preventDefault();
      alert("Por favor, complete todos los campos correctamente.");
    }
  });
});