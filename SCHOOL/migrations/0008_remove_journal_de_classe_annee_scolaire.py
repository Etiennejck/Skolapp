# Generated by Django 2.2.6 on 2020-02-10 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SCHOOL', '0007_auto_20200207_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal_de_classe',
            name='annee_scolaire',
        ),
    ]
