# Generated by Django 2.2.6 on 2020-02-02 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CANDIDAT', '0013_auto_20200202_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='ParentFK',
            new_name='IdParentFK',
        ),
    ]