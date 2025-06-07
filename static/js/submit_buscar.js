document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form.search-bar');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            const input = form.querySelector('input[type="text"]');
            if (input && !input.value.trim()) {
                e.preventDefault();
                alert('Debe introducir un criterio de búsqueda');
                input.focus();
            }
        });
    });
});