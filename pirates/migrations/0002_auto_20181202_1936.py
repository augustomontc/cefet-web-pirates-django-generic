# Generated by Django 2.1.3 on 2018-12-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesouro',
            name='img_tesouro',
            field=models.ImageField(upload_to='imgs', verbose_name='Imagem'),
        ),
    ]
