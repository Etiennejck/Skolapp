# Generated by Django 2.2.6 on 2019-11-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCHOOL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='nombrePlaces',
            field=models.IntegerField(null=True, verbose_name='capacitée de la classe'),
        ),
    ]
