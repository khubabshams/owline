setTimeout(function () {
    let messages = document.getElementsByClassName("message");
    let alert = false;
    for (let message of messages) {
        alert = new bootstrap.Alert(message);
        alert.close();
    }

}, 3000);