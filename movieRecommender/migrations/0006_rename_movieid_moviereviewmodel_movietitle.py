# Generated by Django 5.0.3 on 2024-03-24 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieRecommender', '0005_rename_review_moviereviewmodel_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviereviewmodel',
            old_name='movieid',
            new_name='movietitle',
        ),
    ]