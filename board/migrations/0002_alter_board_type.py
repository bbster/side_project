# Generated by Django 3.2.4 on 2021-07-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
