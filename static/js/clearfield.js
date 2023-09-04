document.addEventListener('DOMContentLoaded', function() {
    const clearButton = document.getElementById('clear-button');
    const searchInput = document.querySelector('input[name="search"]');
    const antiExplosiveSelect = document.querySelector('select[name="anti_explosive_choice"]');

    clearButton.addEventListener('click', function() {
        searchInput.value = '';
        antiExplosiveSelect.value = '';

        const form = clearButton.closest('form');
        form.submit();
    });
});