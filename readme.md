🛒 Flipkart DBMS Mini Project (Tkinter + Python)

A simple Flipkart-style user authentication system built using Python, Tkinter, and a database backend.
This project demonstrates how a frontend GUI interacts with a backend DBMS using clean architecture.

🚀 Features

🔐 User Registration

🔑 User Login

🖥️ Interactive Tkinter GUI

🗄️ Database Integration (via DBhelper)

🎨 Modern UI with styled components and hover effects

🧱 Project Structure
project/
│── db_helper.py        # Handles database operations
│── backend.py          # CLI-based backend (optional)
│── frontend.py         # Tkinter GUI (main app)
│── README.md
⚙️ Technologies Used

Python 3

Tkinter (for GUI)

SQLite / MySQL (depending on your DBhelper implementation)

🧠 Architecture

This project follows a separation of concerns approach:

Frontend (Tkinter) → Handles UI and user interaction

Backend (DBhelper) → Handles database operations

User → Tkinter GUI → DBhelper → Database
▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/flipkart-dbms-project.git
cd flipkart-dbms-project

Run the application:

python frontend.py
🧪 Functional Flow
🔹 Registration

User enters name, email, password

Data is sent to DBhelper.register()

Stored in database

🔹 Login

User enters credentials

Verified using DBhelper.login()

Access granted on success

🎨 UI Highlights

Card-based layout

Hover effects on buttons

Clean and centered design

Input validation with alerts

⚠️ Known Limitations

No password hashing (plaintext storage)

No product catalog yet

Basic authentication only

🔮 Future Improvements

🛍️ Add product listing (Flipkart-style dashboard)

🛒 Shopping cart system

🔐 Password hashing (bcrypt)

🌐 API-based backend

🌙 Dark mode

👨‍💻 Author

Darsh (IIIT Dharwad)

📌 Notes

This is a mini DBMS project ideal for:

College submissions

Viva demonstrations

Beginner GUI + DB integration learning
