# Generated by Django 3.2.7 on 2021-09-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=999, null=True),
        ),
    ]