# Generated by Django 4.1.5 on 2023-01-31 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_tournament_num_rounds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='seed',
            new_name='rating',
        ),
    ]
