# Generated by Django 4.0.4 on 2022-06-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='audio',
            field=models.FileField(blank=True, upload_to='blog/uploads/audios/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/uploads/images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, upload_to='blog/uploads/videos/%Y/%m/%d'),
        ),
    ]