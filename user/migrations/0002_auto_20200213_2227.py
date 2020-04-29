# Generated by Django 2.0.13 on 2020-02-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_rating_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.FloatField(default=0, null=True),
        ),
    ]
