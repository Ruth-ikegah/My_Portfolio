# Generated by Django 3.2.9 on 2021-12-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_work_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='image_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
