# DB_ShoppingList-Website

Un sito web per la gestione collaborativa di una lista della spesa, sviluppato utilizzando **Python**, **JavaScript**, e **HTML**. 
Il sito può essere molto facilmente adattato a necessità diverse, offrendo una base flessibile per applicazioni simili.

## Funzionalità principali

1. **Login Utente**:
   - Gli utenti possono accedere utilizzando il loro numero di telefono e una password.
   - Credenziali di esempio per testare l'applicazione:
     - **Numero di telefono**: `12345678`
     - **Password**: `password`

2. **Gestione Articoli**:
   - Gli utenti possono **aggiungere** e **rimuovere** articoli dalla lista della spesa.

3. **Interazione tra Utenti**:
   - Ogni utente può **approvare** o **rifiutare** gli articoli nella lista, rendendo il processo collaborativo.

4. **Multi-utente**:
   - Il sito supporta più utenti contemporaneamente, con ogni utente che può contribuire alla lista comune.

## Requisiti

- **Python 3.x**
- **SQLite**
- **JavaScript abilitato nel browser**
- Librerie e moduli necessari (vedi la sezione [Installazione](#installazione))

## Installazione

1. **Clona la repository**:
   ```bash
   git clone https://github.com/paoloronco/DB_ShoppingList-Website.git
   cd DB_ShoppingList-Website
   ```

2. **Installa le dipendenze**:
   Assicurati di avere Python installato e utilizza `pip` per installare i pacchetti richiesti:
   ```bash
   pip install -r requirements.txt
   ```

3. **Crea il database**:
   Il database verrà creato automaticamente quando esegui l'app per la prima volta grazie alla funzione `create_database()`.

4. **Esegui il server**:
   Avvia il sito web eseguendo il file `app.py`:
   ```bash
   python app.py
   ```

5. **Accedi al sito**:
   Apri il browser e vai all'indirizzo:
   ```
   http://localhost:5000
   ```

## Struttura del Progetto

- `app.py`: File principale che gestisce il backend e le API.
- `shopping.db`: Database SQLite per la gestione degli articoli.
- `templates/`: Contiene i file HTML (es. `index.html`, `layout.html`, `shopping_list.html`).
- `static/js/`: Contiene i file JavaScript (es. `login.js`, `shopping_list.js`).

## Uso del Sito

1. **Login**:
   - Inserisci le credenziali di esempio o registrati come nuovo utente (se implementato).
2. **Gestione Lista**:
   - Aggiungi nuovi articoli inserendo il nome dell'articolo.
   - Rimuovi articoli dalla lista, se necessario.
3. **Approva o Rifiuta**:
   - Esamina gli articoli aggiunti dagli altri utenti e decidi se approvarli o rifiutarli.



## Contribuire

1. Fai un fork della repository.
2. Crea un nuovo branch per le modifiche:
   ```bash
   git checkout -b nome-branch
   ```
3. Esegui i tuoi aggiornamenti e fai commit:
   ```bash
   git commit -m "Descrizione delle modifiche"
   ```
4. Spingi le modifiche:
   ```bash
   git push origin nome-branch
   ```
5. Apri una pull request.

## Licenza

Questa repository è distribuita sotto la licenza MIT. Vedi il file [LICENSE](https://it.wikipedia.org/wiki/Licenza_MIT) per ulteriori dettagli.

---

Sviluppato con ❤️ per semplificare la gestione delle liste della spesa! 🛒
