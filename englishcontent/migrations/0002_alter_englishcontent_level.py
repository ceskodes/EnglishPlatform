# Generated by Django 5.1 on 2024-08-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishcontent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='englishcontent',
            name='level',
            field=models.CharField(choices=[('A1', 'A1 - Beginner'), ('A2', 'A2 - Elementary'), ('B1', 'B1 - Intermediate'), ('B2', 'B2 - Upper-Intermediate'), ('C1', 'C1 - Advanced'), ('C2', 'C2 - Proficient')], max_length=2, verbose_name='English Level'),
        ),
    ]
