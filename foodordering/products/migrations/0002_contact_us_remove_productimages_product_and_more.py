# Generated by Django 4.2.7 on 2023-12-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact_us",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=250)),
                ("message", models.TextField()),
                ("added_on", models.DateTimeField(auto_now_add=True)),
                ("is_approved", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "Contact Table",
            },
        ),
        migrations.RemoveField(
            model_name="productimages",
            name="product",
        ),
        migrations.RemoveField(
            model_name="productmetainformation",
            name="product",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
        migrations.DeleteModel(
            name="ProductImages",
        ),
        migrations.DeleteModel(
            name="ProductMetaInformation",
        ),
    ]
