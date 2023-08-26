# Generated by Django 4.2 on 2023-08-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0024_alter_tournament_entry_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentround',
            name='pairing_system',
            field=models.CharField(choices=[['ROUND_ROBIN', 'Round Robin'], ['SWISS', 'Swiss'], ['KOTH', 'KOTH'], ['RANDOM', 'Random'], ['MANUAL', 'Manual'], ['AUTO', 'Auto']], max_length=16),
        ),
    ]
