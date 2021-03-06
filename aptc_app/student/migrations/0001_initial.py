# Generated by Django 4.0.2 on 2022-03-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_class', models.IntegerField()),
                ('student_board', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=50)),
                ('student_gender', models.CharField(max_length=10)),
                ('student_date_of_birth', models.DateField(auto_now_add=True)),
                ('student_father_name', models.CharField(max_length=50)),
                ('student_phone_number', models.IntegerField()),
                ('student_receipt_number', models.IntegerField()),
                ('student_receipt_amount', models.IntegerField()),
                ('student_comments', models.CharField(max_length=100)),
                ('student_date_of_joining', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
