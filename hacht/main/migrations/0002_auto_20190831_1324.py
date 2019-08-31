# Generated by Django 2.2.4 on 2019-08-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muestra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_sesion', models.PositiveIntegerField(null=True)),
                ('url_img', models.URLField(null=True)),
                ('pred', models.CharField(max_length=8, null=True)),
                ('accuracy', models.FloatField(null=True)),
                ('obs', models.CharField(max_length=200, null=True)),
                ('is_true', models.CharField(max_length=1, null=True)),
                ('consent', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_user', models.PositiveIntegerField(null=True)),
                ('identificador', models.EmailField(max_length=40, null=True)),
                ('sexo', models.CharField(max_length=1, null=True)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_N',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_user', models.PositiveIntegerField(null=True)),
                ('nombre', models.EmailField(max_length=40, null=True)),
                ('ced', models.CharField(max_length=10, null=True)),
                ('sexo', models.CharField(max_length=1, null=True)),
                ('edad', models.PositiveSmallIntegerField(null=True)),
                ('res', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_paciente', models.PositiveIntegerField(null=True)),
                ('date', models.DateField()),
                ('obs', models.CharField(max_length=500, null=True)),
                ('estado', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='correo',
            field=models.EmailField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombre',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='org',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
