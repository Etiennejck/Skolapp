# Generated by Django 2.2.6 on 2020-02-02 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CANDIDAT', '0012_auto_20200202_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Parent',
        ),
        migrations.AddField(
            model_name='student',
            name='ParentFK',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='CANDIDAT.Parent'),
        ),
    ]
