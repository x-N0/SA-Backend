# Generated by Django 2.2.6 on 2019-10-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialNetwork', '0004_auto_20191024_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
    ]
