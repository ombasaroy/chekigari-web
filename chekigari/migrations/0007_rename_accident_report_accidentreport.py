# Generated by Django 5.2 on 2025-04-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chekigari', '0006_alter_body_type_options_alter_damageseverity_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='accident_report',
            new_name='AccidentReport',
        ),
    ]
