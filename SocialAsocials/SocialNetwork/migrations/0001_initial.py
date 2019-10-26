# Generated by Django 2.2.6 on 2019-10-24 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_friends', models.PositiveIntegerField(auto_created=True, editable=False)),
                ('created', models.DateField(auto_created=True)),
                ('username', models.CharField(editable=False, max_length=20, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('telephone', models.CharField(blank=True, max_length=100)),
                ('birth', models.DateField(blank=True)),
                ('about_me', models.CharField(blank=True, max_length=255)),
                ('current_status', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('content', models.CharField(max_length=1255)),
                ('likes', models.IntegerField(default=0)),
                ('amount_comments', models.IntegerField(default=0)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialNetwork.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('content', models.CharField(max_length=400)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialNetwork.User')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialNetwork.Post')),
            ],
        ),
    ]
