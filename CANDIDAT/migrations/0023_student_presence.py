# Generated by Django 2.2.6 on 2020-02-10 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CANDIDAT', '0022_auto_20200206_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='presence',
            field=models.BooleanField(default=False),
        ),
    ]
