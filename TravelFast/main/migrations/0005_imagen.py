# Generated by Django 2.1.15 on 2020-11-10 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201109_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='Viajes')),
            ],
        ),
    ]