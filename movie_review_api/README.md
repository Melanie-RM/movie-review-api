#  Movie Review App

A back-end Django web application that allows users to browse movies,
write reviews, like other users' reviews, and receive personalized movie
recommendations using TMDB API integration.

------------------------------------------------------------------------

##  Live Features

-    User Registration & Authentication (Login/Logout)
-    User Profile Management
-    Browse Movies (TMDB API Integration)
-    Create, Update & Delete Reviews
-    Like Reviews
-    5-Star Rating System
-    Personalized Movie Recommendations

------------------------------------------------------------------------

##  Built With

-   Python 3
-   Django
-   SQLite (Development)
-   PostgreSQL (Production Ready)
-   TMDB API
-   Gunicorn
-   Heroku Deployment

------------------------------------------------------------------------

## Project Structure

movie_review_project/ │ ├── movie_review/ \# Django project settings ├──
movie_review_app/ \# Main application ├── templates/ ├── static/ ├──
manage.py └── requirements.txt

------------------------------------------------------------------------

##  Installation Guide

### 1️ Clone Repository

``` bash
git clone https://github.com/yourusername/movie-review-app.git
cd movie-review-app
```

### 2️ Create Virtual Environment

``` bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️ Configure Environment Variables

Create a `.env` file:

    SECRET_KEY=your_secret_key
    DEBUG=True
    TMDB_API_KEY=your_tmdb_api_key

Get your TMDB API key from https://www.themoviedb.org/

### 5️ Run Migrations

``` bash
python manage.py makemigrations
python manage.py migrate
```

### 6️ Create Superuser

``` bash
python manage.py createsuperuser
```

### 7️ Start Development Server

``` bash
python manage.py runserver
```



------------------------------------------------------------------------

## API Endpoints

  Endpoint                Description
 
  /api/movies/            List movies
  /api/reviews/           Create & view reviews
  /api/recommendations/   Get recommendations

------------------------------------------------------------------------

##  Recommendation Logic

Recommendations are generated using:

-   User's highest rated movies
-   Frequently liked genres
-   Popular movies from TMDB
-   Basic collaborative filtering

------------------------------------------------------------------------

##  Security

-   CSRF Protection
-   Secure password hashing
-   Environment variable protection
-   Login-required views
-   Production-ready configuration

------------------------------------------------------------------------

##  Database Models

### Movie

-   tmdb_id
-   title
-   overview
-   release_date
-   poster

### Review

-   user (ForeignKey)
-   movie (ForeignKey)
-   rating
-   comment
-   created_at

### Like

-   user (ForeignKey)
-   review (ForeignKey)

------------------------------------------------------------------------

##  Deployment (Heroku)

1.  Add `gunicorn` to requirements.txt
2.  Create a Procfile
3.  Configure environment variables on Heroku
4.  Run production migrations

------------------------------------------------------------------------

##  Future Improvements

-   Watchlist feature
-   Advanced ML recommendations
-   Search & filtering
-   Pagination
-   Swagger API documentation

------------------------------------------------------------------------

##  Author

Melanie\
Django Developer\
Movie Review Project


