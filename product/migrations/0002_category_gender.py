# Generated by Django 2.2.3 on 2019-08-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('man', 'Erkek'), ('women', 'Kadın'), ('unisex', 'Unisex')], default='unisex', max_length=6),
        ),
    ]
