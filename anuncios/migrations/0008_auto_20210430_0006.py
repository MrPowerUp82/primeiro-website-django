# Generated by Django 2.2.7 on 2021-04-30 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0007_remove_anuncio_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anuncio',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='anuncios/static/anuncios/img'),
        ),
    ]
