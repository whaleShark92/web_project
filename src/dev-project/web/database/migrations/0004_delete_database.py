# Generated by Django 4.2.5 on 2023-09-30 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_eventparticipant_link_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Database',
        ),
    ]
