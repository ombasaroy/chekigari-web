# Generated by Django 5.2 on 2025-04-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chekigari', '0007_rename_accident_report_accidentreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accidentreport',
            name='report_id',
        ),
        migrations.AddField(
            model_name='accidentreport',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
