import os
from datetime import datetime
from pathlib import Path

from django.core.files.storage import default_storage
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.decorators import *
from app.serializers import *
from app.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings


class AuthorAPI(APIView):
    def get(self, request, author_id=None):
        if author_id is not None:
            try:
                author = Author.objects.get(pk=author_id)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = AuthorSerializer(author)
            return Response(serializer.data, status=status.HTTP_200_OK)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(unauthenticated_user)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def put(self, request, author_id):
        try:
            author = Author.objects.get(pk=author_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def delete(self, request, author_id):
        try:
            author = Author.objects.get(pk=author_id)
        except ObjectDoesNotExist:
            return Response({"message": "Автор не існує"}, status=status.HTTP_404_NOT_FOUND)

        author.delete()
        return Response({"message": "Автор успішно видалений"}, status=status.HTTP_204_NO_CONTENT)


class BookAPI(APIView):
    def get(self, request, book_id=None):
        if book_id is not None:
            try:
                book = Book.objects.get(pk=book_id)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)

        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(unauthenticated_user)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def put(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def delete(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherAPI(APIView):
    def get(self, request, publisher_id=None):
        if publisher_id is not None:
            try:
                publisher = Publisher.objects.get(pk=publisher_id)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PublisherSerializer(publisher)
            return Response(serializer.data, status=status.HTTP_200_OK)

        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(unauthenticated_user)
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            publisher = serializer.save()
            return Response(PublisherSerializer(publisher).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def put(self, request, publisher_id):
        try:
            publisher = Publisher.objects.get(pk=publisher_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PublisherSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def delete(self, request, publisher_id):
        try:
            publisher = Publisher.objects.get(pk=publisher_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreAPI(APIView):
    def get(self, request, genre_id=None):
        if genre_id is not None:
            try:
                genre = Genre.objects.get(pk=genre_id)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = GenreSerializer(genre)
            return Response(serializer.data, status=status.HTTP_200_OK)

        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(unauthenticated_user)
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            genre = serializer.save()
            return Response(GenreSerializer(genre).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def put(self, request, genre_id):
        try:
            genre = Genre.objects.get(pk=genre_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    @method_decorator(unauthenticated_user)
    def delete(self, request, genre_id):
        try:
            genre = Genre.objects.get(pk=genre_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorGenreAPI(APIView):
    def get(self, request, author_id):
        author = Author.objects.get(id=author_id)
        books = Book.objects.filter(author=author)
        author_genre = AuthorGenre.objects.filter(book__in=books)
        return Response(AuthorGenreSerializer(author_genre, many=True).data)


class PublisherGenreAPI(APIView):
    def get(self, request, publisher_id):
        genres = Genre.objects.filter(publisher_id=publisher_id)
        return Response(PublisherSerializer(genres, many="many").data)


class BookAuthorAPI(APIView):
    def get(self, request, author_id):
        books = Book.objects.filter(author_id=author_id)
        return Response(BookSerializer(books, many="many").data)


class BookPublisherAPI(APIView):
    def get(self, request, publisher_id):
        books = Book.objects.filter(publisher_id=publisher_id)
        return Response(BookSerializer(books, many="many").data)


class BookGenreAPI(APIView):
    def get(self, request, genre):
        books = Book.objects.filter(genre=genre)
        return Response(BookSerializer(books, many="many").data)


class BookYearAPI(APIView):
    def get(self, request, published_at):
        books = Book.objects.filter(published_at=published_at)
        return Response(BookSerializer(books, many="many").data)


class FileUploadAPI(APIView):
    def post(self, request, author_id):
        file_obj = request.FILES["file"]

        if not self.validate_file_extension(file_obj.name):
            return Response(
                {"error": "Unsupported file extension."}, status=status.HTTP_406_NOT_ACCEPTABLE
            )

        current_date = datetime.now().strftime("%Y-%m-%d")
        file_path = f"{author_id}/{current_date}/{file_obj.name}"
        full_path_for_saving = os.path.join(settings.MEDIA_ROOT, "images", current_date)
        full_file_path = os.path.join(full_path_for_saving, file_obj.name)
        default_storage.save(full_file_path, file_obj)

        response_data = {"file_path": file_path}
        return Response(response_data, status=status.HTTP_201_CREATED)

    def validate_file_extension(self, filename):
        extension = Path(filename).suffix
        return extension in [".png", ".img", ".svg"]
