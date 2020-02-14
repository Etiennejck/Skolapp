# Generated by Django 2.2.6 on 2020-02-05 08:27

import CANDIDAT.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('CANDIDAT', '0020_auto_20200203_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parent',
            options={'ordering': ['-dateInscription']},
        ),
        migrations.AddField(
            model_name='student',
            name='class_journal',
            field=models.TextField(null=True, verbose_name='Journal de classe'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='BE'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='mail',
            field=models.EmailField(help_text='addresse email', max_length=254, validators=[CANDIDAT.models.validate_email]),
        ),
        migrations.AlterField(
            model_name='student',
            name='ClassePrecedente',
            field=models.IntegerField(default=1, validators=[CANDIDAT.models.validate_integer], verbose_name='Classe précédente'),
        ),
        migrations.AlterField(
            model_name='student',
            name='parents_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='CANDIDAT.Parent', verbose_name='Parent'),
        ),
    ]