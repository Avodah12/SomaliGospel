# Generated by Django 5.1.2 on 2024-11-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_imagecategory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
