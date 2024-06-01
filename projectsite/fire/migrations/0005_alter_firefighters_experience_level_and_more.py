# Generated by Django 4.2.11 on 2024-06-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire', '0004_alter_firefighters_experience_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firefighters',
            name='experience_level',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='firefighters',
            name='rank',
            field=models.CharField(choices=[('Probationary Firefighter', 'Probationary Firefighter'), ('Firefighter I', 'Firefighter I'), ('Firefighter II', 'Firefighter II'), ('Firefighter III', 'Firefighter III'), ('Driver', 'Driver'), ('Captain', 'Captain'), ('Battalion Chief', 'Battalion Chief')], max_length=150),
        ),
    ]