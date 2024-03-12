# Generated by Django 5.0.1 on 2024-03-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0007_rename_leaving_id_leave_leave_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials/')),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]
