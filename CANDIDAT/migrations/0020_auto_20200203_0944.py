# Generated by Django 2.2.6 on 2020-02-03 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CANDIDAT', '0019_auto_20200202_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Id_parentFK',
            new_name='parents_id',
        ),
    ]
