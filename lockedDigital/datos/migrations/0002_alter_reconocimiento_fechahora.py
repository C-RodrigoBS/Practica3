# Generated by Django 4.0.5 on 2022-07-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reconocimiento',
            name='fechaHora',
            field=models.TimeField(),
        ),
    ]