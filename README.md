# Rail Mate 🚆

**Seamless Train Travel Starts Here. Your Ultimate Digital Ticketing Companion.**

 Rail-Mate is a modern, responsive Progressive Web App (PWA) built with Python and Django, designed to revolutionize the local train ticketing experience. Say goodbye to long queues and confusing interfaces. With Rail-Mate, you get a beautiful, fast, and straightforward way to book your train tickets from anywhere, at any time.

<!-- ![Barasat Rail-Mate Showcase](https://i.imgur.com/example.png) 
*(Image not available, replace with a screenshot of your app)* -->

---

## ✨ Features

- ⚡ **Blazing-Fast Station Search:** Instantly find your source and destination stations with an intelligent, autocomplete-powered search.
- 💵 **Real-Time Fare Calculation:** Get accurate, up-to-date ticket prices between any two stations in our network.
- 🎫 **Effortless Booking:** Book your journey in seconds and receive instant confirmation.
- 🌓 **Stunning Dark & Light Modes:** A beautifully crafted UI that automatically adapts to your system preference or can be toggled manually for comfortable viewing, day or night.
- 👤 **Personalized Profiles:** Create a profile to manage your details and enjoy a customized experience. Includes a secure logout option.
- 📱 **Progressive Web App (PWA):** Install Rail-Mate on your home screen for a fast, reliable, and engaging native-app-like experience.
- 🏠 **Intuitive & Modern UI:** A clean, user-friendly interface built with Bootstrap 5, designed for simplicity and ease of use.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Data & APIs:** jQuery & jQuery UI for dynamic content, Django ORM
- **Database:** SQLite3 (for development)
- **Environment:** Nix-based development environment

---

## 🚀 Getting Started

Get your local copy up and running in a few simple steps.

### Prerequisites

- Python 3.x
- `pip` package manager

### Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/arpan7sarkar/ticket-reservation
    cd ticket-reservation
    ```

2.  **Activate the Virtual Environment:**
    The project is configured to work within a Nix environment. To activate the Python virtual environment in your terminal:
    ```bash
    source .venv/bin/activate
    ```

3.  **Install Dependencies:**
    All required packages are listed in `requirements.txt`.
    ```bash
    pip install -r mysite/requirements.txt
    ```

4.  **Set Up the Database:**
    Run the initial migrations to prepare your database.
    ```bash
    python mysite/manage.py migrate
    ```

5.  **Populate Train Routes:**
    This custom command seeds the database with an extensive list of train routes and fares.
    ```bash
    python mysite/manage.py populate_routes
    ```

6.  **Run the Development Server:**
    Use the provided script to launch the Django development server.
    ```bash
    ./devserver.sh
    ```
    Or run it manually:
    ```bash
    python mysite/manage.py runserver
    ```
    Your application will be live at `http://127.0.0.1:8000/`.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
