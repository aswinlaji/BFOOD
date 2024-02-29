# Generated by Django 5.0.1 on 2024-02-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_email', models.CharField(max_length=50, null=True)),
                ('l_password', models.CharField(max_length=50, null=True)),
                ('l_type', models.CharField(max_length=50, null=True)),
                ('l_status', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50, null=True)),
                ('Lname', models.CharField(max_length=50, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('Phone', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
