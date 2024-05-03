# Generated by Django 4.0.1 on 2024-05-03 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutdb', '0009_session_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutdb.session'),
            preserve_default=False,
        ),
    ]