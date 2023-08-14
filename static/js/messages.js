document.addEventListener("DOMContentLoaded", function () {
    var messageContainer = document.getElementById("message-container");

    if (messageContainer) {
        // Mostrar el mensaje
        messageContainer.style.display = "block";

        // Ocultar el mensaje después de 5 segundos (5000 ms)
        setTimeout(function () {
            messageContainer.style.display = "none";
        }, 5000);
    }
});
