document.addEventListener('DOMContentLoaded', function() {
    const clearButton = document.getElementById('clear-button');

    clearButton.addEventListener('click', function() {
        const searchInput = document.querySelector('input[name="search"]');
        searchInput.value = '';

        const form = clearButton.closest('form');
        form.submit();
    });
});