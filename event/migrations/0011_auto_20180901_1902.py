# Generated by Django 2.0.8 on 2018-09-01 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0010_auto_20180901_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='form',
            name='event',
        ),
        migrations.AddField(
            model_name='form',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forms', to='event.Event'),
        ),
    ]