# Generated by Django 3.1.7 on 2021-04-03 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='re_password',
            new_name='reenter_password',
        ),
    ]
