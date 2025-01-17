# DB_ShoppingList-Website

A collaborative shopping list management website, developed using **Python**, **JavaScript**, and **HTML**. The site can be very easily adapted to different needs, offering a flexible foundation for similar applications.

## Main Features

1. **User Login**:
   - Users can log in using their phone number and a password.
   - Example credentials for testing the application:
     - **Phone Number**: `12345678`
     - **Password**: `password`

2. **Item Management**:
   - Users can **add** and **remove** items from the shopping list.

3. **User Interaction**:
   - Each user can **approve** or **reject** items on the list, making the process collaborative.

4. **Multi-user Support**:
   - The site supports multiple users simultaneously, with each user contributing to the shared list.

## Requirements

- **Python 3.x**
- **SQLite**
- **JavaScript enabled in the browser**
- Required libraries and modules (see [Installation](#installation))

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/DB_ShoppingList-Website.git
   cd DB_ShoppingList-Website
   ```

2. **Install dependencies**:
   Ensure Python is installed, then use `pip` to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database**:
   The database will be created automatically when you run the app for the first time, thanks to the `create_database()` function.

4. **Run the server**:
   Start the website by running the `app.py` file:
   ```bash
   python app.py
   ```

5. **Access the website**:
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

- `app.py`: Main file managing the backend and APIs.
- `shopping.db`: SQLite database for managing items.
- `templates/`: Contains HTML files (e.g., `index.html`, `layout.html`, `shopping_list.html`).
- `static/js/`: Contains JavaScript files (e.g., `login.js`, `shopping_list.js`).

## Using the Website

1. **Login**:
   - Enter the example credentials or register as a new user (if implemented).
2. **List Management**:
   - Add new items by entering the item name.
   - Remove items from the list, if necessary.
3. **Approve or Reject**:
   - Review items added by other users and decide whether to approve or reject them.

## Contributing

1. Fork the repository.
2. Create a new branch for your changes:
   ```bash
   git checkout -b branch-name
   ```
3. Make your updates and commit:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes:
   ```bash
   git push origin branch-name
   ```
5. Open a pull request.

## License

This repository is distributed under the MIT license. See the [LICENSE](LICENSE) file for more details.

---

Developed with ❤️ to simplify shopping list management! 🛒
