# Generated by Django 5.0.7 on 2024-08-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_remove_feedbackstaffs_leave_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminhod',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
