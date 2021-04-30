# Generated by Django 2.2.7 on 2021-04-30 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_anuncio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['titulo']},
        ),
        migrations.AddField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='static/anuncios/img/'),
        ),
    ]