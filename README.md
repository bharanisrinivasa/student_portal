# 🎓 Student Portal

A robust, full-stack Django web application designed to manage student records efficiently. The project features a secure authentication system, role-based access control, REST API endpoints, and a custom modern dark user interface.

## ✨ Features

- **Student Management System**: Easily add, edit, delete, and view student records (including name, course, marks, and age).
- **Authentication & Authorization**: Built-in login, registration, and password management.
- **Role-Based Access Control**: Only staff members (`is_staff`) have the permission to add, modify, or delete student records.
- **Search & Pagination**: Browse through large datasets seamlessly with paginated lists and a search bar.
- **REST API Integration**: Built-in API endpoints (`/student_api/`) using Django REST Framework for JSON-based data operations.
- **Modern UI**: A beautifully crafted, responsive dark theme design utilizing frosted glass elements and vibrant blue accents.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **API**: Django REST Framework (DRF)
- **Frontend**: HTML5, Vanilla CSS (Custom styling)
- **Database**: SQLite (default)

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have Python and `pip` installed on your machine.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/bharanisrinivasa/student_portal.git
   cd student_portal
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Staff account)**
   *You will need a staff account to be able to add, edit, or delete students from the interface.*
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**
   Navigate to `http://127.0.0.1:8000/` to test the application!

## 📸 Screenshots

*(You can add screenshots of your sleek dark theme web application here)*

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License

Distributed under the MIT License.
