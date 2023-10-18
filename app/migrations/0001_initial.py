# Generated by Django 4.1.7 on 2023-04-12 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("alias", models.CharField(blank=True, max_length=100)),
                ("date_of_birth", models.DateField()),
                ("date_of_death", models.DateField(blank=True, null=True)),
                ("country", models.CharField(max_length=100)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="authors/")),
                ("rating", models.FloatField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AuthorGenre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.author"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("binding", models.CharField(max_length=100)),
                ("foundation_at", models.DateField()),
                ("address", models.CharField(max_length=100)),
                ("owner", models.CharField(max_length=100)),
                ("rating", models.FloatField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("published_at", models.DateField()),
                ("pages", models.IntegerField()),
                ("binding", models.CharField(max_length=100)),
                ("is_e_book", models.BooleanField(default=False)),
                ("edition", models.CharField(max_length=100)),
                ("is_published", models.BooleanField(default=False)),
                ("rating", models.FloatField(default=0)),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.author"),
                ),
                ("genre", models.ManyToManyField(through="app.AuthorGenre", to="app.genre")),
                ("publishers", models.ManyToManyField(to="app.publisher")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="authorgenre",
            name="book",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.book"),
        ),
        migrations.AddField(
            model_name="authorgenre",
            name="genre",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.genre"),
        ),
    ]
