# Generated by Django 4.0 on 2022-03-16 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0005_orphanblock_block_transactions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='orphan',
            new_name='added_to_bc',
        ),
    ]