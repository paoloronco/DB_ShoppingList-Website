from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Chiave segreta per le sessioni

# Finto database utenti
users = [
    {"id": 1, "nome": "user1", "numero_telefono": "12345678", "password": "password"},
]

#Funzione per connettersi al database SQLite
def get_db_connection():
    conn = sqlite3.connect('shopping.db')
    conn.row_factory = sqlite3.Row  # Per accedere ai dati come dizionari
    return conn

# Route per la pagina principale (login)
@app.route('/')
def home():
    return render_template('index.html')

# Route per gestire il login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    numero = data.get("numero_telefono")
    password = data.get("password")

    for user in users:
        if user["numero_telefono"] == numero and user["password"] == password:
            session['user_id'] = user["id"]
            session['nome'] = user["nome"]
            print(f"Login riuscito per {user['nome']}")
            return jsonify({"message": "Accesso riuscito", "redirect": url_for('shopping_list_page')}), 200
    print("Tentativo di login fallito.")
    return jsonify({"message": "Credenziali non valide"}), 401

# Route per la pagina della lista della spesa
@app.route('/shopping_list')
def shopping_list_page():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    return render_template('shopping_list.html', nome=session['nome'])

# API per ottenere tutti gli articoli
@app.route('/get_items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM shopping_list').fetchall()
    conn.close()
    return jsonify({'items': [dict(item) for item in items]})

@app.route('/add_item', methods=['POST'])
def add_item():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Non autorizzato'}), 403

    item_name = request.form.get('name').strip().lower()  # Normalizza: rimuove spazi e mette in minuscolo
    print("Nome articolo ricevuto:", item_name)

    if not item_name:
        return jsonify({'success': False, 'message': 'Nome articolo non valido'})

    conn = get_db_connection()
    
    # Controlla se l'articolo esiste già (case-insensitive)
    existing_item = conn.execute(
        'SELECT * FROM shopping_list WHERE LOWER(name) = ?',
        (item_name,)
    ).fetchone()

    if existing_item:
        conn.close()
        print("Articolo già esistente:", item_name)
        return jsonify({'success': False, 'message': 'Articolo già esistente nella lista'})

    # Aggiunge il nuovo articolo
    conn.execute(
        'INSERT INTO shopping_list (name, approved_by, rejected_by) VALUES (?, ?, ?)',
        (item_name, '', '')
    )
    conn.commit()
    conn.close()
    print("Articolo aggiunto con successo!")
    return jsonify({'success': True, 'message': 'Articolo aggiunto con successo'})



#API per approvare un articolo
@app.route('/approve_item', methods=['POST'])
def approve_item():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Non autorizzato'}), 403

    item_id = request.form.get('id')
    user_name = session['nome']
    print(f"Approvazione richiesta per ID {item_id} da {user_name}")

    conn = get_db_connection()
    conn.execute('UPDATE shopping_list SET approved_by = ? WHERE id = ?', (user_name, item_id))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

# API per rifiutare un articolo
@app.route('/reject_item', methods=['POST'])
def reject_item():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Non autorizzato'}), 403

    item_id = request.form.get('id')
    user_name = session['nome']
    print(f"Rifiuto richiesto per ID {item_id} da {user_name}")

    conn = get_db_connection()
    conn.execute('UPDATE shopping_list SET rejected_by = ? WHERE id = ?', (user_name, item_id))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

# Route per il logout
@app.route('/logout')
def logout():
    session.clear()
    print("Logout effettuato")
    return redirect(url_for('home'))

# Creazione del database e della tabella (eseguito una volta)
def create_database():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS shopping_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            approved_by TEXT,
            rejected_by TEXT
        );
    ''')
    conn.commit()
    conn.close()
    print("Database e tabella creati con successo.")

if __name__ == '__main__':
    create_database()  # Crea il database se non esiste
    app.run(host='0.0.0.0', port=5000, debug=True)
