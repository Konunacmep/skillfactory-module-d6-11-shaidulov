# Generated by Django 3.1.1 on 2020-09-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200930_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='full_name',
            field=models.CharField(max_length=128, verbose_name='Имя'),
        ),
    ]
