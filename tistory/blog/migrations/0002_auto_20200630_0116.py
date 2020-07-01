# Generated by Django 3.0.7 on 2020-06-30 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_post_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='text_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_post_set', to='blog.Blog'),
        ),
        migrations.AddField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
