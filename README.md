
# BookSpot Services
This repository contains the source code for the BookSpot Services API, a RESTful API backend created using Django and Django REST Framework. It serves as the backend for an app that allows users to rate movies and books.

## Features

- Users can sign up and log in to use the app
- Users can rate movies and books
- Users can view their own ratings, as well as the average rating of a movie or book
- Admins can manage user accounts and content ratings

## Technologies

- Python 3.7
- Django 3.0
- Django REST Framework 3.11
- SQLite (development) / PostgreSQL (production)

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/username/BookSpot_Services.git
    ```

2. **Change to the project directory:**
    ```
    cd BookSpot_Services
    ```

3. **Install the required Python packages:**
    ```
    pip install -r requirements.txt
    ```

4. **Create a new file named ".env" in the project directory. Add the following environment variables:**
    ```
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    ALLOWED_HOSTS=localhost, 127.0.0.1
    ```

5. **Apply the database migrations:**
    ```
    python manage.py migrate
    ```

6. **Start the development server:**
    ```
    python manage.py runserver
    ```

7. **The API will be available at http://localhost:8000/**

## API Endpoints

### App Functionality Endpoints

| Method |  Url                          | Description                       |
|:-------|:------------------------------|:----------------------------------|
| GET    | **/api/movies/**              | Get a list of movies              |
| POST   | **/api/movies/**              | Add a new movie                    |
| GET    | **/api/movies/<int:pk>/**     | Get a specific movie              |
| PUT    | **/api/movies/<int:pk>/**     | Update a specific movie           |
| DELETE | **/api/movies/<int:pk>/**     | Delete a specific movie           |
| GET    | **/api/books/**               | Get a list of books               |
| POST   | **/api/books/**               | Add a new book                     |
| GET    | **/api/books/<int:pk>/**      | Get a specific book               |
| PUT    | **/api/books/<int:pk>/**      | Update a specific book            |
| DELETE | **/api/books/<int:pk>/**      | Delete a specific book            |
| GET    | **/api/wishlist/**            | Get the wishlist                  |
| POST   | **/api/wishlist/**            | Add a new item to the wishlist     |
| GET    | **/api/wishlist/<int:pk>/**   | Get a specific wishlist item      |
| DELETE | **/api/wishlist/<int:pk>/**   | Delete a specific wishlist item   |
| GET    | **/api/reviews/**             | Get a list of reviews              |
| POST   | **/api/reviews/**             | Add a new review                   |
| GET    | **/api/reviews/<int:pk>/**    | Get a specific review             |
| PUT    | **/api/reviews/<int:pk>/**    | Update a specific review          |
| DELETE | **/api/reviews/<int:pk>/**    | Delete a specific review          |

### Authentication Endpoints

| Method |  Url                  | Description                    |
|:-------|:----------------------|:-------------------------------|
| POST   | **/auth/signup/**   | Register a new user            |
| POST   | **/auth/login/**      | Log in and get an auth token    |
| POST   | **/auth/logout/**     | Log out and invalidate token   |
| GET    | **/auth/get_user/**       | Get details of authenticated user |
