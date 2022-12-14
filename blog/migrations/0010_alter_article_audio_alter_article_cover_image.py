# Generated by Django 4.0.5 on 2022-06-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='audio',
            field=models.FileField(upload_to='blog/uploads/audios/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='cover_image',
            field=models.ImageField(upload_to='blog/uploads/images/%Y/%m/%d'),
        ),
    ]
