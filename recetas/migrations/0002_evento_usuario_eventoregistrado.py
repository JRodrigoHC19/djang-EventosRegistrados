# Generated by Django 4.2.5 on 2023-10-16 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('week', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventoRegistrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_ini', models.DateTimeField()),
                ('fec_fin', models.DateTimeField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.usuario')),
            ],
        ),
    ]
