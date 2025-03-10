# Generated by Django 5.1.1 on 2025-02-24 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=225, null=True, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('role', models.CharField(blank=True, choices=[('admin', 'Admin'), ('manager', 'Manager'), ('operator', 'Operator')], max_length=9, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='warehouse_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='warehouse_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=225)),
                ('capacity', models.IntegerField()),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouses', to='warehouse.user')),
            ],
        ),
    ]
