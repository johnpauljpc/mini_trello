# Generated by Django 5.2.3 on 2025-06-28 12:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterUniqueTogether(
            name='board',
            unique_together={('board_name', 'owner')},
        ),
    ]
