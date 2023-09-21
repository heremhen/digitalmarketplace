document.addEventListener("DOMContentLoaded", function () {
    var messageElements = document.querySelectorAll(".message-timer");
    var delay = 2500;

    function hideMessages() {
        if (messageElements.length > 0) {
            var currentMessage = messageElements[0];
            currentMessage.style.display = "none";

            messageElements = Array.prototype.slice.call(messageElements, 1);

            if (messageElements.length > 0) {
                setTimeout(hideMessages, delay);
            }
        }
    }

    setTimeout(hideMessages, delay);
});