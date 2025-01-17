document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const numero = document.getElementById('numero').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            numero_telefono: numero,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        if (data.message === "Accesso riuscito") {
            messageDiv.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
            window.location.href = data.redirect;  // Reindirizza alla pagina della lista
        } else {
            messageDiv.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
        }
    })
    .catch(error => {
        console.error('Errore:', error);
        document.getElementById('message').innerHTML = `<div class="alert alert-danger">Errore di comunicazione.</div>`;
    });
});
