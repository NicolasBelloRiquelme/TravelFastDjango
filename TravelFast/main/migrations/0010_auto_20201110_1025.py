# Generated by Django 2.1.15 on 2020-11-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20201110_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularioregistro',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Media/'),
        ),
    ]