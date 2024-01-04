# Generated by Django 4.2.7 on 2024-01-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('discription', models.TextField()),
                ('price', models.CharField(max_length=6)),
                ('category', models.ManyToManyField(to='categories.category')),
            ],
        ),
    ]
