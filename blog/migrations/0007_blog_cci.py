# Generated by Django 5.0.3 on 2024-07-15 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_schedule_comment_time_begin_comment_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='CCI',
            field=models.CharField(max_length=250, null=True),
        ),
    ]