# Generated by Django 5.0.3 on 2024-07-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_name_comment_schedule_comment_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='schedule',
            field=models.TextField(null=True),
        ),
    ]