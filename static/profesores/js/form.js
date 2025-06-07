window.addEventListener('DOMContentLoaded', function() {
    const select = document.getElementById('grupos');
    const container = document.getElementById('grupos-checkboxes');

    // Crear un checkbox por cada opción del select
    Array.from(select.options).forEach(option => {
        const label = document.createElement('label');
        label.style.display = 'block';
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.value = option.value;
        checkbox.name = select.name; // para que se envíen como lista
        checkbox.checked = option.selected;
        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(' ' + option.text));
        container.appendChild(label);

        // Sincronizar checkbox con select
        checkbox.addEventListener('change', function() {
            option.selected = checkbox.checked;
        });
    });
});