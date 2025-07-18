# Generated by Django 5.2.4 on 2025-07-04 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recompensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Progreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_avance', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('intentos_realizados', models.IntegerField(default=0)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.nivel')),
            ],
        ),
    ]
