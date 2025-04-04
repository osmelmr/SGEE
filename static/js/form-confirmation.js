/**
 * Maneja la confirmación de envío de formularios
 * @param {HTMLFormElement} form - El formulario a validar
 * @param {string} message - El mensaje de confirmación a mostrar
 * @returns {boolean} - True si el usuario confirma, False si cancela
 */
function confirmSubmit(form, message = '¿Está seguro que desea enviar este formulario?') {
    form.addEventListener('submit', function(event) {
        // Prevenir el envío del formulario
        event.preventDefault();
        
        // Mostrar el diálogo de confirmación
        if (confirm(message)) {
            // Si el usuario confirma, enviar el formulario
            form.submit();
        }
    });
}

/**
 * Inicializa la confirmación en todos los formularios con la clase 'needs-confirmation'
 */
document.addEventListener('DOMContentLoaded', function() {
    // Buscar todos los formularios que necesitan confirmación
    const forms = document.querySelectorAll('form.needs-confirmation');
    
    forms.forEach(function(form) {
        // Obtener el mensaje personalizado del atributo data-confirm-message si existe
        const message = form.dataset.confirmMessage || '¿Está seguro que desea enviar este formulario?';
        confirmSubmit(form, message);
    });
}); 