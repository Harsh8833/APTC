# Generated by Django 4.0.2 on 2022-03-01 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_detail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_detail',
            old_name='student_joining',
            new_name='student_date_of_joining',
        ),
    ]
