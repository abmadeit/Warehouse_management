# Generated by Django 5.1.1 on 2024-09-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
