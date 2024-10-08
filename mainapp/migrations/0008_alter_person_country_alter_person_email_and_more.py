# Generated by Django 5.1 on 2024-08-27 19:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_person_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='english_level',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='English Level'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=15, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='person',
            name='plan_status',
            field=models.BooleanField(default=False, verbose_name='Plan Status'),
        ),
        migrations.AlterField(
            model_name='person',
            name='plan_subscribed',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Plan Subscribed'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
