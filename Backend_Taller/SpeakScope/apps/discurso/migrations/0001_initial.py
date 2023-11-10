# Generated by Django 4.2.5 on 2023-11-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivoAudio', models.FileField(upload_to='audios/')),
                ('transcripcion', models.TextField()),
                ('resumen', models.TextField()),
                ('palabrasClave', models.TextField()),
                ('ideasClave', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
