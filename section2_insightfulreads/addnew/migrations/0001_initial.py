# Generated by Django 4.2.2 on 2023-06-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('publishing_date', models.DateField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
