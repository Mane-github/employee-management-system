# Generated by Django 5.0.1 on 2024-03-09 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='leaving_id',
            new_name='leave_id',
        ),
    ]