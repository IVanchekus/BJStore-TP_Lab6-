# Generated by Django 4.0.2 on 2023-05-04 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_profiletocompanies_profile_proftocomp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='proftocomp',
        ),
    ]