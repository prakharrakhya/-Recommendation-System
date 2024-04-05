# Generated by Django 5.0.3 on 2024-03-24 19:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieRecommender', '0008_alter_moviereviewmodel_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereviewmodel',
            name='movietitle',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='moviereviewmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]