document.addEventListener('DOMContentLoaded', function() {
    const clearButton = document.getElementById('clear-button');
    const searchInput = document.querySelector('input[name="search"]');

    clearButton.addEventListener('click', function() {
        searchInput.value = '';
        antiExplosiveSelect.value = '';

        const form = clearButton.closest('form');
        form.submit();
    });
});