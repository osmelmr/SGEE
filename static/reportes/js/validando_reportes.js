document.addEventListener("DOMContentLoaded", function () {
  // Función genérica para manejar mensajes de error
  function manejarMensajeDeError(campo, regex, mensajeError, permitirVacio = false) {
    let errorMessage = campo.parentNode.querySelector(".error-message");
    if (!errorMessage) {
      errorMessage = document.createElement("span");
      errorMessage.className = "error-message";
      errorMessage.style.color = "red";
      errorMessage.style.fontSize = "0.9em";
      errorMessage.style.display = "none"; // Oculto por defecto
      campo.parentNode.appendChild(errorMessage);
    }

    campo.addEventListener("input", function () {
      if (this.value.trim() === "") {
        if (!permitirVacio) {
          errorMessage.textContent = "Este campo es obligatorio";
          errorMessage.style.display = "block";
          campo.classList.add("is-invalid");
        } else {
          errorMessage.style.display = "none";
          campo.classList.remove("is-invalid");
        }
      } else if (!regex.test(this.value)) {
        errorMessage.textContent = mensajeError;
        errorMessage.style.display = "block";
        campo.classList.add("is-invalid");
      } else {
        errorMessage.style.display = "none";
        campo.classList.remove("is-invalid");
      }
    });

    campo.addEventListener("blur", function () {
      if (this.value.trim() === "" && !permitirVacio) {
        errorMessage.textContent = "Este campo es obligatorio";
        errorMessage.style.display = "block";
        campo.classList.add("is-invalid");
      }
    });

    campo.addEventListener("focus", function () {
      errorMessage.style.display = "none";
      campo.classList.remove("is-invalid");
    });
  }

  // Validaciones específicas para los campos del formulario de reporte
  manejarMensajeDeError(
    document.getElementById("codigo"),
    /^.+$/, // Acepta cualquier valor no vacío
    "Este campo es obligatorio"
  );

  manejarMensajeDeError(
    document.getElementById("fecha"),
    /^\d{4}-\d{2}-\d{2}$/, // Formato de fecha YYYY-MM-DD
    "Debe ingresar una fecha válida (YYYY-MM-DD)"
  );

  manejarMensajeDeError(
    document.getElementById("periodo"),
    /^.+$/, // Acepta cualquier valor no vacío
    "Este campo es obligatorio"
  );

  manejarMensajeDeError(
    document.getElementById("select_grupo"),
    /^.+$/, // Acepta cualquier valor no vacío
    "Este campo es obligatorio"
  );

  manejarMensajeDeError(
    document.getElementById("resumen"),
    /^.{10,1000}$/,
    "Debe tener entre 10 y 1000 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("objetivos"),
    /^.{10,1000}$/,
    "Debe tener entre 10 y 1000 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("actividades"),
    /^.{10,1000}$/,
    "Debe tener entre 10 y 1000 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("institucion"),
    /^.{3,50}$/,
    "Debe tener entre 3 y 50 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("resultados"),
    /^.{10,1000}$/,
    "Debe tener entre 10 y 1000 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("analisis"),
    /^.{10,1000}$/,
    "Debe tener entre 10 y 1000 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("desafios"),
    /^.{10,1000}$/,
    "Debe tener entre 10 y 1000 caracteres"
  );

  manejarMensajeDeError(
    document.getElementById("proximos-pasos"),
    /^.{10,1000}$/,
    "Debe tener entre 10 y 1000 caracteres"
  );

  // Función para manejar el evento de submit
  const form = document.getElementById("form-reporte");
  form.addEventListener("submit", function (event) {
    let isValid = true;

    // Validar todos los campos
    const campos = [
      { id: "codigo", regex: /^.+$/ },
      { id: "fecha", regex: /^\d{4}-\d{2}-\d{2}$/ },
      { id: "periodo", regex: /^.+$/ },
      { id: "select_grupo", regex: /^.+$/ },
      { id: "resumen", regex: /^.{10,1000}$/ },
      { id: "objetivos", regex: /^.{10,1000}$/ },
      { id: "actividades", regex: /^.{10,1000}$/ },
      { id: "institucion", regex: /^.{3,50}$/ },
      { id: "resultados", regex: /^.{10,1000}$/ },
      { id: "analisis", regex: /^.{10,1000}$/ },
      { id: "desafios", regex: /^.{10,1000}$/ },
      { id: "proximos-pasos", regex: /^.{10,1000}$/ }
    ];

    campos.forEach(({ id, regex }) => {
      const campo = document.getElementById(id);
      const errorMessage = campo.parentNode.querySelector(".error-message");

      if (campo.value.trim() === "") {
        isValid = false;
        errorMessage.textContent = "Este campo es obligatorio";
        errorMessage.style.display = "block";
        campo.classList.add("is-invalid");
      } else if (!regex.test(campo.value)) {
        isValid = false;
        errorMessage.textContent = "Debe cumplir con el formato especificado";
        errorMessage.style.display = "block";
        campo.classList.add("is-invalid");
      } else {
        errorMessage.style.display = "none";
        campo.classList.remove("is-invalid");
      }
    });

    // Si no es válido, prevenir el envío del formulario
    if (!isValid) {
      event.preventDefault();
      alert("Por favor, complete todos los campos correctamente.");
    }
  });
});