# Generated by Django 5.0 on 2024-01-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0002_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
