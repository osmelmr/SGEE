document.addEventListener("DOMContentLoaded", function () {
  const solapinInput = document.getElementById("solapin");
  const errorMessage = document.createElement("span");
  errorMessage.style.color = "red";
  errorMessage.style.fontSize = "0.9em";
  errorMessage.style.display = "none"; // Oculto por defecto
  solapinInput.parentNode.appendChild(errorMessage);

  solapinInput.addEventListener("input", function () {
    console.log("Validando solapin:", this.value);
    const regex = /^[A-Z][0-9]{6}$/; // Una letra mayúscula seguida de exactamente 6 números

    if (!regex.test(this.value)) {
      errorMessage.textContent = "El formato debe ser: Una letra mayúscula seguida de 6 números (ejemplo: A123456)";
      errorMessage.style.display = "block"; // Muestra el mensaje de error
    } else {
      errorMessage.style.display = "none"; // Oculta el mensaje si es válido
    }
  });
});