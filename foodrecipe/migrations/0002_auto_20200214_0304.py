# Generated by Django 2.2.10 on 2020-02-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodrecipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddetail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
