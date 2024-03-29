# Generated by Django 3.2.9 on 2021-12-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_work_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='description',
            new_name='overview',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='work',
            name='live_site',
        ),
        migrations.RemoveField(
            model_name='work',
            name='problem_statement',
        ),
        migrations.AddField(
            model_name='work',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='work',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='work',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='work',
            name='image_6',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
