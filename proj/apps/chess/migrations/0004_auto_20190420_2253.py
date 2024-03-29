# Generated by Django 2.1.1 on 2019-04-20 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0003_chessgame_chesssnapshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chesssnapshot',
            name='action',
            field=models.CharField(choices=[('create_match', 'create_match'), ('join_match', 'join_match'), ('close_match', 'close_match'), ('resign_match', 'resign_match'), ('take_move', 'take_move'), ('suggest_move', 'suggest_move'), ('create_undo_request', 'create_undo_request'), ('approve_undo_request', 'approve_undo_request'), ('reject_undo_request', 'reject_undo_request'), ('undo_move', 'undo_move')], max_length=32),
        ),
    ]
