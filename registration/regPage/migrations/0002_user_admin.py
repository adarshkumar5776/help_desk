# Generated by Django 4.1.1 on 2022-10-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]