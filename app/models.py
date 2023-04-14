from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)
    rating = models.FloatField(default=0)


class Genre(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Publisher(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    binding = models.CharField(max_length=100)
    foundation_at = models.DateField()
    address = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    rating = models.FloatField(default=0)


class Book(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_at = models.DateField()
    pages = models.IntegerField()
    binding = models.CharField(max_length=100)
    is_e_book = models.BooleanField(default=False)
    edition = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre, through='AuthorGenre')
    publishers = models.ManyToManyField(Publisher)


class AuthorGenre(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
