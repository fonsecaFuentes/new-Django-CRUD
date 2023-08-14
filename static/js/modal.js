document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const motorRedirectModal = params.get('motorModal');
    const couplingRedirectModal = params.get('couplingModal');

    const showModal = motorRedirectModal === 'true' || couplingRedirectModal === 'true';

    if (showModal) {
        const imagenModal = new bootstrap.Modal(document.getElementById('editarModal'));
        imagenModal.show();
    }
});