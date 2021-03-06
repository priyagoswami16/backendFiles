# Generated by Django 4.0.1 on 2022-02-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgone', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('emailaddress', models.EmailField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('message', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('img', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Scrdile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtwo', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgthree', models.FileField(upload_to='static')),
            ],
        ),
    ]
