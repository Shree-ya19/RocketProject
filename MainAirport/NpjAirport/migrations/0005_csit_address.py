# Generated by Django 5.1.1 on 2024-09-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NpjAirport', '0004_rename_email_csit_email_rename_name_csit_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='csit',
            name='address',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
