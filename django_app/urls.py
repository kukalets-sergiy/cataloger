import os

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.views import (
    AuthorAPI,
    FileUploadAPI,
    BookAPI,
    BookAuthorAPI,
    BookPublisherAPI,
    BookGenreAPI,
    BookYearAPI,
    PublisherAPI,
    PublisherGenreAPI,
    GenreAPI,
    AuthorGenreAPI,
)

urlpatterns = [
    path(f"api/{os.getenv('API_VERSION')}/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        f"api/{os.getenv('API_VERSION')}/token/refresh", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path(f"api/{os.getenv('API_VERSION')}/author", AuthorAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/author/<author_id>", AuthorAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/author/<author_id>/upload", FileUploadAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/book", BookAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/book/<book_id>", BookAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/book/author/<author_id>", BookAuthorAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/book/publisher/<publisher_id>", BookPublisherAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/book/genre/<genre_id>", BookGenreAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/book/publisher/<published_at>", BookYearAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/publisher", PublisherAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/publisher/<publisher_id>", PublisherAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/publisher/genre/<publisher_id>", PublisherGenreAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/genre", GenreAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/genre/<genre_id>", GenreAPI.as_view()),
    path(f"api/{os.getenv('API_VERSION')}/genre/author/<author_id>", AuthorGenreAPI.as_view()),
]
