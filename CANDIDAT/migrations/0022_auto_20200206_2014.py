# Generated by Django 2.2.6 on 2020-02-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CANDIDAT', '0021_auto_20200205_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_journal',
            field=models.TextField(null=True, verbose_name='notes des parents'),
        ),
    ]
