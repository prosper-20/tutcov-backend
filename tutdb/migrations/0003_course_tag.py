# Generated by Django 4.0.1 on 2024-05-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutdb', '0002_alter_course_department_alter_course_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(choices=[('New', 'New'), ('Stale', 'Stale')], default='New', max_length=100),
        ),
    ]
