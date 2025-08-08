## 🍽 Food Menu

This is a Django-based web application that allows users to list, view, update, and delete food items. The project also includes user authentication, where users can register, log in, and view their profiles.

### ✨ Features

  - View a list of food items.
  - User authentication: Register, Log in, and Log out.
  - Authenticated users can add new food items.
  - Update and delete existing food items.
  - A profile page for each user.
  - Bootstrap-based responsive design.

-----

### 🛠 Installation & Setup

Follow these steps to run the project:

1.  **Install Dependencies**
    `pip install django`
2.  **Run Database Migrations**
    `python manage.py makemigrations food users`
    `python manage.py migrate`
3.  **Start the Development Server**
    `python manage.py runserver`

Now open your browser and go to:
`http://127.0.0.1:8000/`

-----

### 📂 File Structure

  - `MYSITE/food/`: The food app containing models, views, templates, and URLs.
  - `MYSITE/users/`: Handles user authentication and profile management.
  - `MYSITE/settings.py`: The main configuration file for the project.
  - `MYSITE/urls.py`: The main URL router for the project.

-----

### 📸 Screenshots

\<img width="1875" height="942" alt="image" src="[https://github.com/user-attachments/assets/aea4bb91-9f3a-4cbc-84ef-bb412a728096](https://github.com/user-attachments/assets/aea4bb91-9f3a-4cbc-84ef-bb412a728096)"\>

-----

### 📜 License

This project is for learning purposes and can be modified freely.
