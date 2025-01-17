$(document).ready(function() {
    // Funzione per caricare gli articoli
    function loadItems() {
        $.get('/get_items', function(data) {
            console.log("Dati ricevuti dal server:", data);  // Debug: stampa i dati ricevuti
            const list = $('#shoppingList');
            list.empty();  // Svuota la lista
            data.items.forEach(item => {
                const approvedBy = item.approved_by || 'Nessuno';
                const rejectedBy = item.rejected_by || 'Nessuno';

                list.append(`
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div>
                            <strong>${item.name}</strong><br>
                            <small>Approvato da: ${approvedBy}</small><br>
                            <small>Rifiutato da: ${rejectedBy}</small>
                        </div>
                        <div>
                            <button class="btn btn-success btn-sm me-2 approve-btn" data-id="${item.id}">Approva</button>
                            <button class="btn btn-danger btn-sm reject-btn" data-id="${item.id}">Rifiuta</button>
                        </div>
                    </li>
                `);
            });
        }).fail(function(err) {
            console.error("Errore nel caricamento degli articoli:", err);
            alert("Errore nel caricamento della lista.");
        });
    }

    // Aggiungere un nuovo articolo
    $('#addItemForm').submit(function(e) {
        e.preventDefault();
        const itemName = $('#itemName').val().trim();
        console.log("Articolo inviato:", itemName);

        if (itemName) {
            $.post('/add_item', { name: itemName }, function(response) {
                console.log("Risposta dal server:", response);
                if (response.success) {
                    $('#itemName').val('');  // Pulisce il campo input
                    loadItems();  // Ricarica la lista aggiornata
                } else {
                    alert("Errore nell'aggiunta dell'articolo.");
                }
            }).fail(function(err) {
                console.error("Errore nella richiesta POST:", err);
                alert("Errore nella comunicazione con il server.");
            });
        }
    });

    // Approva un articolo
    $('#shoppingList').on('click', '.approve-btn', function() {
        const itemId = $(this).data('id');
        console.log("Approva articolo con ID:", itemId);

        $.post('/approve_item', { id: itemId }, function(response) {
            console.log("Risposta approvazione:", response);
            if (response.success) loadItems();
            else alert("Errore nell'approvazione.");
        }).fail(function(err) {
            console.error("Errore nella richiesta di approvazione:", err);
        });
    });

    // Rifiuta un articolo
    $('#shoppingList').on('click', '.reject-btn', function() {
        const itemId = $(this).data('id');
        console.log("Rifiuta articolo con ID:", itemId);

        $.post('/reject_item', { id: itemId }, function(response) {
            console.log("Risposta rifiuto:", response);
            if (response.success) loadItems();
            else alert("Errore nel rifiuto.");
        }).fail(function(err) {
            console.error("Errore nella richiesta di rifiuto:", err);
        });
    });

    // Carica gli articoli al caricamento della pagina
    loadItems();
});
