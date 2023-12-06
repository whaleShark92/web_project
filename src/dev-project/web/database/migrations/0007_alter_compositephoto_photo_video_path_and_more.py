# Generated by Django 4.2.5 on 2023-09-30 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_compositephoto_content_a_compositephoto_content_b_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compositephoto',
            name='photo_video_path',
            field=models.ImageField(blank=True, null=True, upload_to='data/Composites/', verbose_name='照片/影片路徑'),
        ),
        migrations.AlterField(
            model_name='media',
            name='path',
            field=models.ImageField(blank=True, null=True, upload_to='data/media/', verbose_name='路徑'),
        ),
        migrations.AlterField(
            model_name='templatehtml',
            name='template_path',
            field=models.FileField(blank=True, null=True, upload_to='data/templates/', verbose_name='模板路徑'),
        ),
    ]
