# Generated by Django 3.0.7 on 2020-06-28 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text_post', models.TextField(max_length=255)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_post_set', to=settings.AUTH_USER_MODEL)),
                ('text_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_post_set', to='blog.Blog')),
            ],
        ),
    ]