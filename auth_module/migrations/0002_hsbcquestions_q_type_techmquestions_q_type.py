# Generated by Django 4.2 on 2024-04-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hsbcquestions',
            name='Q_type',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='techmquestions',
            name='Q_type',
            field=models.TextField(default=True),
        ),
    ]
