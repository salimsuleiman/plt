# Generated by Django 4.0 on 2022-03-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0003_block_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='orphan',
            field=models.BooleanField(default=False),
        ),
    ]
