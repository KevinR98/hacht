# Generated by Django 2.2.4 on 2019-09-26 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190922_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muestra',
            name='id_sesion',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.Sesion'),
        ),
        migrations.AlterField(
            model_name='muestra',
            name='obs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='obs',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
