# Generated by Django 3.2.16 on 2023-05-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0038_auto_20230209_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='draft_created_at',
            field=models.DateTimeField(default=None, help_text='Draft creation time', null=True, verbose_name='draft created at'),
        ),
    ]
