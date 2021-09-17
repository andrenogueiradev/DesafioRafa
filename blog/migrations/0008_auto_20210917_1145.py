# Generated by Django 3.2.7 on 2021-09-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_authorimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='authorimage',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto do Autor'),
        ),
    ]